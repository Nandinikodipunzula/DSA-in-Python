class Solution:
    def furthestBuilding(self, height: List[int], bricks: int, ladders: int) -> int:
        ladders_allocated =[]
        for i in range(len(height)-1):
            climb =  height[i]- height[i+1]
            if climb < 0 :
                heapq.heappush(ladders_allocated,-climb)
            if len(ladders_allocated) > ladders:
                bricks-=heapq.heappop(ladders_allocated)
            if bricks < 0:
                return i
        return len(height)-1
