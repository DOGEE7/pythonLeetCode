# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 示例 1:
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
class Solution(object):
    '''def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length=len(s)    #length:int
        d=dict(zip(list(range(length)),list(s)))   #d:dict
        max=1   #max:int
        for i in range(length):    #i:int
            j=i+1
            while j<length:
                if d[i]==d[j] and (j-i)>=max:
                    max=j-i
                    break
                j+=1
        return max
    '''

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = ''
        max_sublen = 0
        for i in s:
            if i not in tmp:
                tmp += i
                l = len(tmp)
                if l > max_sublen: max_sublen = l
            else:
                index = tmp.index(i)
                tmp = tmp[(index + 1):] + i

        return max_sublen

    '''神仙算法
    class Solution:
        def lengthOfLongestSubstring(self, s):
            """
            :type s: str
            :rtype: int
            """
            st = {}
            i, ans = 0, 0
            for j in range(len(s)):
                if s[j] in st:
                    i = max(st[s[j]], i)
                ans = max(ans, j - i + 1)
                st[s[j]] = j + 1
            return ans;
    '''


if __name__ == "__main__":
    solution = Solution()
    s = "pwwkew"
    l = solution.lengthOfLongestSubstring(s)
    print(l)
