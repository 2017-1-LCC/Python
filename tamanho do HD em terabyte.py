tam=int(input("Informe o valor em TB :"))
gb= tam * 1024
mb= gb * 1024
kb= mb * 1024
B= kb * 1024
b= B * 8

print(gb, "GB")
print(mb, "MB")
print(kb, "KB")
print(B, "Byte")
print(b, "bit")
