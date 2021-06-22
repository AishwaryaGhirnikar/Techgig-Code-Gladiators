def main():

 # Write code here 
    T=int(input())
    for i in range(T):
        L, R = map(int,input().split(" "))
        temp=L
        x=[]
        while(L<=R):
            if check(L):
                x.append(L)
                break
            L+=1
        L=temp
        while(L<=R):
            if check(R):
                x.append(R)
                break
            R-=1
        if len(x)==0:
            print(-1)
        else:
            print(max(x)-min(x))

import math
def check(T):
    if T>1:
        for i in range(2, int(math.sqrt(T))+1):
            if T%i == 0:
                return False
        return True

main()
