cell = input()
alphabet = 'abcdefgh'
if int(cell[1]) % 2 != 0 and cell[0] in alphabet and 0 < int(cell[1]) < 9:
    print('черная')
else:
    print('белая')
