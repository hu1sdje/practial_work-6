cell = input()
if cell[0] == 'a' or cell[0] == 'c' or cell[0] == 'e' or cell[0] == 'g':
    if int(cell[1]) % 2 == 0:
        print('белая')
    else:
        print('черная')
else:
    if int(cell[1]) % 2 == 0:
        print('черная')
    else:
        print('белая')
