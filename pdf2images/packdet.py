
"""Detect if system packages are installed and give friendly installation instruction if not."""

import platform
import distro
from loguru import logger
import os
import json

from plumbum import RETCODE


def assert_system_supported():
    p = platform.system()
    if p not in {"Linux", "Darwin"}:
        raise OSError("This package only works on Linux and macOS: `{}`".format(p))


def check_system_package_exists_archlinux(package: str):
    from plumbum.cmd import pacman

    retcode = pacman["-Q", package] & RETCODE
    return retcode == 0


def check_system_package_exists_debian(package: str):
    from plumbum.cmd import dpkg
