def xor_cipher(msg1, msg2):

    digs = "0123456789abcdef"

    lst1 = ([digs.index(i) for i in msg1])
    lst2 = ([digs.index(i) for i in msg2])

    return ''.join([digs[a ^ b] for a, b in zip(lst1, lst2)])

print(xor_cipher("1020304", "403201"))


