"""Smoke test: checks the package imports. Real tests come in Stage 2."""

import ratelimiter


def test_package_imports():
    assert hasattr(ratelimiter, "FixedWindowLimiter")
