class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new=[]
        n = set(nums)
        for i in range(1,len(nums)+1):
            if(i not in n):
                new.append(i)
        return new
        
 