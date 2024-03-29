m, n, k = map(int, input().split())
if k % m == 0 or k % n == 0:
    print('осуществимо')
else:
    print('неосуществимо')