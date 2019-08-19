#Given a 32-bit signed integer, reverse digits of an integer.
#Example 1:
#Input: 123
#Output: 321

#Example 2:
#Input: -123
#Output: -321

#Example 3:
#Input: 120
#Output: 21

class Solution:
    def reverse(self, x: int) -> int:
        intMax = 2**31-1
        intMin = -2**31
        s = str(x)
        num = ""
        start = len(s)
        switch = 0
        if 0 != s[start-1]: 
            switch = 1
        while start and s[start-1] != "-":
            if 1 == switch:
                num = num+s[start-1]
            elif 0 == switch:
                if 0 != s[start-1]:
                    num = num+s[start-1]
                    switch = 1
            start -= 1
        if x < 0 and -int(num) > intMin:
            return -int(num)
        elif x < 0 and -int(num) < intMin:
            return 0
        elif x > 0 and int(num) < intMax:
            return int(num)
        elif x >0 and int(num) > intMax:
            return 0
        elif 0 == x:
            return 0
