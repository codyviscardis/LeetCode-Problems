class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        else:
            s = s.lower()

            s = ''.join(ch for ch in s if ch.isalnum())

            print(s)
        
            for i in range(len(s)/2):
                if s[i] != s[len(s)-1-i]:
                    return False
            return True