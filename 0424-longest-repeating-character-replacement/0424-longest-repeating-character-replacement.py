class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        i = 0
        cnt = dict()

        while i < len(s):
            if s[i] not in cnt:
                cnt[s[i]] = 1

            else:
                cnt[s[i]] += 1

            if (i - l) + 1 - max(cnt.values()) <= k:
                pass
            
            else:
                cnt[s[l]] -= 1
                l += 1

            i += 1
            
        return (i - l)