class Solution(object):
    def solution_one(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return nums
        
        i,j = 0,1
        max_i, max_j, MAX = i,j, nums[i]
        
        while j < len(nums):

            if nums[j] > max( sum(nums[i:j]) , sum(nums[i:j+1]) ):
                i = j
                j = i+1
            if sum(nums[i:j+1]) > max(nums[j], sum(nums[i:j]) ):
                j = j+1
            if sum(nums[i:j]) > max(nums[j], sum(nums[i:j+1])):
                if sum(nums[i:j]) > max( MAX , sum(nums[max_i:j]) ):
                    max_i = i
                    max_j = j
                if sum(nums[max_i:j])> max( MAX , sum(nums[i:j]) ):
                    max_j = j
                
                MAX = sum(nums[max_i:max_j])
                
                i= j
                j = i+1
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return nums[0]
        current_maximum = global_maximum = nums[0]
        for i in range(len(nums)):
            if(i!=0):
                current_maximum = max(nums[i],current_maximum+nums[i])
                if(current_maximum>global_maximum):
                    global_maximum = current_maximum
        return global_maximum

#q = [-2,1]
q = [-2,1,-3,4,-1,2,1,-5,4]
answer = Solution.maxSubArray(Solution,q)
print(answer)