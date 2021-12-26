# Kids With the Greatest Number of Candies
#There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
#Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
#Note that multiple kids can have the greatest number of candies.
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out =[]
        present_max=max(candies)
        for i in range(len(candies)):
            if extraCandies+candies[i]>=present_max:
                out.append(True)
            else:
                out.append(False)
        return out
if __name__=="__main__":
    sol=Solution()
    print("Input Candies array")
    arr=input().split(" ")
    arr=list(map(int,arr))
    n=int(input("Input extracandies"))
    res=sol.kidsWithCandies(arr,n)
    print("Resut: ")
    print(res)