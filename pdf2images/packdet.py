
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

    retcode = dpkg["-s", package] & RETCODE
    return retcode == 0


def check_system_package_exists_darwin(package: str):
    from plumbum.cmd import brew

    retcode = brew["list", package] & RETCODE
    return retcode == 0


def get_configurations():
    arch_packages = ["qpdf", "xpdf", "perl-image-exiftool"]
    arch_conf = {
        "packages": arch_packages,
        "check_system_package_exists": check_system_package_exists_archlinux,
        "install_instruction": "sudo pacman -Sy && sudo pacman -S --noconfirm {}".format(
            " ".join(arch_packages)
        ),
    }

    debian_packages = ["qpdf", "xpdf", "libimage-exiftool-perl"]
    debian_conf = {
        "packages": debian_packages,
        "check_system_package_exists": check_system_package_exists_debian,
        "install_instruction": "sudo apt update && sudo apt install -y {}".format(
            " ".join(debian_packages)
        ),
    }

    # a.k.a, macOS
    darwin_packages = [
        "freetype",
        "imagemagick",
        "qpdf",
        "xpdf",
        "exiftool",
        "libmagic",
        "ghostscript",