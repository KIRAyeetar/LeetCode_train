class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        hash_table_2 = {}
        for i in range(len(nums)):
            if hash_table.has_key(nums[i]):
                hash_table_2[nums[i]] = i
            else:
                hash_table[nums[i]] = i

            result = target-nums[i]
            if hash_table_2.has_key(result):
                return [i, hash_table[result]]
            if hash_table.has_key(result):
                if hash_table[result]!=i:
                    return [i, hash_table[result]]
        return [0, 0]