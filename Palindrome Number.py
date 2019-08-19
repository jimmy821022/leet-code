#Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

#Example 1:
#Input: 121
#Output: true

#Example 2:
#Input: -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

#Example 3:
#Input: 10
#Output: false
#Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        left, right = (len(s)-1)//2, len(s)//2
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right-left == len(s)+1
