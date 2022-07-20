class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = sorted(nums1 + nums2)
        if len(l) % 2 == 0:
            return ((l[int(len(l) / 2)-1] + l[int(len(l) / 2)]) / 2)
        return l[int((len(l) - 1) / 2)]
