
from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        repeat = {}
        num = 0
        for v in nums:
            
            if v in repeat:
                if repeat[v] == 1:
                    num += 1
                else:
                    num += repeat[v]
                repeat[v] += 1
            else:
                repeat[v] = 1
        return num
    
if __name__=="__main__":
    sol=Solution()
    print("Input address")
    arr = list(map(int, input().split()))
    res=sol.numIdenticalPairs(arr)
    print("Resut: ")
    print(res)

