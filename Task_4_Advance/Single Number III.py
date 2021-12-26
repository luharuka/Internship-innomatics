# Single Number III


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        dic, res = {}, []
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for k, v in dic.items():
            if v == 1:
                res.append(k)
        return res
    
    def singleNumber(self, nums):
        tmp = 0
        for num in nums:
            tmp ^= num
        i = 0
        while tmp & 1 == 0:
            tmp >>= 1
            i += 1
        tmp = 1 << i
    
        first, second = 0, 0
        for num in nums:
            if num & tmp:
                first ^= num
            else:
                second ^= num
        return [first, second]
        