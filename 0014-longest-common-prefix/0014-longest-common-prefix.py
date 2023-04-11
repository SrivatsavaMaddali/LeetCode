class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        #initialize the longest common prefix as the first string
        prefix = strs[0]
    
        for s in strs[1:]:
            # check if the current prefix is a substring of the next string
            while not s.startswith(prefix):
                 # remove the last character from the prefix and try again
                prefix = prefix[:-1]
                if not prefix:
                     # if the prefix becomes empty, there's no common prefix
                    return ""
    
    # return the longest common prefix
        return prefix