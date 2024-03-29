k = int(input())
n = 100
for i in range(1, n):
    for j in range(1, n):
        if k % (i * 5 + j * 7) == 0:
            print('да')
        else:
            print('нет')
        break
    break