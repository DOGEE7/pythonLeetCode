# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
# 请你实现这个将字符串进行指定行数变换的函数：
# string convert(string s, int numRows);
# 示例 1:
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
# 示例 2:
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G

class Solution:
    # def convert(self, s, numRows):
    #     '''
    #     :param s: str
    #     :param numRows: int
    #     :return: str
    #     '''
    #
    #     len_s = len(s)
    #     if len_s<2:return  s
    #     rows = min(len_s, numRows)
    #     list1 = [['' for i in range(len_s)] for j in range(numRows)]
    #     n=2*numRows-2
    #     for i in range(rows):
    #         j = 0
    #         flag = 0
    #         loc = i
    #         list1[i][0] = s[loc]
    #         while loc < len_s:
    #             if i == 0 or i == numRows - 1:
    #                 j = j + (numRows - 1)
    #                 loc = loc + n
    #             else:
    #                 if flag == 0:
    #                     j = j + (numRows - 1 - i)
    #                     if i>=numRows//2:loc=loc+(numRows-i)
    #                     else:loc = loc + n-(i+1)
    #                 else:
    #                     j = j + i
    #                     if i>=numRows//2:loc=loc+(n-numRows+i)
    #                     else:loc = loc + i+1
    #                 flag=~flag
    #             if loc<len_s:list1[i][j] = s[loc]
    #     res = ''
    #     for i in range(rows):
    #         res = res + ''.join(list1[i])
    #     return res


    def convert(self, s, numRows):
        if numRows==1:return  s
        len_s=len(s)
        tmp=[['' for i in range(len_s) ]for j in range(numRows)]
        down=True
        loc=0   #s[loc]
        i,j = 0,0
        # while loc<len_s:
        #     down=not down
        #     # if down:i=0
        #     # else:i=len_s-1
        while loc<len_s:
            if down==True:
                tmp[i][j]=s[loc]
                if i+1<numRows:i=i+1
                else:down=not down
            else:
                if i - 1 > -1: i = i - 1
                else:
                    down = not down
                    if i+1<numRows:
                        i=i+1
                        continue

                j = j + 1
                tmp[i][j]=s[loc]


            loc=loc+1
        # i=numRows-2
        res=''
        for i in range(numRows):
            res=res+''.join(tmp[i])
        return res




if __name__ == '__main__':
    solution = Solution()
    s = "ABC"
    numRows = 1
    print(solution.convert(s, numRows))
