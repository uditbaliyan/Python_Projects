def compare_string(str1: str, str2: str):
    size = len(str1)
    while size >= 0:
        if str2.startswith(str1[:size]):
            return str1[:size]
        size -= 1


def longest_common_prefix(arr: list[str]) -> str | None:
    prefix = arr[0]
    for string in arr:
        prefix = compare_string(prefix, string)
        if prefix is None:
            return None
    return prefix


def main() -> None:
    print(longest_common_prefix(["flower", "flow", "flight"]))


if __name__ == "__main__":
    main()
