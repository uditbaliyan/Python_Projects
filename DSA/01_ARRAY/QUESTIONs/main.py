from my_array_module.array_sorting import bubble_sort


def main(*args):
    """Docstring"""
    arr = [11, 2, 13, 4, 15, 6, 17, 8, 9, 10]
    print(f"unsorted arr = {arr}")
    bubble_sort(arr)
    print(f"sorted arr = {arr}")

    for i in sorted(arr):
        print(f"{i} ", end=" ")


if __name__ == "__main__":
    main()
