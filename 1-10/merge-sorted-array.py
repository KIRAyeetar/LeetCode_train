# encoding:utf-8


def run():
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    print(nums1)


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    if n == 0:
        return
    if m == 0:
        nums1[:] = nums2
        return
    nums1_tmp = nums1[:m]
    nums1_tmp.append(max(nums1_tmp[-1], nums2[-1]) + 1)
    nums2.append(max(nums1_tmp[-1], nums2[-1]) + 1)

    for i in range(m + n):
        if nums2[0] < nums1_tmp[0]:
            nums1[i] = nums2.pop(0)
        else:
            nums1[i] = nums1_tmp.pop(0)

    # the best solution
    # nums1[m:] = nums2
    # nums1.sort()


if __name__ == '__main__':
    run()