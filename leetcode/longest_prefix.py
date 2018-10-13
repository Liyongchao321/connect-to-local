class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        j = 0
        end = 0
        l = len(strs)
        while 1:
            i = 0
            if l == 0:
                return ''
            if l == 1:
                return strs[0]
            while i < l - 1:
                if j > min(len(strs[i]),len(strs[i+1]))-1:
                    return strs[i][:j]
                temp = strs[i][j]
                if  temp != strs[i+1][j]:
                    return strs[i][:j]
                    end = 1
                    break
                i = i+1
            if end == 1:
                break
            j = j+1