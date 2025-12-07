from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()


def math_homework(data: list[list[str]]):
    answer = []
    for i in range(0, 1000):
        eqs = (
            data[0][i]
            + data[-1][i]
            + data[1][i]
            + data[-1][i]
            + data[2][i]
            + data[-1][i]
            + data[3][i]
        )
        answer.append(eval(eqs))
    return sum(answer)


def get_data():
    file_path = BASE_DIR / "input.txt"
    with open(file_path, "r") as file:
        data = file.read().split("\n")
    r0 = [abc for abc in data[0].split(" ") if abc != ""]
    r1 = [abc for abc in data[1].split(" ") if abc != ""]
    r2 = [abc for abc in data[2].split(" ") if abc != ""]
    r3 = [abc for abc in data[3].split(" ") if abc != ""]
    r4 = [abc for abc in data[4].split(" ") if abc != ""]

    print(len(r1), len(r2), len(r0), len(r3), len(r4))

    return [r0, r1, r2, r3, r4]


def main():
    data = get_data()
    print(math_homework(data))


if __name__ == "__main__":
    main()
