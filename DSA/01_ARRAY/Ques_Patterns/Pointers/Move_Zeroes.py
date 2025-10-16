from typing import List

# -----------------------------------------------------------
# LeetCode 283. Move Zeroes
# -----------------------------------------------------------
# Problem:
# Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
# You must do this in-place without making a copy of the array.
#
# Example:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
#
# Constraints:
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# -----------------------------------------------------------


# -----------------------------------------------------------
# 🧩 Approach 1: Extra Array (Not In-Place)
# -----------------------------------------------------------
# - Append all non-zero elements to a new list
# - Then fill remaining positions with zeros
# - Finally, copy back to nums
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# -----------------------------------------------------------
def moveZeroes_extra_array(nums: List[int]) -> None:
    non_zero = [x for x in nums if x != 0]
    nums[:] = non_zero + [0] * (len(nums) - len(non_zero))


# -----------------------------------------------------------
# 🧩 Approach 2: Two Pointer Approach (Optimal)
# -----------------------------------------------------------
# - Use two pointers: `i` (for non-zero placement), `j` (for scanning)
# - Whenever nums[j] != 0, swap with nums[i], increment i
# - Ensures in-place modification
#
# Example:
# nums = [0,1,0,3,12]
# After iteration:
# [1,3,12,0,0]
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------------------------
def moveZeroes(nums: List[int]) -> None:
    i = 0  # position to place the next non-zero element
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1


# -----------------------------------------------------------
# 🧩 Approach 3: Counting Zeroes (Simpler but two passes)
# -----------------------------------------------------------
# - Count number of zeros
# - Move all non-zero numbers in place
# - Fill remaining positions with zeros
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# -----------------------------------------------------------
def moveZeroes_count(nums: List[int]) -> None:
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1
    for i in range(count, len(nums)):
        nums[i] = 0


# -----------------------------------------------------------
# ✅ Test Cases
# -----------------------------------------------------------
if __name__ == "__main__":
    tests = [
        [0, 1, 0, 3, 12],
        [0],
        [1, 2, 3, 0, 0],
        [0, 0, 1],
        [4, 2, 4, 0, 0, 3, 0, 5, 1, 0],
    ]

    for arr in tests:
        nums_copy = arr[:]  # keep original for display
        moveZeroes(nums_copy)
        print(f"Input: {arr}  =>  Output: {nums_copy}")


def moveZeroes_(nums: List[int]) -> None:
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
    moveZeroes_(nums=nums)
    print(nums)


if __name__ == "__main__":
    main()
