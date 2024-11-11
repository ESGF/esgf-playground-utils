"""
Unit tests for the :py:mod:`esgf_playground_utils.utils.cf` module
"""

import unittest
from unittest.mock import Mock, patch

from utils import cf


class TestGetStandardNames(unittest.TestCase):
    """
    Test the functionality of the :py:func:`esgf_playground_utils.utils.cf.get_standard_names` function
    """

    def setUp(self) -> None:
        """Clear the cache of the :py:func:`esgf_playground_utils.utils.cf.get_standard_names` function"""

        cf.get_standard_names.cache_clear()
        super().setUp()

    @patch("defusedxml.ElementTree.parse")
    def test_get_standard_names(self, patched_element_tree_parse: Mock) -> None:
        """
        Should return a tuple the standard names
        """

        expected_result = ("name_1", "name_2")
        patched_element_tree_parse.return_value.getroot.return_value.findall.return_value = [
            {"id": "name_1"},
            {"id": "name_2"},
        ]

        result = cf.get_standard_names()
        self.assertTupleEqual(expected_result, result)
