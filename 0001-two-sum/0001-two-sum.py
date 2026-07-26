class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dic = {}
        for i in range(n):
            comp = target - nums[i]

            if comp in dic:
                return[dic[comp], i]

            dic[nums[i]] = i