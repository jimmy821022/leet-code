"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if 1 == len(s)%2:return False
        par_left = {"(":0, "[":1, "{":2}
        par_right = {")":0, "]":1, "}":2}
        par_stored = ""
        left = 0
        for i in s:
            if left < 0: return False
            if i in par_left:
                par_stored += i
                left += 1
            elif i in par_right:
                if 0 == left: return False
                if par_left[par_stored[left-1]] != par_right[i]: #配對失敗
                    return False
                else:   #成功配對
                    par_stored = par_stored[:len(par_stored)-1] #pop the last element in par_stored
                    left -= 1
        return True if 0 == left else False
