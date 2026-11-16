class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            difference = target - num
            num_count = nums.count(difference)
            if (num_count != 0):
                if (nums.index(num) != nums.index(difference)):
                    num1 = nums.index(num)
                    num2 = nums.index(difference)
                    return [num1, num2]
            else:
                pass
            
        return False