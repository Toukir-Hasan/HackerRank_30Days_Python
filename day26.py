import datetime

def fff(a,b,c,d,e,f):
    x=datetime.date(c,b,a)
    y=datetime.date(f,e,d)
    if x.year<y.year:
        return 0
    if x.year>y.year:
        return 1000
    if x.year==y.year:
        if  x.month<=y.month and x.day<=y.day:
            return 0

    if x.year==y.year and x.month>y.month:
        return (500*(b-e))
    if x.day>y.day and x.month==y.month and x.year==y.year:
        return (15*(a-d))

a,b,c=map(int,input().split())
d,e,f=map(int,input().split())
print(fff(a,b,c,d,e,f))
