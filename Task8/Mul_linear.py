# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
m,n=list(map(int,input().split()))
x=np.ones((n,m+1))
y=np.zeros((n,1))
for i in range(n):
    o=np.array(list(map(float,input().split())))
    for j in range(m):
        x[i,j+1]=o[j]
    y[i,0]=o[m]
q=int(input())
x_test=np.ones((q,m+1))
for i in range(q):
    test=np.array(list(map(float,input().split())))
    for j in range(m):
        x_test[i,j+1]=test[j]

xtx=(x.T).dot(x)
xtx_inv=np.linalg.inv(xtx)
xtx_inv_xt=xtx_inv.dot(x.T)
b=xtx_inv_xt.dot(y)

for k in range(q):
    print(float(x_test[k].dot(b)))