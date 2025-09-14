def fizz_buzz(n: int) -> list[str]:
    result = [None] * n
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result[i - 1] = "fizzbuzz"

        elif i % 3 == 0:
            result[i - 1] = "fizz"

        elif i % 5 == 0:
            result[i - 1] = "buzz"

        else:
            result[i - 1] = str(i)
    return result


def main() -> None:
    print(fizz_buzz(15))


if __name__ == "__main__":
    main()
