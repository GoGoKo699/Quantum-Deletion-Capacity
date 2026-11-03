"""Run the finite scientific checks and compare their recorded reference values."""

import json
import math
from pathlib import Path
import platform

import numpy as np

from direct_kraus_blocks import run as run_direct
from independent_contraction import run as run_independent


def compare(actual, expected, absolute, relative, location="results"):
    """Compare numerical reference values with explicit portable tolerances."""
    if isinstance(expected, dict):
        if not isinstance(actual, dict) or set(actual) != set(expected):
            raise AssertionError(f"Key mismatch at {location}")
        for key, value in expected.items():
            compare(actual[key], value, absolute, relative, f"{location}.{key}")
    elif isinstance(expected, list):
        if not isinstance(actual, list) or len(actual) != len(expected):
            raise AssertionError(f"List length mismatch at {location}")
        for index, value in enumerate(expected):
            compare(actual[index], value, absolute, relative, f"{location}[{index}]")
    elif isinstance(expected, int):
        if actual != expected:
            raise AssertionError(f"Expected {expected!r}, got {actual!r} at {location}")
    elif isinstance(expected, float):
        if not math.isfinite(actual) or not math.isclose(
            actual, expected, rel_tol=relative, abs_tol=absolute
        ):
            raise AssertionError(f"Expected {expected!r}, got {actual!r} at {location}")
    elif actual != expected:
        raise AssertionError(f"Expected {expected!r}, got {actual!r} at {location}")


def main():
    reference_path = Path(__file__).resolve().with_name("expected-results.json")
    reference = json.loads(reference_path.read_text(encoding="utf-8"))
    tolerance = reference["tolerances"]
    results = {
        "direct_kraus_blocks": run_direct(tolerance["structural_absolute"]),
        "independent_contraction": run_independent(tolerance["structural_absolute"]),
    }
    compare(
        results,
        reference["results"],
        tolerance["reference_absolute"],
        tolerance["reference_relative"],
    )
    report = {
        "status": "passed",
        "runtime": {"python": platform.python_version(), "numpy": np.__version__},
        "tolerances": tolerance,
        "results": results,
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
