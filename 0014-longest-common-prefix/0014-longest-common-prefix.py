class Solution(object):
    def longestCommonPrefix(self, strs):
       if not strs:
        return ""  # Return an empty string if the list is empty
    
       prefix = strs[0]  # Start with the first string as the initial prefix candidate
    
       for string in strs[1:]:
         while string.find(prefix) != 0:
            prefix = prefix[:-1]  # Remove the last character from the prefix
            if not prefix:
                return ""  # If the prefix becomes empty, there's no common prefix
    
       return prefix