'''
盛水最多问题：
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。
示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
'''


class Solution:
    def maxArea(self, height):
        '''
        :param height: List[int]
        :return: int
        '''
        # 暴力破解
        # max_area,less_num=0,0
        # length=len(height)
        # if length<2:return 0
        # for i in range(length):
        #     h1 = height[i]
        #     for j in range(i+1,length):
        #         h2=height[j]
        #         less_num=min(h1,h2)
        #         max_area=max(max_area,(j-i)*less_num)
        # return max_area

        # 双指针
        left = 0
        length = len(height)
        right = length - 1
        max_area = 0
        min_height=0
        if length < 2: return 0
        while right >= 1:
            max_area = max(max_area, (right - left) * min(height[right], height[left]))
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return max_area


if __name__ == '__main__':
    solution = Solution()
    height = [1, 1]
    re = solution.maxArea(height)
    print(re)
