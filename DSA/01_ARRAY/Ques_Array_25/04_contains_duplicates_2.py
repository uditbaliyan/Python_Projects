from typing import Dict, List


def contains_duplicate_in_window_k(arr: List[int], k: int) -> bool:
    seen: Dict[int, List[int]] = {}

    for idx, value in enumerate(arr):
        if seen.get(value):
            if idx - k in seen.get(value):
                return True
            else:
                seen.get(value).append(idx)
        else:
            seen[value] = [idx]
    return False
