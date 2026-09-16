class Solution(object):
    def longestCommonPrefix(self, strs):

        if not strs:
            return ""

        prefix= strs[0]
        for s in strs[1:]:
            limit= min(len(s), len(prefix))
            for i in range(limit):
                if prefix[i] != s[i]:
                    prefix=prefix[:i]
                    break
                
            else:
                prefix= prefix[:limit]
        
            if not prefix:
                return ""

        return prefix        