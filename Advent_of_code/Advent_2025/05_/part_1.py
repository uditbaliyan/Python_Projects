# from pathlib import Path

# BASE_DIR = Path(__file__).parent.absolute()

# def fresh_ingredient_count(ranges,ingredients,*arg):
#     answer = 0
#     for start,end in ranges:
#         print("-------------")

#         for ingredient in range(start,end+1):
#             if ingredient in ingredients:
#                 answer+=1
#                 ingredients.pop(ingredient)

#                 print(ingredient)
#     return answer


# def get_data(*arg):
#     file_path = BASE_DIR / "input_1.txt"
#     with open(file_path,"r") as file:
#         data = file.read()
#         ranges,ingredients = data.split("==")
#         ranges = ranges.split("\n")
#         ingredients = ingredients.split("\n")

#     ranges = [list(map(int,abc.split("-"))) for abc in ranges if abc != ""]
#     ingredients = { int(i):1 for i in ingredients if i != ""}
#     return ranges,ingredients


# def main(*arg):
#     # data =
#     ranges,ingredients=get_data()
#     answer = fresh_ingredient_count(ranges,ingredients)
#     print(answer)
# if __name__ == "__main__":
#     main()

from pathlib import Path

BASE_DIR = Path(__file__).parent


def parse_input():
    file_path = BASE_DIR / "input.txt"
    with open(file_path, "r") as f:
        raw = f.read().strip()

    block_ranges, block_ids = raw.split("\n\n")

    ranges = []
    for line in block_ranges.splitlines():
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    ingredients = [int(x) for x in block_ids.splitlines()]

    return ranges, ingredients


def is_fresh(ingredient, ranges):
    for start, end in ranges:
        if start <= ingredient <= end:
            return True
    return False


def count_fresh(ranges, ingredients):
    total = 0
    for ingredient in ingredients:
        if is_fresh(ingredient, ranges):
            total += 1
    return total


def main():
    ranges, ingredients = parse_input()
    answer = count_fresh(ranges, ingredients)
    print(answer)


if __name__ == "__main__":
    main()
