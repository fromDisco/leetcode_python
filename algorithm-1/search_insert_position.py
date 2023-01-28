# https://leetcode.com/problems/search-insert-position/description
# Given a sorted array of distinct integers and a target value,
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
############
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
############
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
############
# Input: nums = [1,3,5,6], target = 7
# Output: 4

# Constraints:
##############
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        list_end = len(nums) - 1
        list_start = 0
        found = False

        # these checks in the beginning make sure,
        # that the loop isn't startet if the condition is met.
        # Could a real long list and why loop, when the answer is simple?
        # check if target has to be added at the very beginning
        if target <= nums[0]:
            return 0
        # or at the very end
        elif target > nums[-1]:
            return list_end + 1
        # or is it equal to the last element
        elif target == nums[-1]:
            return list_end

        # if first condiditions are not met
        # start binary search
        while not found:
            # calculate midpoint of actual part of the list
            mid = (list_start + list_end) // 2

            if target == nums[mid]:
                index = mid
                break
            # if target is bigger than mid, than we don't need
            # numbers smaller than mid
            elif target > nums[mid]:
                # but if target is also smaller than the next list element
                # it must be in the middel of both
                if target < nums[mid + 1] or target == nums[mid + 1]:
                    index = mid + 1
                    break
                # return new mid
                list_start = mid + 1
            # if target is smaller than mid, than we don't need
            # numbers bigger than mid
            elif target < nums[mid]:
                # if target is also bigger than previous list element,
                # it must be between mid and the previous element
                if target == nums[mid - 1]:
                    index = mid - 1
                    break
                if target > nums[mid - 1]:
                    index = mid
                    break
                # return new mid
                list_end = mid - 1

        return index

    # better, faster solution
    def searchInsert2(self, nums: List[int], target: int) -> int:
        # after speedtest this version is the winner in performance
        # it is at least 5 to 10 times faster, than the extensive testing.
        list_start = 0
        list_end = len(nums) - 1

        # start binary search
        # run until mid is a match,
        # or list_start is bigger then list_end
        while list_start <= list_end:
            mid = (list_start + list_end) // 2

            if target == nums[mid]:
                return mid
            # if target is bigger than mid, than we don't need
            # numbers smaller than mid
            elif target > nums[mid]:
                list_start = mid + 1
            # if target is smaller than mid, than we don't need
            # numbers bigger than mid
            else:
                list_end = mid - 1

        return list_start


if __name__ == "__main__":
    import time

    nums = [i for i in range(1000000)]

    # instatiate Solution Class
    solution = Solution()

    # long code execution
    first_start = time.time()
    print(solution.searchInsert(nums, 545))  # -> 2
    first_end = time.time()
    print("first")
    first_result = first_end - first_start
    print(first_result)

    # short version. less checking
    now = time.time()
    print(solution.searchInsert2(nums, 545))  # -> 2
    then = time.time()
    print("Second time")
    result = then - now
    print(result)

    print("\nShort Version x times faster than long Version:")
    print(first_result / result)

    # print(solution.searchInsert2([1,3,5,6,7], 5)) # -> 2
    # print(solution.searchInsert2([1,3,5,6,7], 2)) # -> 1
    # print(solution.searchInsert2([1,3,5,6,7], 0)) # -> 0
    # print(solution.searchInsert2([1,3,5,6,7], 7)) # -> 4
    # print(solution.searchInsert2([1,3,5,6,7], 8)) # -> 5
    # print(solution.searchInsert2([1,3,4,5,6,7], 3)) # -> 1
