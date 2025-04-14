"""
Test the functions in kafka.config module
"""

import unittest

from esgf_playground_utils.config.kafka import Settings


class TestSettings(unittest.TestCase):
    """Test the functionality of the Settings class"""

    def test_init(self) -> None:
        """Settings should be creatable with no additional import or env files"""

        settings = Settings()

        # This appears to be meaningless, but it is actually to prevent automatic code
        # formatters from removing the line (the test doesn't strictly need to assert anything, it just needs
        # not to raise an Exception)
        self.assertIsInstance(settings, Settings)
