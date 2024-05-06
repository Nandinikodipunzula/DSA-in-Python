class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        greaterElementDict = {}
        greatestSoFar = -1
        greaterElementDict[nums2[-1]] = greatestSoFar

        for i in range(len(nums2)-2,-1,-1):
            if nums2[i+1] > nums2[i]:
                greaterElementDict[nums2[i]]=nums2[i+1]
                greatestSoFar = nums2[i+1]
            else:
                temp = nums2[i+1]
                while temp != -1 and nums2[i] >= temp:
                    temp = greaterElementDict[temp]
                greaterElementDict[nums2[i]] = temp


        for i,num in enumerate(nums1):
            nums1[i] = greaterElementDict[num]
        return nums1

