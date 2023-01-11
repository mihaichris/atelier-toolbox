"""Download class"""
import urllib.request
import sys
import time
from os import path, get_terminal_size, name
import itertools
from re import match
from toolbox.common.exceptions import DownloadException


class Download:

    def __init__(
        self,
        url,
        des=None,
        overwrite=False,
        continue_download=False,
        echo=False,
        quiet=False,
        batch=False,
        icon_done="▓",
        icon_left="░",
        icon_border="|"
    ):
        self.url = url
        self.des = des
        self.passed_dir = None
        self.headers = {}
        self.f_size = 0
        self.done_icon = icon_done if len(icon_done) < 2 else "▓"
        self.left_icon = icon_left if len(icon_left) < 2 else "░"
        self.border_left, self.border_right = self._extract_border_icon(
            icon_border)
        self._cycle_bar = None
        self.echo = echo
        self.quiet = quiet
        self.batch = batch
        self.overwrite = overwrite
        self.continue_download = continue_download
        self.file_exists = False
        self.ostream = sys.stderr if self.echo else sys.stdout
        self.basename = None
        self.conn = None
        self.req = None

    def _extract_border_icon(self, passed_icon):
        """"
        Extract the passed border icon according to
        what is passed.
        If the string has length equal to 2, then use the
        first char as left border icon and the second as
        right.
        If the string has length equal to 1, use the same icon for both.
        """
        if len(passed_icon) == 1:
            return passed_icon, passed_icon

        if len(passed_icon) == 2:
            return passed_icon[0], passed_icon[1]

        return "|", "|"

    def _build_headers(self, rem):
        """Build headers according to requirement."""
        self.headers = {"Range": f"bytes={rem}-"}
        print(f"Trying to resume download at: {rem} bytes", file=self.ostream)

    def _parse_exists(self):
        """This function should be called if the file already exists.
        In that case there are two possibilities, it's partially downloaded
        or it's a proper file.
        """
        if self.overwrite:
            return
        if self.continue_download:
            cur_size = path.getsize(self.des)
            original_size = urllib.request.urlopen(self.url).info()[
                'Content-Length']

            if original_size is None:
                print("WARNING: Could not perform sanity check on partial download.",
                      file=self.ostream)
                self._build_headers(cur_size)
            elif cur_size < int(original_size):
                self._build_headers(cur_size)
        else:
            print("ERROR: File exists. See 'dw --help' for solutions.",
                  file=self.ostream)
            sys.exit(-1)

    def _preprocess_conn(self):
        """Make necessary things for the connection."""
        self.req = urllib.request.Request(url=self.url, headers=self.headers)
        self.conn = urllib.request.urlopen(self.req)
        self.f_size = self.conn.info()['Content-Length']
        if self.f_size is not None:
            self.f_size = int(self.f_size)

    def _get_terminal_length(self):
        """Return the length of the terminal."""
        # If quiet is passed, skip this calculation and return a default length
        if self.quiet:
            return 50

        cols = get_terminal_size().columns
        return cols if name != "nt" else cols - 1

    def _parse_destination(self):
        # Check if the des is passed
        if self.des is not None:
            if path.isdir(self.des):
                self.passed_dir = self.des
                self.des = path.join(self.des, self._get_name())
        else:
            self.des = self._get_name()

        # Put a check to see if file already exists.
        # Try to resume it if that's true
        if path.exists(self.des):
            self._parse_exists()
            self.file_exists = True

    def _is_valid_src_path(self, file_path):
        """Check to see if the path passed is
        a valid source path.
        A valid source path would be a file that
        is not a directory and actually a file
        present in the disk.
        """
        return not path.exists(file_path) or not path.isfile(file_path)

    def _parse_url(self):
        """
        The URL can be a file as well so in that case we
        will download each URL from that file.
        In case the URL is not a file and just a simple URL,
        download just that one.
        returns: A list of urls
        """
        if match(r"^https?://*|^file://*", self.url):
            return [self.url]

        # Below code will only be executed if the -b
        # flag is passed
        if not self.batch:
            print(f"{self.url}: not a valid URL. Pass -b if it is a file "
                  "containing various URL's and you want bulk download.")
            sys.exit(0)

        rel_path = path.expanduser(self.url)

        # Put a check to see if the file is present
        if self._is_valid_src_path(rel_path):
            print(f"{rel_path}: not a valid name or is a directory")
            sys.exit(-1)

        # If it's not an URL, read the contents.
        # Since the URL is not an actual URL, we're assuming
        # it is a file that contains URL's seperated by new
        # lines.
        with open(rel_path, "r", encoding="utf8") as rstream:
            return rstream.read().split("\n")

    def _get_name(self):
        """Try to get the name of the file from the URL."""

        file_name = 'temp'
        temp_url = self.url

        split_url = temp_url.split('/')[-1]

        if split_url:
            # Remove query params if any
            file_name = split_url.split("?")[0]

        return file_name

    def _format_size(self, size):
        """Format the passed size.
        If its more than an 1 Mb then return the size in Mb's
        else return it in Kb's along with the unit.
        """
        map_unit = {0: 'bytes', 1: "KB", 2: "MB", 3: "GB"}
        formatted_size = size

        no_iters = 0
        while formatted_size > 1024:
            no_iters += 1
            formatted_size /= 1024

        return (formatted_size, map_unit[no_iters])

    def _format_time(self, time_left):
        """Format the passed time depending."""
        unit_map = {0: 's', 1: 'm', 2: 'h', 3: 'd'}

        no_iter = 0
        while time_left > 60:
            no_iter += 1
            time_left /= 60

        return time_left, unit_map[no_iter]

    def _format_speed(self, speed):
        """Format the speed."""
        unit = {0: 'Kb/s', 1: 'Mb/s', 2: 'Gb/s'}

        inc_with_iter = 0
        while speed > 1000:
            speed = speed / 1000
            inc_with_iter += 1

        return speed, unit[inc_with_iter]

    def _get_speed_n_time(self, file_size_dl, beg_time, cur_time):
        """Return the speed and time depending on the passed arguments."""

        # Sometimes the beg_time and the cur_time are same, so we need
        # to make sure that doesn't raise a ZeroDivisionError in the
        # following line.
        if cur_time == beg_time:
            return "Inf", "", 0, ""

        # Calculate speed
        speed = (file_size_dl / 1024) / (cur_time - beg_time)

        # Calculate time left
        if self.f_size is not None:
            time_left = ((self.f_size - file_size_dl) / 1024) / speed
            time_left, time_unit = self._format_time(time_left)
        else:
            time_left, time_unit = 0, ""

        # Format the speed
        speed, s_unit = self._format_speed(speed)

        return round(speed), s_unit, round(time_left), time_unit

    def _get_pos(self, reduce_with_each_iter):
        if self._cycle_bar is None:
            self._cycle_bar = itertools.cycle(
                range(0, int(reduce_with_each_iter)))

        return next(self._cycle_bar) + 1

    def _get_bar(self, status, length, percent=None):
        """Calculate the progressbar depending on the length of terminal."""
        # Till now characters present is the length of status.
        # length is the length of terminal.
        # We need to decide how long our bar will be.
        cur_len = len(status) + 2  # 2 for bar

        if percent is not None:
            cur_len += 5  # 5 for percent

        reduce_with_each_iter = 40
        while reduce_with_each_iter > 0:
            if cur_len + reduce_with_each_iter > length:
                reduce_with_each_iter = int(reduce_with_each_iter / 2)
            else:
                break

        # Add space.
        space = length - (len(status) + 2 + reduce_with_each_iter + 5)
        status += fr'{" " * space}'

        if reduce_with_each_iter > 0:
            # Make BOLD
            status += "\033[1m"
            # Add color.
            status += "\033[1;34m"
            if percent is not None:
                done = int(percent / (100 / reduce_with_each_iter))
                status += fr"{self.border_left}{self.done_icon * done}\
                {self.left_icon * (reduce_with_each_iter - done)}{self.border_right}"
            else:
                current_pos = self._get_pos(reduce_with_each_iter)
                status_bar = " " * (current_pos - 1) if current_pos > 1 else ""
                status_bar += self.done_icon * 1
                status_bar += " " * int(reduce_with_each_iter - current_pos)
                status += fr"{self.border_left}{status_bar}{self.border_right}"

        status += "\033[0m"
        return status

    def _download(self):
        try:
            self._parse_destination()
            self._preprocess_conn()
            with open(self.des, 'ab') as wstream:
                if self.f_size is not None and self.quiet is False:
                    formatted_file_size, dw_unit = self._format_size(self.f_size)
                    print(f"Size: {round(formatted_file_size)} {dw_unit}", file=self.ostream)
                _owrite = (f"Overwriting: {self.des}" if (self.file_exists and self.overwrite)
                           else f"Saving as: {self.des}")
                if self.quiet:
                    self.ostream.write(_owrite)
                    self.ostream.write("...")
                else:
                    print(_owrite, file=self.ostream)
                    self.ostream.flush()
                file_size_dl = 0
                block_sz = 8192
                beg_time = time.time()
                while True:
                    buffer = self.conn.read(block_sz)
                    if not buffer:
                        break

                    file_size_dl += len(buffer)
                    wstream.write(buffer)
                    percent = ''

                    speed, s_unit, time_left, time_unit = self._get_speed_n_time(
                        file_size_dl,
                        beg_time,
                        cur_time=time.time()
                    )

                    if self.f_size is not None:
                        percent = file_size_dl * 100 / self.f_size

                    # Get basename
                    self.basename = path.basename(self.des)

                    # Calculate amount of space req in between
                    length = self._get_terminal_length()

                    f_size_disp, dw_unit = self._format_size(file_size_dl)

                    status = fr"{round(f_size_disp)} {dw_unit}-7s"
                    status += fr'| {speed}-3s {s_unit}'

                    if self.f_size is not None:
                        status += fr"|| ETA: {time_left} {time_unit}-4s "
                        status = self._get_bar(status, length, percent)
                        status += fr" {round(percent)}-4s"
                    else:
                        status = self._get_bar(status, length)

                    if not self.quiet:
                        self.ostream.write('\r')
                        self.ostream.write(status)
                        self.ostream.flush()

            wstream.close()
            if self.quiet:
                self.ostream.write("...success\n")
                self.ostream.flush()

        except KeyboardInterrupt:
            self.ostream.flush()
            print("Keyboard Interrupt passed. Exiting peacefully.")
            sys.exit(0)
        except DownloadException as exception:
            print(f'ERROR: {exception}')
            return False
        return True

    def is_quiet(self):
        """Return if download is quiet."""
        return self.quiet

    def download(self):
        """
        download will iterate through a list of possible url's
        and destinations and keep passing to the actual download
        method _download().
        """
        urls = self._parse_url()
        for url in urls:
            self.url = url
            self._download()
            self.des = self.passed_dir
