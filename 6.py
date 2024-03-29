n, k, m = map(int, input().split())
total_time = (n * 2) // k * m
if (n * 2) % k:
    total_time += m
print(total_time)
