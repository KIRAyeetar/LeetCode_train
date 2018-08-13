# encoding:utf-8


def run():
    print(findMedianSortedArrays([1,2], [3,4]))


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    tmp = sorted(nums1+nums2)
    len_tmp = len(tmp)
    if len_tmp%2 == 0:
        add = len_tmp/2
        return (tmp[add] + tmp[add-1])/2.0
    else:
        return tmp[len_tmp/2]


if __name__ == '__main__':
    run()