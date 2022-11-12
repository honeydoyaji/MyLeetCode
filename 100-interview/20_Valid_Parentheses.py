# References : https://leetcode.com/problems/valid-parentheses/solutions/316753/python-4ms-faster-then-100-with-explanation/
# Runtime 33 ms Memory 13.8 MB

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Understand the stack (pop -> last one)
        stack = []
        pdict = {'(':')', '{': '}','[':']'}

        for char in s:
            if char in pdict:
                stack.append(char) # { ( [
            # use pop()
            elif len(stack) == 0 or pdict[stack.pop()] != char:
                return False
        # return true or false by using this line
        return len(stack) == 0
