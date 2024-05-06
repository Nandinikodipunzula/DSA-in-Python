class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleLen =  len(needle)
        haystackLen  = len(haystack)

        i,j=0,0

        for i in range (haystackLen-needleLen+1):
            for j in range(needleLen):
                if haystack[i+j]!=needle[j]:
                    break
                if j==needleLen-1:
                    return i
        return -1

if __name__ == "__main__":
    solution = Solution()
    index = solution.strStr('happyohappy','appy')
    print(index)