class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[]
        d={}
        for i in nums1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        for j,key in d.items():
            if j in nums2:
                result.append(j)
        return result
            
