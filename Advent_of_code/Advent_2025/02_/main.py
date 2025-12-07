from pathlib import Path

BASE_DIR = Path()


def invaild_id_sum(ranges: list[str], *arg):
    answer = []
    for r in ranges:
        start, end = map(int, r.split("-"))
        for value in range(start, end):
            temp = str(value)
            size = len(temp) // 2
            if temp[0:size] == temp[size:]:
                answer.append(int(temp))
    return sum(answer)


def invaild_id_sum_I(ranges: list[str], *arg):
    answer = []
    for r in ranges:
        start, end = map(int, r.split("-"))
        for value in range(start, end):
            temp = str(value)
            size = len(temp) // 2
            if temp[0:size] * 2 == temp:
                answer.append(int(temp))
    return sum(answer)


def invaild_id_sum_II(ranges: list[str], *arg):
    answer = []
    for r in ranges:
        start, end = map(int, r.split("-"))
        for value in range(start, end):
            temp = str(value)
            if match_pattern(temp):
                answer.append(int(temp))
    return sum(answer)


def match_pattern(number: str):
    size = len(number)
    for i in range(1, size // 2 + 1):
        abc = size // i
        temp = number[0:i]
        x = temp * abc
        if x == number:
            return True
        print(number, "---", temp, "---", x)
    return False


def main(*arg):
    input_file = BASE_DIR / "input.txt"
    ranges: list[str] = []
    with open(input_file, "r") as file:
        abc = file.read()
        ranges = abc.split(",")
    print(invaild_id_sum_II(ranges=ranges))


if __name__ == "__main__":
    main()
