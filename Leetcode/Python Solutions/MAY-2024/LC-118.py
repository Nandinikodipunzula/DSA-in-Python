from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        triangle.append([1])

        for i in range(1, numRows):
            row = []
            prevRow = triangle[len(triangle)-1]
            row.append(1)
            for j in range(1,len(prevRow)):
                row.append(prevRow[j-1]+prevRow[j])
            row.append(1)
            triangle.append(row)
        return triangle
            
#time complexity(O(n2)) n = numRows

if __name__ == "__main__":
    solution = Solution()
    pascalTriangle = solution.generate(7)
    print(pascalTriangle)


        