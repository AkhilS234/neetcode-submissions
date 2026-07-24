class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m + n - 1
        onePtr = m - 1
        twoPtr = n - 1

        while (onePtr >= 0 and twoPtr >= 0):

            if (nums1[onePtr] < nums2[twoPtr]):
                nums1[l] = nums2[twoPtr]
                twoPtr -= 1
            else: 
                nums1[l] = nums1[onePtr]
                onePtr -= 1
            l -= 1

        while (twoPtr >= 0):
            nums1[l] = nums2[twoPtr]
            l -= 1
            twoPtr -= 1




             