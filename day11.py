def sss(mat,row,col):
    s=0
    s+=mat[row-1][col-1]
    s+=mat[row-1][col]
    s+=mat[row-1][col+1]
    s+=mat[row][col]
    s+=mat[row+1][col-1]
    s+=mat[row+1][col]
    s+=mat[row+1][col+1]
    return (s)

a=[]
for x in range(6):
    d=[int(k) for k in input().split(" ")]
    a.append(d)
f=-36
for i in range(1,5):
    for j in range(1,5):
        e=sss(a,i,j)
        if e>f:
            f=e
print(f)