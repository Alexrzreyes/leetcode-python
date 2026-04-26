def twoSum(nums: list[int], target: int) -> list[int]:
    map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in map:
            return [i, map[complement]]
        map[num] = i
    return []

print(twoSum([2, 7, 11, 15], 9)) # [0, 1]
print(twoSum([3, 2, 4], 6)) # [1, 2]
print(twoSum([3, 3], 6)) # [0, 1]