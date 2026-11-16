class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, number in enumerate(nums):
            difference = target - number
            if (difference in map):
                return [map[difference], index]
            map[number] = index
        return