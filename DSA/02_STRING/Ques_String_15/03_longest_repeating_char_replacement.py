def longest_repeating_char_replacement(s: str, k: int) -> int:
    prev_char = s[0]
    ans = 0
    temp = 1
    lives = k
    size = len(s)
    for i in range(1, size):
        j = i
        while lives and j < size:
            if s[j] != prev_char:
                lives -= 1

            temp += 1
            prev_char = s[j]
            j += 1
        ans = max(temp, ans)
        lives = k
        temp = 0
    return ans


def main() -> None:
    print(f"ans={longest_repeating_char_replacement(s="AABBAABAA", k=3)}")


if __name__ == "__main__":
    main()
