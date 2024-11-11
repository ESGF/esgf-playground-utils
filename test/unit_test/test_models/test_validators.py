import unittest
from unittest.mock import patch

from esgf_playground_utils.models.validators import validate_cf_standard_name


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
