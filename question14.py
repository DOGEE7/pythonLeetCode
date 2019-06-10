# 14. 最长公共前缀
'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
'''


class Solution:
    def longestCommonPrefix(self, strs):
        '''
        :param strs: list[str]
        :return: str
        '''
        # if len(strs)==0:return ''
        # if len(strs)==1:return strs[0]
        # minlen_s=len(strs[0])
        # record=0
        # flag=True
        # length=len(strs)
        # for i in range(length):
        #     minlen_s=min(minlen_s,len(strs[i]))
        #     if strs[i]=='':strs.remove(strs[i])
        #     # print(strs[i])
        # for i in range(minlen_s):   #选定第i个字母
        #     if flag:
        #         record = i  # 记录i值
        #         for j in range(len(strs) - 1):  # 字符串之间的比较
        #             if strs[j][i] != strs[j + 1][i]:
        #                 flag=False
        #                 # record+=1
        #                 break
        # if flag:record+=1
        # return strs[0][0:record]
        length = len(strs)
        if length == 0:
            return ''
        elif length == 1:
            return strs[0]
        cmp = strs[0]
        if len(cmp) == 0: return ''
        for i in range(1, length):
            minlen_s = min(len(cmp), len(strs[i]))
            if minlen_s == 0: return ''
            for j in range(minlen_s):
                if cmp[j] != strs[i][j]:
                    break
            cmp = cmp[0:j+1]

        if len(cmp) != 1: cmp = cmp[0:j+1]
        return cmp


if __name__ == '__main__':
    solution = Solution()
    strs = ["aaa", "aa",'aaa']
    re = solution.longestCommonPrefix(strs)
    print(re)
