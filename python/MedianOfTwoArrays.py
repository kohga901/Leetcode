class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        if (length % 2 == 0 ):
            index_2 = length // 2
            index_1 = index_2 - 1
            median = (nums1[index_1] + nums1[index_2]) / 2.0
        else:
            index = length // 2
            median = nums1[index]
        return median

sol = Solution()
nums_1 = [1,2]
nums_2 = [3,4]
print(sol.findMedianSortedArrays(nums_1, nums_2))