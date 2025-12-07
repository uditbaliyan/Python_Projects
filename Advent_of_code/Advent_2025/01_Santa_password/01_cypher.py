# BASE_DIR = Path.absolute()
document = "/home/udit/Documents/Github/Python_Projects/Advent_of_code/Advent_2025/01_Santa_password/pass.txt"


def part_1(rotations: list[str], *arg):
    Dial: int = 100
    current: int = 50
    answer = 0
    for value in rotations:
        direction, step = value[0], value[1:]
        print(value, "---", direction, "---", step, "==", end=" ")
        step = int(step)

        if direction.upper() == "R":
            current += step
        else:
            current -= step
        current = current % Dial
        if current == 0:
            answer += 1
        print(current)
    return answer


def part_2_2(rotations: list[str], *arg):
    Dial: int = 100
    current: int = 50
    answer = 0

    for value in rotations:
        direction, step = value[0], value[1:]
        # print(value,"---",direction,"---",step,"==",end=" ")
        step = int(step)
        d = -1
        if direction.upper() == "R":
            d = 1
        for _ in range(step):
            current += d
            current %= Dial
            if current == 0:
                answer += 1

    return answer


def part_2(rotations: list[str], *arg):
    Dial: int = 100
    current: int = 50
    answer = 0
    prev = 0
    for value in rotations:
        direction, step = value[0], value[1:]
        # print(value,"---",direction,"---",step,"==",end=" ")
        step = int(step)
        d = -1
        if direction.upper() == "R":
            d = 1
        current += step * d
        temp = list(range(prev, current + d, d))
        if 0 in temp:
            answer += 1
        current %= Dial
        # if current == 0:
        #     answer+=1
        prev = current
    return answer


with open(document, "r") as file:
    abc = file.read()
    rotations = abc.split("\n")
    print(len(rotations))
    print(part_2(rotations))

    """
    The dial starts by pointing at 50.
The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
The dial is rotated L30 to point at 52.
The dial is rotated R48 to point at 0.
The dial is rotated L5 to point at 95.
The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
The dial is rotated L55 to point at 0.
The dial is rotated L1 to point at 99.
The dial is rotated L99 to point at 0.
The dial is rotated R14 to point at 14.
The dial is rotated L82 to point at 32; during this rotation, it points at 0 once
    """
