from typing import List
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        countNeg = 0
        countPos = 0
        countZero = 0

        for num in nums:
            if num < 0:
                countNeg+=1
            elif num > 0:
                countPos+=1
            else:
                countZero+=1
                return 0
        if countNeg % 2 !=0:
            return -1
        return 1
    
if __name__ == "__main__":
    solution = Solution()
    nums = [-1,1,-1,1,-1]
    sign = solution.arraySign(nums)
    print(sign)

    nums = [-1,-2,-3,-4,3,2,1]
    sign = solution.arraySign(nums)
    print(sign)

    nums = [1,5,0,2,-3]
    sign = solution.arraySign(nums)
    print(sign)