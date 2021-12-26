class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count=0
        z= x^y
        a=bin(z)
        for i in a:
            if i=='1':
                count+=1
        return count
        
if __name__=="__main__":
    a=int(input())
    b=int(input())
    sol=Solution()
    print(sol.hammingDistance(a,b))