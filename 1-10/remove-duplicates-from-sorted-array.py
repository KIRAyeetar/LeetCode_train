# encoding:utf-8


def run():
    print(removeDuplicates([1,2,2,3,4,4,4]))


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    for i in range(len(nums) - 1):
        j = i-count
        if nums[j] == nums[j+1]:
            del nums[j]
            count += 1
    return len(nums)


if __name__ == '__main__':
    run()