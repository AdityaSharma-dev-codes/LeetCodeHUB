class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * (len(nums))
        print(ret)
        pref = 1
        post = 0
        for i in range(len(nums)):
            ret[i] = pref
            pref *= nums[i]
        
        post = 1

        for i in range(len(nums) - 1, -1, -1):
            ret[i] *= post
            post *= nums[i]

        return ret
