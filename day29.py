if __name__ == '__main__':
    d = []
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        for s in range(1, n + 1):
            for i in range(1, s):
                f = i & s
                m = 0
                if f < k < m:
                    d.append()

        print(max(d))
        d.clear()
