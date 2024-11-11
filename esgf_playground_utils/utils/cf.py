"""
Utilities for reading bundled CF values
"""

import gzip
from functools import lru_cache
from pathlib import Path
from typing import Tuple

from defusedxml import ElementTree

_ROOT = Path(__file__).parent.parent
STANDARD_NAMES_FILE_PATH = (
    _ROOT / "vocabularies/cf_standard_names/cf-standard-name-table.xml.gz"
)


@lru_cache
def get_standard_names() -> Tuple[str, ...]:
    """Yield CF standard names from bundled XML CF specification (version 86)."""

    with gzip.GzipFile(STANDARD_NAMES_FILE_PATH.as_posix(), "rb") as xml_file:
        element_tree = ElementTree.parse(xml_file)

    standard_names_root = element_tree.getroot()
    standard_names = tuple(_.get("id") for _ in standard_names_root.findall("entry"))
    return standard_names
