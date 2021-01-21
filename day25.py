import math
def prime(n):
    if n<=1:
        return "Not prime"
    if n==2:
        return "prime"
    if n>=2 and n%2==0:
        return "Not Prime"
    d=math.floor(math.sqrt(n))
    for x in range(3,d+1,2):
        if n%x==0:
            return "Not prime"
    return "Prime"

k=int(input())
for i in range(k):
    n=int(input())
    print(prime(n))
