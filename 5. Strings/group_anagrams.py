class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mydict = collections.defaultdict(list)
        for str in strs:
            sortedStr = "".join(sorted(str))
            mydict[sortedStr].append(str)
            
        return mydict.values()
