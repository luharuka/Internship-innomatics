

class Solution:
    def defangIPaddr(self, address: str) -> str:
        ret=""
        for i in address:
            if i=='.':
                ret=ret+"[.]"
            else:
                ret=ret+i
        return ret

if __name__=="__main__":
    sol=Solution()
    print("Input address")
    arr=input()
    res=sol.defangIPaddr(arr)
    print("Resut: ")
    print(res)
        
