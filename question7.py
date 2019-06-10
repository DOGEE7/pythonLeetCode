# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 示例 1:
#
# 输入: 123
# 输出: 321
#  示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21
class Solution:
    def reverse(self, x) :
        '''
        :param x: int
        :return: int
        '''
        if not x:return x
        s=str(x)
        n=len(s)-1
        nag_flag=False
        re=0
        if x<0:
            nag_flag=True
            n=n-1
            x=-x
        for i in range(n+1):
            tmp = x % 10
            x=x//10
            re=re+tmp*(10**n)
            n=n-1
        if re>2**31-1 or re<-2**31:return 0
        if nag_flag==True:return -re
        return re

if __name__=='__main__':
    solution=Solution()
    x=1534236469
    print(solution.reverse(x))
