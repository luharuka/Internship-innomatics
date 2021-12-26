from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        direc={}
        for i in nums:
            if i not in direc:
                direc[i]=0
            direc[i]+=1
        for i in direc:
            if direc[i]<3:
                return i
        
        

if __name__=="__main__":
    arr=input().split(" ")
    arr=list(map(int,arr))
    sol=Solution()
    print(sol.singleNumber(arr))