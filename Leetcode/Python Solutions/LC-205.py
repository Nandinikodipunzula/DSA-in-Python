class Solution:
    def genPattern(self, s :str) -> str:
        indexMap = {}
        pattern = []
        for i , char in enumerate(s):
            if char not in indexMap:
                indexMap[char] = i
            pattern.append(str(indexMap[char]))
        return " ".join(pattern)

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.genPattern(s) == self.genPattern(t)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.isIsomorphic('abc','deb'))

#Time complexity : O(n)
