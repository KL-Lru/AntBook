"""
三角形

入力
n
a_1 a_2 ... a_n

制約
3 <= n <= 100
1 <= a_i <= 1e+8
"""

if __name__ == '__main__':
    ans = 0
    n = int(input())
    a = sorted([int(x) for x in input().split()],reverse=True)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if a[i] < a[j] + a[k]:
                    ans = max(ans, a[i] + a[j] + a[k])
    print(ans)