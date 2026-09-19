class Solution(object):
    def moveZeroes(self, nums):
        stack = []
        output = []

        for i in nums:
            if i == 0:
                stack.append(i)
            else:
                output.append(i)

        for j in stack:
            output.append(j)

        # copy output back into nums
        for i in range(len(nums)):
            nums[i] = output[i]