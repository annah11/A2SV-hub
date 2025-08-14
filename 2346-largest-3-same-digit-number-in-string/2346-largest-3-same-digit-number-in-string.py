class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        ans = ""
        for i in range(2,len(num)):
            if num[i]==num[i-1]==num[i-2]:
                can = num[i-2:i+1]
                ans = max(ans,can)
        return ans
