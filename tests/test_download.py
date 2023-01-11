"""Tests various methods of the Download
class.
All the methods that start with test are used
to test a certain function. The test method
will have the name of the method being tested
seperated by an underscore.
If the method to be tested is extract_content,
the test method name will be test_extract_content
"""

from hashlib import md5
from os import remove
import unittest

from src.toolbox.sets.dw.download import Download

TEST_URL = "https://github.com/mihaichris/atelier-toolbox/raw/main/tests/resources/test.zip"


class TestDownloader(unittest.TestCase):

    def test__extract_border_icon(self):
        """Test the _extract_border_icon method"""
        download = Download(TEST_URL, quiet=True)

        icon_one = download._extract_border_icon("#")
        icon_two = download._extract_border_icon("[]")
        icon_none = download._extract_border_icon("")
        icon_more = download._extract_border_icon("sdafasdfasdf")

        assert icon_one == ('#', '#'), "Should be ('#', '#')"
        assert icon_two == ('[', ']'), "Should be ('[', '])"
        assert icon_none == ('|', '|'), "Should be ('|', '|')"
        assert icon_more == ('|', '|'), "Should be ('|', '|')"

    def test__build_headers(self):
        """Test the _build_headers method"""
        download = Download(TEST_URL, quiet=True)

        download._build_headers(1024)
        header_built = download.headers

        assert header_built == {"Range": "bytes={}-".format(1024)}, \
            "Should be 1024"

    def test__preprocess_conn(self):
        """Test the _preprocess_conn method"""
        download = Download(TEST_URL, quiet=True)
        download._preprocess_conn()

        assert download.f_size == 154, "Should be 154"

    def test__format_size(self):
        """
        Test the function that formats the size
        """
        download = Download(TEST_URL, quiet=True)

        size, unit = download._format_size(255678999)

        # Size should be 243.83449459075928
        # and unit should be `MB`
        size = int(size)

        assert size == 243, "Should be 243"
        assert unit == "MB", "Should be MB"

    def test__format_time(self):
        """
        Test the format time function that formats the
        passed time into a readable value
        """
        download = Download(TEST_URL, quiet=True)

        time, unit = download._format_time(2134991)

        # Time should be 9 days
        assert int(time) == 9, "Should be 9"
        assert unit == "d", "Should be d"

        time, unit = download._format_time(245)

        # Time should be 4 minutes
        assert int(time) == 4, "Should be 4"
        assert unit == "m", "Should be m"

    def test_file_integrity(self):
        """
        Test the integrity of the downloaded file.
        We will test the test.zip file which has a hash
        of `a527ded21dc1c68eba11687453c3690d`.
        """
        hash = "a527ded21dc1c68eba11687453c3690d"

        download = Download(url=TEST_URL, quiet=True)
        download.download()

        # Once download is done, check the integrity
        _hash = md5(open("test.zip", "rb").read()).hexdigest()

        assert _hash == hash, "Integrity check failed for test.zip"

        # Remove the file now
        remove(download.basename)
