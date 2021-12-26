# Designer Door Mat

n,m=map(int,input().split(" "))
k=n-2
l=1
for i in range(0,n):
  
    if i< int(n/2):
        print(int((m-l*3)/2)*"-"+l*".|."+int((m-l*3)/2)*"-")
        l=l+2
        continue
        
    if i==int(n/2):    
        print(int((m-7)/2)*"-"+"WELCOME"+int((m-7)/2)*"-")
        continue
        
    if i> int(n/2):
        print(int((m-k*3)/2)*"-"+k*".|."+int((m-k*3)/2)*"-")
        k=k-2
        continue