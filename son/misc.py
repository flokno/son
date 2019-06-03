"""Contains miscellaneous helpers like errors and warnings for son"""


class FileExistsError(Exception):
    """File exists, possibility of data loss"""


class EmptyStringWarning(Warning):
    """Signal an empty string"""


class EmptyFileWarning(Warning):
    """Signal an empty file"""
