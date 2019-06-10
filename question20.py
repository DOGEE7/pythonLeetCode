# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
# 示例 3:
#
# 输入: "(]"
# 输出: false
# 示例 4:
#
# 输入: "([)]"
# 输出: false
# 示例 5:
#
# 输入: "{[]}"
# 输出: true
class Solution:
    def isValid(self, s: str) -> bool:
        # 错误：
        # s=s.strip()
        # length=len(s)
        # s_flag=m_flag=l_flag=0
        # if length%2==1 or s[0]==')' or s[0]==']' or s[0]=='}':return False
        # for i in range(length):
        #     if s[i]=='(':
        #         if s[i+1]!=')' and s[i+1]!=' ':
        #             return False
        #     if s[i]=='[':
        #         if s[i+1]!=']' and s[i+1]!=' ':
        #             return False
        #     if s[i]=='{':
        #         if s[i+1]!='}' and s[i+1]!=' ':
        #             return False
        # return True

        # 栈
        # s = s.strip()
        # len_s = len(s)
        # if len_s % 2 == 1 : return False
        # stack = ['1']
        # for i in range(len_s):
        #     tmp = stack.pop()
        #     if s[i] == ' ':
        #         stack.append(tmp)
        #         continue
        #     else:
        #         if tmp == '(':
        #             if s[i] != ')':
        #                 stack.append(tmp)
        #                 stack.append(s[i])
        #             else:
        #                 continue
        #         elif tmp == '[':
        #             if s[i] != ']':
        #                 stack.append(tmp)
        #                 stack.append(s[i])
        #             else:
        #                 continue
        #         elif tmp == '{':
        #             if s[i] != '}':
        #                 stack.append(tmp)
        #                 stack.append(s[i])
        #             else:
        #                 continue
        #         else:
        #             stack.append(tmp)
        #             stack.append(s[i])
        # if stack.pop() == '1': return True
        # return False

        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:

            if char in mapping:

                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

if __name__ == '__main__':
    solution = Solution()
    s = "([])"
    print(solution.isValid(s))
