from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        output=0
        for i in nums:
            a=str(i)
            if len(a)>=2 and len(a)%2==0:
                output+=1
        return output

if __name__=="__main__":
    sol=Solution()
    print("Input address")
    arr = list(map(int, input().split()))
    res=sol.findNumbers(arr)
    print("Resut: ")
    print(res)