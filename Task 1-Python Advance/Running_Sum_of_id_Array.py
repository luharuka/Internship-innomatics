# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i])

from typing import List


class Solution:
    def runningSum(self, nums:List[int])->List[int]:
        out=[]
        result=0
        for i in range(len(nums)):
            result=result+nums[i]
            out.append(result)
        return out

if __name__=="__main__":
    sol=Solution()
    print("Input array")
    arr=input().split(" ")
    arr=list(map(int,arr))
    res=sol.runningSum(arr)
    print("Resut: ")
    print(res)

            
            