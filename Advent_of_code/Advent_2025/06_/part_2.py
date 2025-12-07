from pathlib import Path
from collections import defaultdict
# BASE_DIR = Path(__file__).parent.resolve()

# def math_homework(data:list[list[str]]):
#     answer = []
#     for i in range(999,0,-1):
#         var = [data[j][i] for j in range(0,4)]
#         temp = len(max(var))
#         var = [j.zfill(4) for j in var]
#         operator = data[-1][i]
#         eqs = ""
#         for value in range(temp-1,-1):
#             for value in range(0,temp):
#                 var_1 = str(int(var[0][value] + var[1][] + var[2][-1] + var[3][-1]))

#         var_2 = str(int(var[0][-2] + var[1][-2] + var[2][-2] + var[3][-2]))
#         var_3 = str(int(var[0][-3] + var[1][-3] + var[2][-3] + var[3][-3]))
#         var_4 = str(int(var[0][-4] + var[1][-4] + var[2][-4] + var[3][-4]))


#         eqs = var_1 +  + var_2 + data[-1][i] + var_3 + data[-1][i] + var_4
#         print(i,":",var_1,var_2,var_3,var_4,data[-1][i],eval(eqs))
#         answer.append(eval(eqs))
#     return sum(answer)

# def get_data():
#     file_path = BASE_DIR / "input.txt"
#     with open(file_path,"r") as file:
#         data = file.read().split("\n")
#     r0=[abc for abc in data[0].split(" ") if abc != ""]
#     r1=[abc for abc in data[1].split(" ") if abc != ""]
#     r2=[abc for abc in data[2].split(" ") if abc != ""]
#     r3=[abc for abc in data[3].split(" ") if abc != ""]
#     r4=[abc for abc in data[4].split(" ") if abc != ""]

#     return [r0,r1,r2,r3,r4]


# def main():
#     data = get_data()
#     print(math_homework(data))


# if __name__ == "__main__":
#     main()

# from pathlib import Path

BASE_DIR = Path(__file__).parent

# def parse_input():
#     text = (BASE_DIR / "input.txt").read_text().rstrip("\n")
#     rows = text.split("\n")
#     # rows: 4 rows, equal width
#     width = len(rows[0])
#     return rows, width

# def solve_part2(rows, width):
#     problems = []
#     current_columns = []

#     def finish_problem():
#         if not current_columns:
#             return
#         # Build 3 numbers (top → bottom rows 0,1,2)
#         nums = ["", "", ""]
#         for col in current_columns:
#             for r in range(3):
#                 if col[r].isdigit():
#                     nums[r] += col[r]
#         # strip empty strings -> interpret as 0
#         nums = [int(n) if n else 0 for n in nums]

#         # Operator is bottom of any column
#         op = current_columns[-1][3]

#         if op == "+":
#             value = nums[0] + nums[1] + nums[2]
#         else:
#             value = nums[0] * nums[1] * nums[2]

#         problems.append(value)

#     i = 0
#     while i < width:
#         col = [rows[r][i] for r in range(4)]
#         if all(c == " " for c in col):
#             finish_problem()
#             current_columns = []
#         else:
#             current_columns.append(col)
#         i += 1

#     finish_problem()

#     return sum(problems)

# from pathlib import Path

# def load():
#     rows = ((BASE_DIR/"input.txt").read_text()).splitlines()
#     W = len(rows[0])
#     return rows, W

# def solve(rows, W):
#     problems = []
#     cur = []

#     def finish():
#         if not cur:
#             return
#         # Build 3 numbers
#         nums = ["", "", ""]
#         for col in cur:
#             # read digits top → bottom
#             for r in range(3):
#                 ch = col[r]
#                 if ch.isdigit():
#                     nums[r] += ch
#         nums = [int(n) if n else 0 for n in nums]
#         op = cur[-1][3]
#         if op == "+":
#             val = nums[0] + nums[1] + nums[2]
#         else:
#             val = nums[0] * nums[1] * nums[2]
#         problems.append(val)

#     for i in range(W):
#         col = [rows[r][i] for r in range(4)]
#         if all(c == " " for c in col):
#             finish()
#             cur = []
#         else:
#             cur.append(col)

#     finish()
#     return sum(problems)

# def fname(rows:list[str],operators:list[str],width:int):
#     eqs = []
#     num =""
#     eq = ""
#     k=999
#     for i in range(width-1,-1,-1):
#         var_1,var_2,var_3,var_4 = rows[0][i],rows[1][i],rows[2][i],rows[3][i]
#         if (var_1,var_2,var_3,var_4).count(" ") != 4:
#             num = var_1+var_2+var_3+var_4
#             eq = eq+num+operators[k]
#         else:
#             eqs.append(eval(eq[:-1]))
#             eq = ""
#             k-=1

#     return sum(eqs)

# def abc(data):
#     r4=[abc for abc in data.split(" ") if abc != ""]
#     return r4
# def main():
#     # data = get_data
#     rows,width = load()
#     # print(rows[0])
#     operators = abc(rows[-1])
#     print(fname(rows,operators,width))


# if __name__ == "__main__":
#     main()


def calc_nums(col, op):
    if op == "+":
        return sum(col)
    prod = 1
    for v in col:
        prod *= v
    return prod


with open(BASE_DIR / "input.txt", "r") as file:
    data = file.read()
    lines = data.splitlines()
    vals = defaultdict(list)
    for i in range(len(lines) - 1):
        line = lines[i]
        nums = [int(x) for x in line.split()]
        for j in range(len(nums)):
            vals[j].append(nums[j])
    ops = lines[-1].split()
    ans = 0
    for i in range(len(ops)):
        ans += calc_nums(vals[i], ops[i])
    print(ans)

with open(BASE_DIR / "input.txt", "r") as file:
    data = file.read()
    lines = data.splitlines()
    nums = []
    cur_op = ""
    max_len = max(len(line) for line in lines)
    ans = 0
    for x in range(max_len):
        cur_num = 0
        for y in range(len(lines)):
            if x < len(lines[y]):
                if lines[y][x] in "+*":
                    cur_op = lines[y][x]
                elif lines[y][x] == " ":
                    pass
                else:
                    cur_num *= 10
                    cur_num += int(lines[y][x])
        if cur_num != 0:
            nums.append(cur_num)
        else:
            ans += calc_nums(nums, cur_op)
            nums = []
    ans += calc_nums(nums, cur_op)
    print(ans)
# 10149018945413
# 10153315705125
