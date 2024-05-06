from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        largestSoFar = -1 
        for i in reversed(range(length)):
            if arr[i] < largestSoFar:
                arr[i] = largestSoFar
            else:
                arr[i],largestSoFar = largestSoFar,arr[i]
        return arr
    

if __name__ == "__main__":
    solution = Solution()
    arr = [17,18,5,4,6,1]
    output = solution.replaceElements(arr)
    print("Output:", output)


# method 2

# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         length = len(arr)
#         largestSoFar = -1 
#         for i in reversed(range(length)):
#             cur = arr[i]
#             arr[i] = largestSoFar;
#             largestSoFar = max(largestSoFar, cur)
#         return arr
