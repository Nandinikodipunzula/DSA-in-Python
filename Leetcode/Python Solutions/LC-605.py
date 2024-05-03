from typing import List

class Solution:
    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        empty_plots = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                check_left = (i == 0) or flowerbed[i-1] ==0
                check_right = (i == len(flowerbed)-1) or flowerbed[i+1] ==0
                if check_left and check_right:
                    flowerbed[i] =1
                    empty_plots+=1
        return empty_plots>=n 
    
if __name__ == "__main__":
    solution = Solution()    
    flowerbed = [0,0,1,0,1]  
    n=1
    print(solution.canPlaceFlowers(flowerbed,n)) 

#Time Complexity : O(n) 
        