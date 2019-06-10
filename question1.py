# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
# 示例:
# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

class Solution:
    # def twoSum(self, nums, target) :
    #     if not nums:
    #         return None
    #     i=0
    #     while i<len(nums):
    #        j=i+1
    #        while j<len(nums)-1:
    #            if nums[i]+nums[j]==target:
    #                return [i,j]
    #     return None

    def twoSum(self,nums,target):
        """
        :param nums: list[int]
        :param target:int
        :return: list[int]
        """
        hashmap={}
        for i,element in enumerate(nums):
            tmp=target-element
            if tmp not in hashmap:
                hashmap[element]=i  #key:element value:index
            else:
                return [hashmap[tmp],i]
        return None


if __name__=='__main__':
    solution=Solution()
    nums=[2,7,11,15]
    target=13
    print(solution.twoSum(nums,target))

