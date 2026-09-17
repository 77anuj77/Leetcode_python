# class Solution(object):
#     def isPalindrome(self, s):
        # left = 0
        # right = len(s) - 1

        # while left < right:

        #     # Skip non-alphanumeric characters
        #     if not s[left].isalnum():
        #         left += 1
        #         continue

        #     if not s[right].isalnum():
        #         right -= 1
        #         continue

        #     # Compare characters
        #     if s[left].lower() != s[right].lower():
        #         return False

        #     left += 1
        #     right -= 1

        # return True

class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        sc=' ,@:.&*#$%"!?_-+=/|{[]}():;><^`\~'
        for i in sc:
            s=s.replace(i,'')
        s=s.replace("'",'')
        if s==s[::-1]:
            return True
        return False