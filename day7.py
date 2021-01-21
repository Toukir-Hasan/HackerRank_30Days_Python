t=int(input())
s=(input())
k=list((map(int,s.split())))
if len(k)==t:
    reverse=k[::-1]
    for x in reverse:
        print(x,end=" ")
else:
    pass
