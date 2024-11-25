class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = []
        i = ""
        for i in nums:
            if i not in new:
                new.append(i)
            continue
        nums[:len(new)] = new
        return len(new)