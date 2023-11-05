"""Hashing Algorithms package."""
from enum import Enum


class HashingAlgorithms(str, Enum):
    """Hasing Algorithms enums"""
    SHA_512 = "sha512"
    SHA_256 = "sha256"
    MD5 = "md5"

    @classmethod
    def values(cls) -> list:
        """Get all values from class as list"""
        return list(map(lambda c: c.value, cls))
