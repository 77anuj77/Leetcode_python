class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = w = 0
        wasRight = False
        for ch in s:
            if ch == ')':
                if wasRight:
                    if w:
                        w -= 1
                    else:
                        a += 1
                    wasRight = False
                else:
                    wasRight = True
            else:
                if wasRight:
                    a += 1
                    if w:
                        w -= 1
                    else:
                        a += 1
                    wasRight = False
                w += 1
        
        if wasRight:
            a += 1
            if w:
                w -= 1
            else:
                a += 1
        
        return a + 2*w