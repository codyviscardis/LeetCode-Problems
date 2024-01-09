class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastWord = ""
        result = ""
        for i in range(len(s)):
            
            if s[i] == " ":
                lastWord = ""
            else:
                lastWord += s[i]
                result = lastWord
        return len(result)