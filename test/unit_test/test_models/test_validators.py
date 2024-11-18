import unittest
from unittest.mock import MagicMock, patch

import httpx

from esgf_playground_utils.models.validators import (
    validate_any_url,
    validate_cf_standard_name,
)


class TestValidators(unittest.TestCase):
    """
    Test the functionality of the :py:func:`esgf_playground_utils.models.validators.validate_cf_standard_name`
    function.
    """

    def setUp(self) -> None:
        """Set up the `get_standard_names` patch"""

        patched_get_standard_names = patch(
            "esgf_playground_utils.models.validators.get_standard_names"
        )
        self.patched_get_standard_names = patched_get_standard_names.start()
        self.addCleanup(patched_get_standard_names.stop)
        super().setUp()

    def test_with_valid_standard_name(self) -> None:
        """Should return cf_standard_name."""

        expected_value = "standard_name"
        self.patched_get_standard_names.return_value = [expected_value]

        result = validate_cf_standard_name(expected_value)

        self.assertEqual(expected_value, result)

    def test_with_invalid_standard_name(self) -> None:
        """Should raise ValueError."""

        expected_value = "standard_name"
        self.patched_get_standard_names.return_value = [expected_value]

        with self.assertRaises(ValueError):
            validate_cf_standard_name("unexpected_value")

    """
    Test the functionality of the :py:func:`esgf_playground_utils.models.validators.validate_any_url` function.
    """

    def test_valid_url_without_check(self) -> None:
        """Should return the URL when valid and check_url is False."""
        value = "http://example.com"

        mock_info = MagicMock()
        mock_info.context = {"check_url": False}

        result = validate_any_url(value, mock_info)
        self.assertEqual(result, value)

    def test_invalid_url_format(self) -> None:
        """Should raise ValueError when URL format is invalid."""
        value = "invalid_url"

        mock_info = MagicMock()
        mock_info.context = {"check_url": False}

        with self.assertRaises(ValueError):
            validate_any_url(value, mock_info)

    @patch("httpx.head")
    def test_unreachable_url_with_check(self, mock_head: MagicMock) -> None:
        """Should raise ValueError when URL is unreachable and check_url is True."""
        mock_head.side_effect = httpx.RequestError("Unable to connect")
        value = "http://nonexistent.example.com"

        mock_info = MagicMock()
        mock_info.context = {"check_url": True}

        with self.assertRaises(ValueError):
            validate_any_url(value, mock_info)

    @patch("httpx.head")
    def test_valid_url_with_check(self, mock_head: MagicMock) -> None:
        """Should return the URL when valid and reachable and check_url is True."""
        mock_response = httpx.Response(200)
        mock_head.return_value = mock_response
        value = "http://example.com"

        mock_info = MagicMock()
        mock_info.context = {"check_url": True}

        result = validate_any_url(value, mock_info)
        self.assertEqual(result, value)
