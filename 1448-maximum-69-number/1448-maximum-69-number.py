class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        array = []
        original = [int(d) for d in str(num)]
        num = []
        # print(original)
    
        for i in range(len(original)):
            num[:] = original
            if num[i] == 6:
                num[i] = 9

            flipped_num = int(''.join(str(d) for d in num))
            array.append(flipped_num)

        # print(array)
        return max(array)