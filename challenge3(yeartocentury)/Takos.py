def yearToCentury(year: int):
    """Gets the century of a year.

    Parameters:
        year (int): year to convert into century.

    Returns:
        int: century of the year.
    """

    century = 1 + ((year - 1) // 100)
    return century