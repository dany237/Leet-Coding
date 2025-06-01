from leetcode import LeetCode

if __name__ == "__main__":

    leet_obj = LeetCode()

    num = [2,7,11,15]; target = 9
    print(leet_obj.twoSum(num, target))

    #Median of two sorted list

    nums1, nums2 = [1,2], [3,4]
    print(leet_obj.findMedianSortedArrays(nums1, nums2))