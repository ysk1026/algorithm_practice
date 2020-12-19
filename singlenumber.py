class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h={}
        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]] = 1
            else:
                h[nums[i]] = 2
        for num, frequency in h.items():
            if frequency==1:
                return num