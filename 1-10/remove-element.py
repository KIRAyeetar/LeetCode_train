# encoding:utf-8


def run():
    print(removeElement([1,2,2,3,4,4,4], 4))


def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    count = 0
    for i in range(len(nums)):
        j = i-count
        if nums[j] == val:
            del nums[j]
            count += 1
    return nums


if __name__ == '__main__':
    run()