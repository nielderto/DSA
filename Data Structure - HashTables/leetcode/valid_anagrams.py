'''
49. Group Anagrams (https://leetcode.com/problems/group-anagrams/description/)
Given an array of strings strs, group the 
anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
'''

#O(m * n * log(n))

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        result = []

        for s in strs:
            sorted_strs = tuple(sorted(s))
            anagrams[sorted_strs].append(s)

        for values in anagrams.values():
            result.append(values)

        return result
    
    
s = Solution()
print(s.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(s.groupAnagrams(["x"]))
