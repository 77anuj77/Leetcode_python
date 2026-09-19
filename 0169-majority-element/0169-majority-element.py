class Solution(object):
    def majorityElement(self, nums):
        
        n=len(nums)
        d={}

        for i in nums:
            if i in d:
                d[i]+=1

            else:
                d[i]=1
        maj=0
        for k,v in d.items():
            if v>(n/2):
                maj=k
        return maj