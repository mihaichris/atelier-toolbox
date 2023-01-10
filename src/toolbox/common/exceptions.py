"""Custom Exceptions module."""


class ConvertPDFException(Exception):
    """ConvertPDFException class."""

    def __init__(self, message):
        """ConvertPDFException constructor."""
        super().__init__()
        self.message = message

class DownloadException(Exception):
    """ConvertPDFException class."""

    def __init__(self, message):
        """ConvertPDFException constructor."""
        super().__init__()
        self.message = message
