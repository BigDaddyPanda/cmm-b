n=int(input())
d=[list(map(int,input().split()))for i in range(n)]
d.append(d[0])
v=[(d[i][0]-d[i+1][0])**2+(d[i][0]-d[i+1][0])**2 for i in range(n)]
_=lambda i:i**0.5
print(round(sum(map(_,v)),3))