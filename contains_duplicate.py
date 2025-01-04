"""
Given an integer array nums, return true if any value appears at 
least twice in the array, and return false if every element is distinct


Brute force solution has a time complexity of O(n2) and a space complexity of O(1)

sorting takes a time complexity of O(nlogn) and a space complexity of o(1)

A hashset allows us to instert elements in to the hashset in 0(1)
"""



set = {}
nums = [1,2,3,1]


print(dir(set))
for i in nums:
    pass