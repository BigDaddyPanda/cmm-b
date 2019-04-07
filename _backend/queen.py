n,m=map(int,input().split())
x,y=map(int,input().split())
res=[[0 for j in range(n)]for i in range(n)]

def _move(d,p):
    global res,x,y
    x1,y1=x,y
    if d in "NS":
        y1=y+(p if d=="N" else -p)
        for i in range(y+1,y1+1):
            res[i][x]+=1
    else:
        x1=x+(p if d=="E" else -p)
        for i in range(x+1,x1+1):
            res[y][i]+=1
    x,y=x1,y1
    

for i in range(m):
    d,p=input().split()
    p=int(p)
    _move(d,p)
    
for i in range(n):
    print(" ".join(map(str,res[i])))