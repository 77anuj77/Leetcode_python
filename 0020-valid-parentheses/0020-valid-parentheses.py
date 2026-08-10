class Solution(object):
    def isValid(self, s):
        '''
    for each character:
    if opening bracket:
        push into stack

    else:
        if stack is empty:
            return False

        if top of stack doesn't match:
            return False

        pop from stack

        return stack is empty    
        '''
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