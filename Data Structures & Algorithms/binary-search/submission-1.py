class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)
        mid = (right-left) // 2

        while (left != right):
            if (nums[mid] == target):
                return mid
            if nums[mid] > target:
                right = mid
                mid = left + (right-left) // 2
            if nums[mid] < target:
                left = mid+1
                mid = left + (right-left) // 2
        return -1
            

        