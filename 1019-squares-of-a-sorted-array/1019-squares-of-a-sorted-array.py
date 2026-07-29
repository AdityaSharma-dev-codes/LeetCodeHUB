from collections import deque
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        sq = deque()
        l, r = 0, len(nums) - 1

        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])

            if left > right:
                sq.appendleft(left * left)
                l += 1
            
            else:
                sq.appendleft(right * right)
                r -= 1

        return list(sq)
