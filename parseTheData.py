import binascii
binary_string = binascii.unhexlify(input())
split = str(binary_string).split('\\')
for c in split:
    print(c)