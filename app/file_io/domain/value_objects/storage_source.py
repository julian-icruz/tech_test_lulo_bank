from enum import Enum


class StorageSource(str, Enum):
    LOCAL = "local"
    AWS = "aws"
