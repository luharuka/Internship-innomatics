
# XOR Operation in an Array



class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        output = 0
        for i in range(n):
            output ^= start + 2 * i
        return output



if __name__=="__main__":
    sol=Solution()
    print("Input n")
    n=int(input())
    start=int(input("Enter starting element"))
    res=sol.xorOperation(n,start)
    print("Resut: ")
    print(res)
        