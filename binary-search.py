# Binary search 
from typing import List


def search(nums: List[int], target: int) -> int:
  length = len(nums) - 1
  low, high = 0, length
  while low <= high:
    mid = (low + high) // 2
    if nums [mid] == target:
      return mid
    elif nums[mid] > target:
      high = mid - 1
    else:
      low = mid + 1
  return -1
  
print(search([1, 7, 10, 15, 30, 40], 7))
