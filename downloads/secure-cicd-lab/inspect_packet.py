"""Inspect synthetic course fixtures. This does not verify a signature."""

from hashlib import sha256
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent


def read(name: str) -> dict:
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def main() -> int:
    provenance_name = sys.argv[1] if len(sys.argv) == 2 else "sample-provenance.json"
    if provenance_name not in {"sample-provenance.json", "sample-provenance-wrong-source.json"}:
        print("Usage: python3 inspect_packet.py [sample-provenance-wrong-source.json]")
        return 2
    policy = read("release-policy.json")
    dependencies = read("sample-dependency-change.json")
    sbom = read("sample-sbom.cdx.json")
    scorecard = read("sample-scorecard.json")
    provenance = read(provenance_name)
    actual_digest = sha256((ROOT / policy["artifact"]).read_bytes()).hexdigest()
    statement_digest = provenance["subject"][0]["digest"]["sha256"]
    build = provenance["predicate"]["buildDefinition"]
    source = build["resolvedDependencies"][0]["uri"]
    inputs = build["externalParameters"]
    builder = provenance["predicate"]["runDetails"]["builder"]["id"]
    print("Direct version:", dependencies["before"]["direct"][0]["version"], "->", dependencies["after"]["direct"][0]["version"])
    print("New transitive package:", dependencies["after"]["transitive"][0]["name"])
    print("SBOM component count:", len(sbom["components"]))
    print("Scorecard fixture:", scorecard["check"], scorecard["score"])
    checks = {
        "digest": actual_digest == statement_digest,
        "source": source == policy["source_repository"],
        "ref": inputs["ref"] == policy["source_ref"],
        "workflow": inputs["workflow"] == policy["workflow"],
        "builder": builder == policy["builder_id"],
    }
    for name, passed in checks.items():
        print(f"{name}: {'MATCH' if passed else 'MISMATCH'}")
    if not all(checks.values()):
        print("HOLD: illustrative policy mismatch")
        return 1
    print("MATCH: illustrative fields align. Signature not verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
