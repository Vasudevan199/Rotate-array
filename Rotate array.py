class Solution:
    @staticmethod
    def rotate(nums, k):
        n = len(nums)
        k %= n 
        nums[:] = nums[-k:] + nums[:-k]

nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
Solution.rotate(nums1, k1)
print(nums1) 

nums2 = [-1, -100, 3, 99]
k2 = 2
Solution.rotate(nums2, k2)
print(nums2) 
