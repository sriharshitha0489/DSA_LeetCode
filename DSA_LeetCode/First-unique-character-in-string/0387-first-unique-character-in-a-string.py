class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr1=[]
        for ele in s:
            if s.count(ele)==1:
                return s.index(ele)
        return -1