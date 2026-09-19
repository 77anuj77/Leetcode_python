class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        stack=[]
        output=[]
        for i in nums:
            if i==0:
                stack.append(i)
            else:
                output.append(i)
        for j in stack:
            output.append(j)
        
        for i in range(len(nums)):
            nums[i]=output[i]