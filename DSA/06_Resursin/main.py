def is_odd(num: int) -> bool:
    return False if num % 2 == 0 else True


def first_n_odd(n: int) -> None:
    """"""
    if n == 0:
        return
    first_n_odd(n - 1)
    if is_odd(n):
        print(n)


def first_n_odd_reverse(n: int) -> None:
    """"""
    if n == 0:
        print(n)
        return
    if is_odd(n):
        print(n)
    first_n_odd_reverse(n - 1)


def is_even(num: int) -> bool:
    return True if num % 2 == 0 else False


def first_n_even(n: int) -> None:
    """"""
    if n == 0:
        print(n)
        return
    first_n_even(n - 1)
    if is_even(n):
        print(n)


def first_n_even_reverse(n: int) -> None:
    """"""
    if n == 0:
        print(n)
        return
    if is_even(n):
        print(n)
    first_n_even_reverse(n - 1)


def first_n(n: int) -> None:
    """"""
    if n == 0:
        print(n)
        return
    first_n(n - 1)
    print(n)


def first_n_reverse(n: int, start: int = 0) -> None:
    """"""

    if start == n:
        print(start)
        return

    first_n_reverse(n, start + 1)
    print(start)


def first_n_reverse_II(n: int) -> None:
    """"""

    if n == 0:
        print(n)
        return
    print(n)
    first_n_reverse_II(n - 1)


def main() -> None:
    # print(first_n(20))
    # print(first_n_reverse(20))
    # print(first_n_reverse_II(20))

    # first_n_even(20)
    # first_n_odd(20)

    # first_n_even_reverse(200)
    first_n_odd_reverse(20)


if __name__ == "__main__":
    main()
