class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num = set(nums)
        length = 0
        cnt = 0

        for n in num:
            if (n - 1) not in num:
                length = 0
            
                while (n + length) in num:
                    length += 1

            cnt = max(length, cnt)

        return cnt