
n=int(input())
d={}
f=[]
for x in range(n):
    keys,values=(input().split())
    d[keys]=values
for y in range(n):
    z=input()
    f.append(z)
for c in f:
    if c in d:
        print(c,end="")
        print("=",end='')
        print(d[c])
    else:
        print("Not found")


