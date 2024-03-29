cell = input()
alphabet = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
if (abs(alphabet[cell[0]] - alphabet[cell[3]]) + abs(alphabet[cell[1]] - alphabet[cell[4]])) == 3:
    print('верно')
else:
    print('неверно')
