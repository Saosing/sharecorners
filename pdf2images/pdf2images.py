
import io
import traceback
import shutil
from typing import List, Dict
import os
import tempfile
from loguru import logger

from wand.image import Image


def pdf_data_to_thumbnails(
    pdf_data: bytes,
    pages: List[int],
    width_max: int,
    height_max: int,
    *,
    use_last_resort: bool = True
) -> Dict[int, bytes]:
    """
    Convert given pdf data to a set of images.

    :return: a dict map from page number to the binary data of image (which can be directly write to disk)
    """