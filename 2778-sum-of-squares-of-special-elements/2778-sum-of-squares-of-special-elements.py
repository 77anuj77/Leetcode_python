class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        index=[i for i in range(1, len(nums)+1) if n%i==0]
        sum=0
        for j in index:
            sum+=nums[j-1]*nums[j-1]
        return sum
