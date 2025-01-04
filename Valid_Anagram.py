"""
 GIven two strings s and t return true if t is a n anagram of s, and false otherwise
"""


##An anagram means that both words contain the same characters

"""
time complexity = O(S+T)
space complexity = O(S+T)
create a hashmap
loop through both strings
append the character as the key and the number the character appears as the value
after that compare the both hashmaps if they are the saame  theb it is an anagram

"""



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] == countT.get(c, 0):
                return False
        return True
 