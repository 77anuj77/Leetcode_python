class Solution(object):
    def maxAlternatingSum(self, nums):
        squares = sorted(x*x for x in nums)

        n = len(squares)
        mid = n // 2

        return sum(squares[mid:]) - sum(squares[:mid])