class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        pairs={
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        
        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])

            else :
                if not stack:
                    return False
                
                if stack[-1] != pairs[s[i]]:
                    return False

                stack.pop()

        return len(stack) == 0