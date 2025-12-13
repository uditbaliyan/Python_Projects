def first_n_sum(num: int) -> int:
    """:===:"""
    if num == 0:
        return 0
    return num + first_n_sum(num - 1)


def is_even(num: int) -> bool:
    return True if num % 2 == 0 else False


def first_n_even_sum(num: int, start: int = 0) -> int:
    """:===:"""
    if num <= start:
        return num
    return start + first_n_even_sum(num, start + 2)


def first_n_odd_sum(num: int, start: int = 1) -> int:
    """:===:"""
    if num <= start:
        return num
    return start + first_n_even_sum(num, start + 2)


def main() -> None:
    # print(first_n_sum(5))
    print(first_n_odd_sum(5))
    print(first_n_even_sum(6))


if __name__ == "__main__":
    main()
