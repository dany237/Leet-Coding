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
    def twoSum(self, num, target):
        dict = {} # for keeping value and index
        for i, num in enumerate(num): # i index of the current number, num value at that index
            complement = target - num # compute the number we need to find
            if complement in dict : # if this complement is found in dict, then the solution if found
                return [dict[complement], i]
            dict[num] = i