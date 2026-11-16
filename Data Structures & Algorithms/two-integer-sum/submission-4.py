class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            difference = target - num
            if (nums.count(difference)!= 0):
                num1 = nums.index(num)
                num2 = nums.index(difference, num1+1)
                return [num1, num2]
            else:
                pass
            
        return False