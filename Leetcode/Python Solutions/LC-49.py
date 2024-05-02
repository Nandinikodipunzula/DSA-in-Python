import collections
from typing import List

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for string in strs:
            key = "".join(sorted(string))
            if map.get(key,[]) == []:
                map[key] = []
            map.get(key).append(string)
        return map.values()
    
#time complexity(O(m*n*logn) , m - len of input , n- average len of input strings


    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        map = collections.defaultdict(list)
        for string in strs:
            key = "".join(sorted(string))
            map[key].append(string)
        return map.values()

#time complexity(O(m*n*logn) , m - len of input , n- average len of input strings

    def groupAnagrams3(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
    
#time complexity(O(m*n*26)) , m - len of input , n- average len of input strings

if __name__ == "__main__":
    solution = Solution()
    anagrams = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(anagrams)