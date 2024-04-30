class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2*n)
        for i in range(n):
            ans[i]= nums[i]
            ans[n+i]= nums[i]
        return ans
    
    if __name__ == "__main__":
        solution = Solution()
        nums= [1,2,3,4,5,6,7]
        output = solution.getConcatenation(nums)
        print('Concatenated array : ' , output)