# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 示例 1：
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
# 输入: "cbbd"
# 输出: "bb"

class Solution:
    #   对字符串进行翻转，再对子串进行回文检验
    # def longestPalindrome(self, s):
    #     if len(s)==0:return s
    #     length_str = len(s)
    #     str_reverse = s[::-1]
    #     sublen = 0
    #     max_sublen = 0
    #     str_new = ''
    #     for i in range(length_str):
    #         if s[i] == str_reverse[i]:
    #             str_new += s[i]
    #             sublen +=1
    #         else:
    #             if sublen < max_sublen:
    #                 max_sublen = sublen
    #                 sublen = 0
    #     if len(str_new)==0:return s[0]
    #     for i in range(max_sublen // 2):
    #         if str_new[i] != str_new[max_sublen - 1 - i]:
    #             return s[0]
    #         else:
    #             continue
    #     return str_new


    #暴力法将选出所有子字符串可能的开始和结束位置，并检验它是不是回文。

    #中心扩展算法
    def longestPalindrome(self, s):
        start=0
        end=0
        max_sublen=0
        for i in range(len(s) - 1):
            len1= self.subLength(s, i, i)
            len2= self.subLength(s, i, i + 1)
            sublen=max(len1,len2)
            if sublen>max_sublen:
                max_sublen=sublen
                start=i-(max_sublen-1)//2
                end=i+max_sublen//2
        return s[start:end + 1]





    def subLength(self,s,left,right):
        while  left>=0 and right<len(s):
            if s[left]==s[right]:
                left-=1
                right+=1
            else:break
        return right-left-1



if __name__ == '__main__':
    solution = Solution()
    str = 'abb'
    str_new = solution.longestPalindrome(str)
    print(str_new)
