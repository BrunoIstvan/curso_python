
def add(a, b):
    """
    Given two integers, return the sum.

    :param a: int
    :param b: int
    :return: int

    >>> add(2, 3)
    5
    >>> add(0, 0)
    0
    """
    return a + b

def div(a, b):
    """
    Given two integers, return the division.

    :param a: int
    :param b: int
    :return: int

    >>> div(21, 3)
    7.0
    >>> div(10, 10)
    1.0
    >>> div(10, 0)
    Traceback (most recent call last):
        ...
    ValueError: b can not be zero
    """
    if not b:
        raise ValueError('b can not be zero')
    return a / b


def count_vowels(word) -> int:
    """
    Given a sing word, return the total number of vowels in that single word

    :param word: str
    :return: int

    >>> count_vowels('Cusco')
    2
    >>> count_vowels('Manila')
    3
    >>> count_vowels('Shhhhhhh')
    0
    """

    return sum(1 for x in range(0, len(word)) if word[x].lower() in 'aeiou')
    


if __name__ == "__main__":
    import doctest
    doctest.testmod()