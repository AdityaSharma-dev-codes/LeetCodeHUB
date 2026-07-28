class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() # -4, -1, -1, 0, 1, 2
        res = []
        n = len(nums)

        for i in range(n):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, n - 1

            while l < r:
                tt = nums[i] + nums[l] + nums[r]

                if tt == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while (l < r) and (nums[l] == nums[l-1]):
                        l += 1

                elif tt < 0:
                    l += 1
                    while (l < r) and (nums[l] == nums[l - 1]):
                        l += 1

                else:
                    r -= 1
                    while (l < r) and (nums[r] == nums[r + 1]):
                        r -= 1
                    
        
        return res