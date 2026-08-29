class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = dict()
        for i in s:
            if i in check:
                check[i] += 1
            else:
                check[i] = 1
        
        for i in t:
            if i not in check:
                return False
            if i in check:
                if check[i] == 0:
                    return False
                else:
                    check[i] -= 1
        
        for i in s:
            if check[i] != 0:
                return False
                
        return True