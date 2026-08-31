class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = dict()
        ret = list()
        for n in nums:
        
            if n not in counter:
                counter[n] = 1
        
            else:
                counter[n] += 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        
        for n in set(nums): 
            freq[counter[n]].append(n)
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ret.append(n)

                if len(ret) == k:
                    return ret