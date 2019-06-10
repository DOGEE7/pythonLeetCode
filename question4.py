"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0
示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 暴力破解：无关时间复杂度
        # list1=list(nums1)
        # list2=list(nums2)
        # list=list1+list2
        # #for i in list2:
        # #    list1.append(i)
        # list1.sort()    #时间复杂度：O(nlogn)
        # length=len(list1)
        # if length%2==0:
        #     index1=length//2-1
        #     index2=index1+1
        #     median_num=float((list1[index1]+list1[index2])/2)
        # else:
        #     index=length//2
        #     median_num=float(list1[index])
        # return median_num

    def median(self,A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2  #i是小数组的中位数索引
            j = half_len - i    #j为大数组索引号
            if i < m and B[j - 1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0




if __name__=='__main__':
    solution=Solution()
    nums1=[1,3]
    nums2=[2,4]
    median_num=solution.findMedianSortedArrays(nums1,nums2)
    print(median_num)