"""
Ants

入力
L n
x_1 x_2 ... x_n

制約
1 <= L <= 1e+6
1 <= n <= 1e+6
0 <= x_i <= L
"""

if __name__ == '__main__':
    L, n = (int(a) for a in input().split())
    x = [int(a) for a in input().split()]
    mn = 0
    mx = 0
    for p in x:
        mx = max(mx, max(L-p, p))
        mn = max(mn, min(L-p, p))

    print('min: ' + str(mn))
    print('max: ' + str(mx))