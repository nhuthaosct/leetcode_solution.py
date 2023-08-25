class Solution(object):
  def removeDuplicates(self, nums):
      if len(nums) == 0:
        return 0
    
    # Initialize two pointers: one to iterate through the array and the other to track the position of unique elements.
      unique_position = 0
    
    # Iterate through the array starting from the second element.
      for i in range(1, len(nums)):
        # If the current element is different from the previous element, increment the unique_position pointer and update the element at that position.
        if nums[i] != nums[unique_position]:
            unique_position += 1
            nums[unique_position] = nums[i]
    
    # The unique_position pointer now points to the last unique element, so the number of unique elements is unique_position + 1.
      return unique_position + 1