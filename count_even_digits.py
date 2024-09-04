class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            num_digits = 0
            while num > 0:
                num = num // 10
                num_digits += 1
            if num_digits % 2 == 0:
                count += 1
        return count
