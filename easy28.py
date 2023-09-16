"""
28. Find the Index of the First occurrence in a String
Easy
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Constraints:
  1 <= haystack.length, needle.length <= 104
  haystack and needle consist of only lowercase English characters.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # trivial cases
        if len(needle) > len(haystack):
            return -1
        if needle == haystack:
            return 0
        
        # check each valid starting point
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

        # not found anywhere
        return -1