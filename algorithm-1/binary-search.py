"""
# Link
######
https://leetcode.com/problems/binary-search/?envType=study-plan&id=algorithm-i

Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

# Example 1:
############
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

# Example 2:
############
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

# Constraints:
##############
    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.
"""
from typing import List

# class based solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # start and end are changed on every call.
        # either start = start + 1
        # or end = end - 1
        # so, if no matches, at some point start > end
        # then target is not found
        # if target is found return index in nums of target
        start = 0
        end = len(nums) - 1

        while True:
            # base case
            if start > end:
                return -1

            # get the middle of actual start and end
            mid_index = (start + end) // 2

            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] > target:
                # search only in left part of list, excluding mid_index
                end = mid_index - 1
            elif nums[mid_index] < target:
                # search only in right part of list, excluding mid_index
                start = mid_index + 1


# recursive function based solution
def binary_search(num_list, start, end, target) -> int:
    """
    start and end are changed on every call.
    either start = start + 1
    or end = end - 1
    so, if no matches, at some point start > end
    then target is not found

    if target is found return index in num_list of target
    """
    # base case
    if start > end:
        return -1

    # get the middle of actual start and end
    midIndex = (start + end) // 2

    if num_list[midIndex] == target:
        return midIndex
    elif num_list[midIndex] > target:
        # return the left part of the list, exluding midIndex
        return binary_search(num_list, start, midIndex - 1, target)
    elif num_list[midIndex] < target:
        # return only right part of the list, excluding midIndex
        return binary_search(num_list, midIndex + 1, end, target)


if __name__ == "__main__":
    num_list = [-1, 0, 3, 5, 9, 12]
    target = 3
    solution = Solution()
    print(solution.search(num_list, target))
    # start = 0
    # end = len(num_list) - 1
    # print(binary_search(num_list, start, end, target))
