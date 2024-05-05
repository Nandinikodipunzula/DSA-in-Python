class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        size = m+n
        r1=m-1
        r2=n-1

        for w in reversed(range(size)):
            if r1 >= 0 and r2 >=0 :
                if  nums1[r1] > nums2[r2]:
                    nums1[w] = nums1[r1]
                    r1-=1
                elif nums1[r1] <= nums2[r2]:
                    nums1[w] = nums2[r2]
                    r2-=1
            elif r1>=0:
                nums1[w] = nums1[r1]
                r1-=1
            elif r2>=0:
                nums1[w] = nums2[r2]
                r2-=1


            
            