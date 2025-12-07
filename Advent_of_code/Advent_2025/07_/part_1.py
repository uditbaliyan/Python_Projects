# # from helpers.filehandler import fh

# # def main():
# #     f = fh('input.txt')
# #     rows = f.get_rows() # This reads each row into string where \n gets removed
# #     timelines = [1 for _ in rows[0]] # [1,1,1,...]

# #     # start from bottom and combine timelines, index of 'S' is the real count
# #     for row in rows[::-1]:
# #         for i in range(len(row)):
# #             if row[i] == '^':
# #                 timelines[i] = timelines[i-1] + timelines[i+1]

# #     print(timelines[rows[0].index('S')])

# # if __name__ == '__main__':
# #     main()


# f=open('Advent_of_code/Advent_2025/07_/input.txt','r').read().strip().split("\n")

# fin = tuple(tuple(l) for l in f)

# from functools import cache

# @cache
# def doadv(fin,li,ci):
#     if li+1>=len(fin):
#         return 1
#     if fin[li+1][ci]=='.':
#         return doadv(fin,li+1,ci)
#     elif fin[li+1][ci]=='^':
#         return doadv(fin,li+1,ci+1)+doadv(fin,li+1,ci-1)
#     else:
#         return 'ERROR'

# li=0
# for ci,c in enumerate(fin[li]):
#     if(c=='S'):
#         print("going in",ci)
#         print(doadv(fin,li,ci))


def read_input_file(file_path: str) -> list[str]:
    with open(file=file_path, mode="r") as input_file:
        lines = input_file.readlines()
        return [line.strip() for line in lines]


def measure_time(func):
    def wrapper(*args, **kwargs):
        from time import perf_counter

        start_time = perf_counter()
        result = func(*args, **kwargs)
        print(f"Time (ms): {(perf_counter() - start_time) * 1000}")
        return result

    return wrapper


@measure_time
def solution(lines: list[str]):
    R, C = len(lines), len(lines[0])
    splitters = {}

    beam = None
    for r in range(R):
        for c in range(C):
            if lines[r][c] == "S":
                beam = c

            if lines[r][c] == "^":
                if r not in splitters:
                    splitters[r] = set()

                splitters[r].add(c)

    beams = set([beam])
    splits = 0

    for r in range(1, R):
        if r not in splitters:
            continue

        new_beams = set()
        while beams:
            beam = beams.pop()

            if beam not in splitters[r]:
                new_beams.add(beam)
            else:
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
                splits += 1

        beams = new_beams

    print(splits)


lines = read_input_file(file_path="Advent_of_code/Advent_2025/07_/input.txt")
solution(lines)
