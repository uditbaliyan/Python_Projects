from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # ptr_z=0
    # ptr_nz=0
    # while ptr_nz < len(nums):
    #     if nums[ptr_z] != 0:
    #         ptr_z +=1
    #     if nums[ptr_nz] == 0:
    tz = nums.count(0)
    for _ in range(tz):
        nums.pop(nums.index(0))

    nums += [0] * tz


def main():
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums=nums)
    print(nums)


if __name__ == "__main__":
    main()
