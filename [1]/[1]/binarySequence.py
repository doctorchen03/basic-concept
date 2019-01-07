#Binary Sequence Types — bytes, bytearray, memoryview
#bytes and bytearray are used for manipulating binary data.
#memoryview access the memory of the binary objects.
print(bytes.fromhex('2Ef0F1f2'))#decode the hexadecimal digits.
print(b'\xf0\xf1\xf2'.hex())#return a string containing two hexadecimal digits for each byte.
print(bytearray.fromhex('2Ef0F1f2'))
print(bytearray(b'\xf0\xf1\xf2').hex())

v = memoryview(b'abcefg')#get memory information from a bytes object.
print(v[1])#get memory address of b'b'
print(v[1:2])#get memory address of b'bc'
print(bytes(v[1:2]))#get b'bc' bytes string with the memory address