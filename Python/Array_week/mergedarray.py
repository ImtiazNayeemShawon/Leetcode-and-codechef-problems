class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        if n % 2 == 0:
            median = (nums1[n//2] + nums1[n//2 - 1]) / 2.0
        else:
            median = nums1[n//2]
        return median

print(Solution().findMedianSortedArrays([1, 2], [3,4]))