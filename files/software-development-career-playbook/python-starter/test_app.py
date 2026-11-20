"""Tests for the beginner unit converter."""

import unittest
from decimal import Decimal

from app import convert_meters_to_feet


class ConverterTests(unittest.TestCase):
    def test_one_meter(self) -> None:
        self.assertEqual(convert_meters_to_feet("1"), Decimal("3.28"))

    def test_zero_meters(self) -> None:
        self.assertEqual(convert_meters_to_feet("0"), Decimal("0.00"))

    def test_decimal_input(self) -> None:
        self.assertEqual(convert_meters_to_feet("2.5"), Decimal("8.20"))

    def test_negative_input_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            convert_meters_to_feet("-1")

    def test_text_input_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "number"):
            convert_meters_to_feet("secret")


if __name__ == "__main__":
    unittest.main()
