# encoding:utf-8


def run():
    print(searchRange([1,2,2,3,4,4,4], 4))


def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    flag = 0
    _flag = 0
    forward_num = -1
    backword_num = -1
    for i in range(len(nums)):
        if flag*_flag == 1:
            break
        if flag == 0:
            if nums[i] == target:
                forward_num = i
                flag = 1
        if _flag == 0:
            j = -i-1
            if nums[j] == target:
                backword_num = len(nums)+j
                _flag = 1
    return [forward_num, backword_num]


if __name__ == '__main__':
    run()
