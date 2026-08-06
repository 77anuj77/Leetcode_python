class Solution(object):
'''
Create empty dictionary

For every number:
    complement = target - current_number

    If complement already exists:
        return both indices

    Otherwise:
        store current_number and its index
'''
    #using the hash map logic for better time complexity
    def twoSum(self, nums, target):

        history={}
        for i, num in enumerate(nums):
            diff = target - nums[i]
            if diff in history:
                return [i,history[diff]]
            else :
                history[num]=i
        return []
