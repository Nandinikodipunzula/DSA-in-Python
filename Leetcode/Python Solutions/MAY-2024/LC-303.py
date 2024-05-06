class NumArray:
    def __init__(self, nums: List[int]):
        numsSum=0
        self.prefixSum=[]
        for num in nums:
            numsSum+=num
            self.prefixSum.append(numsSum)
        print(self.prefixSum)
    
    def sumRange(self, left: int, right: int) -> int:
        if left > 0 :
            return self.prefixSum[right]-self.prefixSum[left-1]
        else:
            return self.prefixSum[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)