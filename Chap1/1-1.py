"""
くじびき

入力
n m
k_1 k_2 ... k_n

制約
1 <= n <= 50
1 <= m <= 1e+8
1 <= k_i <= 1e+8
"""

if __name__ == '__main__':
    n, m = (int(x) for x in input().split())
    k = [int(x) for x in input().split()]
    f = False
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    if k[a] + k[b] + k[c] + k[d] == m:
                        f = True
    if f:
        print('Yes')
    else:
        print('No')