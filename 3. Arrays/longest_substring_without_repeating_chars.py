class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        dict = {}
        maxlength = 0
        start = 0
        for i in range(len(s)):
            if s[i] not in dict or dict[s[i]]<start:
                maxlength = max(maxlength, i-start+1)
            else:
                start = dict[s[i]] + 1
            dict[s[i]] = i
                
               
        return maxlength