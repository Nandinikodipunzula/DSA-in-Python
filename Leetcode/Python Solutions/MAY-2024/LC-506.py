from typing import List
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        indexMap={}
        ans=[0]*len(score)
        places=["Gold Medal","Silver Medal","Bronze Medal"]
        for i, num in enumerate(score):
            indexMap[num]=i
        score.sort()
        k=0
        for i in reversed(range(len(score))):
            num = score[i]
            index = indexMap[num]
            if i >= len(score)-3:
                ans[index] = str(places[k])
                k+=1
            else:
                ans[index] = str(k+1)
                k+=1
        return ans
if __name__ == "__main__":
    solution = Solution()
    score = [10,3,8,9,4] 
    print(solution.findRelativeRanks(score))

    