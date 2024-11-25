class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        k= 0
        for i in nums:
            if i not in s:
                s.add(i)
                nums[k] = i
                k+=1
                
        return k