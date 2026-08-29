class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = dict()
        for i in s:
            check[i] = check.get(i, 0) + 1
        
        for i in t:
            if i not in check or check[i] == 0:
                return False
            else:
                check[i] -= 1
        
        for i in s:
            if check[i] != 0:
                return False

        return True