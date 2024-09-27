#!/usr/bin/env python3
"""
`hashing` implementation

@authors:
@version: 2022.9
"""


def hash_remainder(key: int, size: int) -> int:
    """Finds hash using remainder

    :param key: key to hash
    :param size: size of the collection
    :return: hash value

    >>> hash_remainder(42, 7)
    0
    >>> hash_remainder(40, 9)
    4
    """
    return key % size


def hash_mid_sqr(key: int, size: int) -> int:
    """
    Finds hash using mid-square method

    :param key: key to hash
    :param size: size of the collection
    :return: hash value

    >>> hash_mid_sqr(4242, 7)
    3
    >>> hash_mid_sqr(424, 9)
    7
    """
    square = pow(key, 2)
    key = str(square)
    if len(key) % 2 != 0:
        key = str(0) + key
    mid = len(key) // 2
    return int(key[mid-1:mid+1]) % size


def hash_folding(key: str, size: int) -> int:
    """
    Finds hash using folding method

    :param key: key to hash
    :param size: size of the collection
    :return: hash value

    >>> hash_folding('(123) 456-7890', 7)
    4
    >>> hash_folding(424-7-23, 8)
    3
    """
    key = str(key)  # cast to string so I can index the input
    index = 0
    pairs = []
    numbers = 0
    while index < len(str(key)):  # parse the string, build a list of strings of only pairs of digits
        if key[index].isnumeric() and (numbers + 1) % 2 != 0:
            pairs.append([key[index]])
            numbers += 1
        elif key[index].isnumeric():
            pairs[len(pairs) - 1][0] += key[index]
            numbers += 1
        else:  # key[index] is non-numeric
            pass  # do nothing
        index += 1

    string_sum = 0  # the list now looks something like ['12','34','5'], now we sum up the strings
    for pair in pairs:
        string_sum += int(pair[0])
    return string_sum % size  # take mod and return


def hash_str(key: str, size: int) -> int:
    """
    Finds hash using sum-of-values method

    :param key: key to hash
    :param size: size of the collection
    :return: hash value

    >>> hash_str('aardvark', 7)
    4
    >>> hash_str('vardakar', 7)
    4
    """
    string_sum = 0
    for string in key:
        string_sum += ord(string)
    return string_sum % size


def hash_str_weighted(key: str, size: int) -> int:
    """
    Finds hash using weighted sum-of-values method

    :param key: key to hash
    :param size: size of the collection
    :return: hash value

    >>> hash_str_weighted('aardvark', 7)
    5
    >>> hash_str_weighted('vardakar', 7)
    2
    """
    string_sum = 0
    index = 0
    for string in key:
        string_sum += ord(string) * index
        index += 1
    return string_sum % size

