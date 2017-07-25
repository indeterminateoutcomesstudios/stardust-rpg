from numbers import Real


def round_up(num: Real, num_digits: int=None) -> int:
    """Add a small epsilon in order to force .5 values to round up."""
    return round(num + 1e-8, num_digits)
