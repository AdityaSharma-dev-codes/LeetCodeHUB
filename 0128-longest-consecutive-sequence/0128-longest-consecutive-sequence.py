class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        length = 0
        if nums == []:
            return 0
        
        num = set(nums)
        cnt = 1

        for n in num:
            if (n - 1) not in num:
                length = 0
            
                while (n + length) in num:
                    length += 1

            cnt = max(length, cnt)

        return cnt