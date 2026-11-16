class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            if (nums.count(target-num)!=0):
                num1 = nums.index(num)
                num2 = nums.index(target-num, num1+1)
                return [num1, num2]
            else:
                return False