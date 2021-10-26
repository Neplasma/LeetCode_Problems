# leetCode problem Two Sum
"""Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]

Input: nums = [-1, -2, -3, -4, -5], target = -8
Output: [2,4]

Input: nums = [0,4,3,0], target = 0
Output: [0,3]"""

inputlist = [0, 4, 3, 0]
targetnum = 0


def twoSum(nums, target):
    for i in range(len(nums)):
        if (target >= 0 and nums[i] <= target) or (target < 0 and nums[i] >= target):
            num1 = nums[i]
            idx1 = i
            nums[i] = 'nan'  # avoid duplication
            num2 = target - num1
            if num2 in nums:
                outputlist = [idx1, nums.index(num2)]
                print(outputlist)
                break


twoSum(inputlist, targetnum)
