# leetCode problem 009 Palindrome Number
"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.
"""
def isPalindrome(self, x: int) -> bool:
        x_str = str(x)       
        for i in range(len(x_str)):
            if x_str[i] == x_str[-1-i]:
                pass
            else:
                return False
        return True
