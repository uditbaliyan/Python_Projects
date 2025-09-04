from math import prod
from typing import List


def product_of_array_except_self_1(arr: List[int]) -> List[int]:
    """iterating and dividing"""
    total_product = prod(arr)
    answer = [total_product // value for value in arr]
    return answer


def product_of_array_except_self_post_prefix(arr: List[int]) -> List[int]:
    """using pre and postfix"""
    size = len(arr)
    prefix = [None] * size
    abc = 1
    for idx, value in enumerate(arr):
        if idx == 0:
            prefix[idx] = 1
            abc *= value
            continue

        prefix[idx] = abc
        abc *= value

    postfix = [None] * size
    abc = 1
    idx = -1
    for value in reversed(arr):
        if idx == -1:
            postfix[idx] = 1
            idx = -2
            abc *= value
            continue

        postfix[idx] = abc

        abc *= value
        idx -= 1

    answer = [prefix[i] * postfix[i] for i in range(0, size)]
    return answer


def product_of_array_except_self_post_prefix_2(arr: List[int]) -> List[int]:
    answer = [None] * len(arr)
    abc = 1
    rev_idx = -1
    for idx, value in enumerate(arr):
        if idx == 0:
            answer[idx] = 1
            abc *= value
            continue
        answer[idx] = abc
        abc *= value

    for value in reversed(arr):
        if rev_idx == -1:
            abc = value
            rev_idx = -2
            continue
        answer[rev_idx] *= abc
        rev_idx -= 1
        abc *= value

    return answer


def product_except_self_division(arr: List[int]) -> List[int]:
    """
    Returns an array where each element is the product of all elements in
    the input array except the element at that index, using division.

    Assumes no zeros in the input array. If zeros are present, behavior is undefined.
    """
    if 0 in arr:
        raise ValueError("Input contains zero. Division approach is not valid.")

    total_product = prod(arr)
    return [total_product // value for value in arr]


def product_except_self_prefix_postfix(arr: List[int]) -> List[int]:
    """
    Returns an array where each element is the product of all elements in the input
    array except the element at that index,
    using prefix and postfix arrays (no division).
    """
    size = len(arr)
    if size == 0:
        return []

    prefix = [1] * size
    postfix = [1] * size

    # Build prefix product array
    for i in range(1, size):
        prefix[i] = prefix[i - 1] * arr[i - 1]

    # Build postfix product array
    for i in range(size - 2, -1, -1):
        postfix[i] = postfix[i + 1] * arr[i + 1]

    # Multiply prefix and postfix arrays
    return [prefix[i] * postfix[i] for i in range(size)]


def product_except_self_optimized(arr: List[int]) -> List[int]:
    """
    Optimized space approach (without using extra prefix/postfix arrays).
    Builds the result in one pass and modifies it with postfix in the second pass.
    """
    size = len(arr)
    if size == 0:
        return []

    result = [1] * size

    # Forward pass for prefix product
    prefix = 1
    for i in range(size):
        result[i] = prefix
        prefix *= arr[i]

    # Backward pass for postfix product
    postfix = 1
    for i in range(size - 1, -1, -1):
        result[i] *= postfix
        postfix *= arr[i]

    return result


def main():
    arr = [1, 2, 3, 4]
    print("Using division:", product_except_self_division(arr))
    print("Using prefix/postfix arrays:", product_except_self_prefix_postfix(arr))
    print("Optimized space:", product_except_self_optimized(arr))

    print(product_of_array_except_self_1(arr))
    print(product_of_array_except_self_post_prefix(arr))
    print(product_of_array_except_self_post_prefix_2(arr))


if __name__ == "__main__":
    main()
