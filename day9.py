def factorial(N):
    d=1
    for x in range(1,N+1):
        d*=x
    return(d)
n=int(input())
print(factorial(n))