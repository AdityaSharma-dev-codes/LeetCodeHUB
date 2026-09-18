class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = nums[0]

        while l <= r:
            m = min(nums[l], m)

            mid = (l + r) // 2
            m = min(nums[mid], m)

            if nums[mid] >= nums[l]:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return m
