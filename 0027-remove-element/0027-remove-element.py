class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # The pointer for keeping track of the current position to place elements not equal to val.
    
        for i in range(len(nums)):
          if nums[i] != val:
             nums[k] = nums[i]
             k += 1
    
        return k



print("All assertions passed.")





