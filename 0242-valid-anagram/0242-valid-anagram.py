class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        dict1 = {}
        for ch in s:
            if ch in dict1:
                dict1[ch]+=1
            else:
                dict1[ch]=1
        for ch in t:
            if ch not in dict1:
                return False
            dict1[ch]-=1
            if dict1[ch]<0:
                return False
        return True



        