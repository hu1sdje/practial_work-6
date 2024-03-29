vanya = int(input())
kolya = int(input())
word_1 = [0]
for i in range(3, 0, -1):
    if 1 <= vanya <= 200:
        word_1.append(vanya % (10 ** i) // (10 ** (i - 1)))
    else:
        print('ERROR')

if len(word_1) > kolya:
    print(word_1[kolya])
else:
    print(word_1[kolya % len(word_1)])