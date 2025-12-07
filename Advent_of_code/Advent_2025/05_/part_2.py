# from pathlib import Path

# BASE_DIR = Path(__file__).parent


# def parse_input():
#     file_path = BASE_DIR / "input.txt"
#     with open(file_path, "r") as f:
#         raw = f.read().strip()

#     block_ranges, block_ids = raw.split("\n\n")

#     ranges = []
#     for line in block_ranges.splitlines():
#         start, end = map(int, line.split("-"))
#         ranges.append((start, end))

#     return ranges


# def count_fresh(ranges):
#     total = set()
#     for start, end in ranges:
#         for i in range(start,end+1):
#             total.add(i)
#         # temp = get_fresh(start,end)

#         # print(total)
#     return len(total)


# def main():
#     ranges= parse_input()
#     answer = count_fresh(ranges)
#     print(answer)


# if __name__ == "__main__":
#     main()
from pathlib import Path

BASE_DIR = Path(__file__).parent


def parse_input():
    file_path = BASE_DIR / "input.txt"
    with open(file_path, "r") as f:
        raw = f.read().strip()

    block_ranges, _ = raw.split("\n\n")

    ranges = []
    for line in block_ranges.splitlines():
        start, end = map(int, line.split("-"))
        ranges.append((start, end))

    return ranges


def merge_ranges(ranges):
    # Sort by start
    ranges.sort()

    merged = []
    cur_start, cur_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= cur_end + 1:  # overlapping or touching
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end

    merged.append((cur_start, cur_end))
    return merged


def count_fresh(ranges):
    merged = merge_ranges(ranges)
    total = 0
    for start, end in merged:
        total += end - start + 1
    return total


def main():
    ranges = parse_input()
    print(count_fresh(ranges))


if __name__ == "__main__":
    main()


"""
def mergeOverlap(arr):
    
    # Sort intervals based on start values
    arr.sort()

    res = []
    res.append(arr[0])

    for i in range(1, len(arr)):
        last = res[-1]
        curr = arr[i]

        # If current interval overlaps with the last merged
        # interval, merge them 
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)

    return res

if __name__ == "__main__":
    arr = [[7, 8], [1, 5], [2, 4], [4, 6]]
    res = mergeOverlap(arr)

    for interval in res:
        print(interval[0], interval[1])

"""
