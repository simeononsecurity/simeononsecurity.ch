"""A dependency-free command-line unit converter for beginner practice."""

from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation
from typing import Sequence

METERS_TO_FEET = Decimal("3.28084")


def convert_meters_to_feet(raw_value: str) -> Decimal:
    """Convert a nonnegative meter value to feet, rounded to two places."""
    try:
        meters = Decimal(raw_value)
    except InvalidOperation as exc:
        raise ValueError("meters must be a number") from exc
    if not meters.is_finite() or meters < 0:
        raise ValueError("meters must be a finite, nonnegative number")
    return (meters * METERS_TO_FEET).quantize(Decimal("0.01"))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Convert meters to feet.")
    parser.add_argument("meters", help="finite, nonnegative meter value")
    args = parser.parse_args(argv)
    try:
        feet = convert_meters_to_feet(args.meters)
    except ValueError as exc:
        parser.error(str(exc))
    print(f"{args.meters} meters = {feet} feet")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
