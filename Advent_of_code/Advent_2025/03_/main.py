from pathlib import Path
import itertools

BASE_DIR = Path(__file__).resolve().parent


# def maximums(bank:str):
#     a = ["0",-1]
#     b = ["0",-1]
#     answer = "0"
#     for idx,value in enumerate(bank):
#         if a[0]<value:
#             b[0],b[1] = a[0],a[1]
#             a[0],a[1] = value,idx
#         elif b[0]<value and value<a[0]:
#             b[0],b[1] = value,idx

#     if a[1]<b[1]:
#         answer = a[0]+b[0]
#     else:
#         answer = b[0]+a[0]
#     return answer


def add_two(temp, *args):
    """Docstring"""
    return temp[0] + temp[1]


def part_1(bank: str, *args):
    """Docstring"""
    all_combinations = itertools.combinations(bank, 2)
    combinations = map(add_two, all_combinations)
    # return all_combinations
    answer = "0"
    for element in combinations:
        # print(element)
        if answer < element:
            answer = element
    return answer


def add_it(temp, *args):
    """Docstring"""
    answer = "0"
    for i in temp:
        answer += i
    return answer


# def maximum(bank: str, *args):
#     """Docstring"""
#     all_combinations = itertools.combinations(bank, 12)
#     temp = max(all_combinations)
#     print("---<")
#     return ''.join(temp)


# def main(*arg):
#     input_file = BASE_DIR / "input.txt"
#     banks: list[str] = []
#     with open(input_file, "r") as file:
#         abc = file.read()
#         banks = abc.split("\n")

#     temp = sum(map(int, (map(maximum, banks))))
#     print(temp)


def pick_max_12(bank: str) -> str:
    """Return the largest 12-digit number formed by selecting digits in order."""
    k = 12
    stack = []
    drop = len(bank) - k

    for digit in bank:
        while drop and stack and stack[-1] < digit:
            stack.pop()
            drop -= 1
        stack.append(digit)

    return "".join(stack[:k])


def main():
    input_file = BASE_DIR / "input.txt"

    with open(input_file) as f:
        banks = f.read().splitlines()

    total = sum(int(pick_max_12(bank)) for bank in banks)
    print(total)


if __name__ == "__main__":
    main()
