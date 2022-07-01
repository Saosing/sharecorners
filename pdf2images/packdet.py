
"""Detect if system packages are installed and give friendly installation instruction if not."""

import platform
import distro
from loguru import logger
import os
import json

from plumbum import RETCODE


def assert_system_supported():
    p = platform.system()