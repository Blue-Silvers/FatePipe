
from string import Formatter


def get_pattern_keys(pattern):
    """
    Returns the format keys for given pattern.

    Example:

        >>> get_pattern_keys("/pattern/{hello}/something_else/{world}/end")
        ['hello', 'world']

    Args:
        pattern: the pattern to parse for keys

    Returns:

    """
    return [fname for _, fname, _, _ in Formatter().parse(pattern) if fname]
