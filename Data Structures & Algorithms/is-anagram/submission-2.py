class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if len(s) != len(t):
            return False
        array_s = list(s)
        array_t = list(t)
        array_s.sort()
        array_t.sort()
        indx_s =0
        indx_t = 0

        while indx_s < len(s) and indx_t <len(t):
            if array_s[indx_s] != array_t[indx_t]:
                return False
            indx_s +=1
            indx_t +=1
        return True


            
        