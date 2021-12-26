# Subtract the Product and Sum of Digits of an Integer


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a=str(n)
        su=0
        prod=1
        for i in a:
            prod=prod*int(i)
            su=su+int(i)
        return prod-su


if __name__=="__main__":
    sol=Solution()
    print("Input number")
    arr=int(input())
    res=sol.subtractProductAndSum(arr)
    print("Resut: ")
    print(res)
        