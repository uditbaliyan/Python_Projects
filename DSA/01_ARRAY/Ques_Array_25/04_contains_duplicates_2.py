from typing import List, Dict


def contains_nearby_duplicate_brute_force(nums: List[int], k: int) -> bool:
    """
    Brute force approach using nested loops.
    Time complexity: O(n * k)
    Space complexity: O(1)
    Not efficient for large arrays or large k.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, min(i + k + 1, n)):
            if nums[i] == nums[j]:
                return True
    return False


def contains_nearby_duplicate_hashmap(nums: List[int], k: int) -> bool:
    """
    Uses a hashmap to track the most recent index of each number.
    Time complexity: O(n)
    Space complexity: O(n)
    Efficient and recommended solution.
    """
    index_map: Dict[int, int] = {}
    for i, num in enumerate(nums):
        if num in index_map and i - index_map[num] <= k:
            return True
        index_map[num] = i
    return False


def contains_nearby_duplicate_set_sliding_window(nums: List[int], k: int) -> bool:
    """
    Uses a sliding window with a set to maintain the last k elements.
    Time complexity: O(n)
    Space complexity: O(min(n, k))
    Efficient for large arrays with small k.
    """
    seen = set()
    for i, num in enumerate(nums):
        if num in seen:
            return True
        seen.add(num)
        if len(seen) > k:
            seen.remove(nums[i - k])
    return False


def contains_nearby_duplicate_enumerate_zip(nums: List[int], k: int) -> bool:
    """
    Pythonic approach using enumerate and zip to check previous indices.
    Time complexity: O(n)
    Space complexity: O(n)
    Less readable, but compact.
    """
    last_seen: Dict[int, int] = {}
    for i, num in enumerate(nums):
        if num in last_seen and i - last_seen[num] <= k:
            return True
        last_seen[num] = i
    return False


# Optional: benchmarking and testing
def main():
    test_cases = [
        # Format: (nums, k)
        ([1, 2, 3, 1], 3),  # True
        ([1, 0, 1, 1], 1),  # True
        ([1, 2, 3, 1, 2, 3], 2),  # False
        ([], 0),  # False
        ([1], 0),  # False
        ([99, 99], 2),  # True
        ([1, 2, 3, 1, 2, 3], 3),  # True
    ]

    methods = [
        contains_nearby_duplicate_brute_force,
        contains_nearby_duplicate_hashmap,
        contains_nearby_duplicate_set_sliding_window,
        contains_nearby_duplicate_enumerate_zip,
    ]

    for i, (nums, k) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: nums = {nums}, k = {k}")
        for method in methods:
            result = method(nums.copy(), k)
            print(f"{method.__name__}: {result}")


if __name__ == "__main__":
    main()
