
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