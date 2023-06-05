#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
        if ord(str[x]) >= ord('a') and ord(str[x]) <= ord('z'):
            atoA = ord(str[x]) + (ord('A') - ord('a'))
        else:
            atoA = ord(str[x])
        print("{}".format(chr(atoA)), end='')
    print()
