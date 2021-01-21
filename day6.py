
t=int(input())

for x in range(0,t):
    d = ""
    e = "  "
    s=str(input())
    for y in range(0,len(s)):
        if y%2==0:
            d+=s[y]
        elif y%2!=0:
            e+=s[y]
    print(d,e)

