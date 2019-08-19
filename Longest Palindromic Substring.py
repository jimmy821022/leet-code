#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

#Example 1:
#Input: "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.

#Example 2:
#Input: "cbbd"
#Output: "bb"

#global pal_sub
class Solution:
    def longestPalindrome(self, s: str) -> str:
        global pal_sub
        pal_sub = ""
        pal_flag = 0
        #if 1 == len(s):
            #return s
        for i in range(2, len(s)+1):
            for j in range(len(s)-i+1):
                flag = 0
                dict = ""
                for k in range(j, j+i):
                    #print(k)
                    dict = dict+s[k]
                for l in range(len(dict)//2):
                    if dict[l] == dict[len(dict)-l-1]:
                        flag = 1
                    elif dict[l] != dict[len(dict)-l-1]:
                        flag = 0
                        #if 2 == len(s):
                            #pal_sub = dict[0]
                        break
                if flag:
                    pal_sub = dict
                    break
                #print(dict)
        if "" == s:
            return s
        elif "" == pal_sub:
            return s[0]
        else:
            return pal_sub
