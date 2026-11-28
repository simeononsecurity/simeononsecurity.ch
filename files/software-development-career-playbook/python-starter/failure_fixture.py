"""Deliberate failing test used to prove delivery blocking."""

import unittest
from decimal import Decimal

from app import convert_meters_to_feet


class DeliberateFailure(unittest.TestCase):
    def test_wrong_expected_value(self) -> None:
        self.assertEqual(convert_meters_to_feet("1"), Decimal("99.99"))


if __name__ == "__main__":
    unittest.main()
