"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        left = 0
        flag = 0
        #if [] == strs: return ""
        if not strs: return ""
        if 1 == len(strs): return strs[0]
        length_min = min([len(i) for i in strs])
        while left < length_min:
            for i in range(len(strs)-1):
                if strs[i][left] != strs[i+1][left]:
                    flag = 1
                    break
                elif len(strs)-2 == i:
                    s += strs[i][left]
            if flag:
                break
            left += 1
        return s
