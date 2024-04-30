class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return False
        if s == t:
            return True

        dictS = {} 
        
        for i in range(len(s)):
            dictS[s[i]] = dictS.get(s[i],0)+1
            dictS[t[i]] = dictS.get(t[i],0)-1
        for ch in dictS:
            if dictS.get(ch,0) !=0:
                return False
        return True

if __name__ == "__main__":
    s,t = 'anagram','nagrama'
    solution = Solution()
    ans:bool = solution.isAnagram(s,t)
    print('Is s and t are anagrams ? : ' , ans)