"""Check a lab artifact against a separately trusted SHA-256 digest."""

from hashlib import sha256
from pathlib import Path
import sys


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 verify_release.py RELEASE_FILE")
        return 2
    root = Path(__file__).resolve().parent
    candidate = (root / sys.argv[1]).resolve()
    if candidate.parent != root or not candidate.is_file():
        print("FAIL: choose a release file in this lab directory")
        return 2
    trusted = (root / "trusted.sha256").read_text(encoding="ascii").strip().split()[0]
    observed = sha256(candidate.read_bytes()).hexdigest()
    if observed != trusted:
        print("FAIL: digest mismatch")
        return 1
    print("PASS: digest matches trusted manifest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
