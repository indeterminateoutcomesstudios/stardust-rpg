from numbers import Real


def round_up(num: Real) -> int:
    """Add a small epsilon in order to force .5 values to round up."""
    return round(num + 1e-8)
