from typing import List


def all_possible_subarray(arr: List[int]):
    """ """
    size = len(arr)
    for i in range(0, size):
        prev, next = 0, i + 1
        while next <= size:
            print(arr[prev:next])
            prev += 1
            next += 1


def max_subarray_product(arr: List[int]) -> int:
    """ """
    max_prod, temp_prod = 1, 1
    size = len(arr)
    for i in range(0, size):
        if arr[i] == 0:
            temp_prod = 0
            continue
        temp_prod *= arr[i]
        max_prod = max(max_prod, temp_prod)

    return max_prod


def main():
    arr = [-2, 1, -3, 4, 0, 2, 1, -5, 4]
    # all_possible_subarray(arr=arr)
    print(max_subarray_product(arr=arr))


if __name__ == "__main__":
    main()
