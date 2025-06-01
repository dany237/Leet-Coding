'''
Leet code contain

'''
class LeetCode: 
    #1. Two sum
    '''
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''
    def twoSum(self, nums, target):
        dict = {} # for keeping value and index
        for i, num in enumerate(nums): # i index of the current number, num value at that index
            c = target - num # compute the number we need to find
            if c in dict : # if this complement is found in dict, then the solution if found
                return [dict[c], i]
            dict[num] = i

# Media Sorted Arrays

    def findMedianSortedArrays(self, nums1, nums2):
        # make sur that nums1 will be the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        len_1, len_2 = len(nums1), len(nums2)
        l, h = 0, len_1
        
        while l <= h:
            i = (l + h) // 2 # partition in nums1
            j = (len_1 + len_2 + 1) // 2 - i #partition in nums2

            nums1left = nums1[i - 1] if i > 0 else float('-inf')
            nums1right = nums1[i] if i < len_1 else float('inf')

            nums2left = nums2[j - 1] if j > 0 else float('-inf')
            nums2right = nums2[j] if j < len_2 else float('inf')

            if nums1left <= nums2right and nums2left <= nums1right :
                if (len_1 + len_2) % 2 == 1:
                    return max(nums1left, nums2left)
                else:
                    return(max(nums1left, nums2left) + min(nums1right, nums2right)) / 2
            elif nums1left > nums2right:
                h = i - 1
            else:
                l = i + 1