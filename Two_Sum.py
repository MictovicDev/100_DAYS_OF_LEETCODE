from typing import List
"""
Given an array of integers return indices of the two numbers such that they addup to a specific target
You may assume that each input would have exactly one solution and you may not use the same element twice
"""


"""
proposed algorithm to follow
using the sliding window aalgorithm
have a pointer which is the initial element at index zero
get it's compliment from the target number, then that's the element you should look for in the list

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #val : index

        for i, x in enumerate(nums):
            diff = target - x
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[x] = i
        return



        

sol = Solution()

print(sol.twoSum([3,3], 6))