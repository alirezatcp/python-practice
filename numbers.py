binary_number = 0b111
print(binary_number) # 7

octal_number = 0o72
print(octal_number) # 58

hexa_decimal = 0xf
print(hexa_decimal) # 15

number = 1_000_000
print(number) # 1000000

print(1e9) # 1000000000.0

print(-1e999) # -inf

print(1e999) # inf

z = 2j+5
print(z.real) # 5.0
print(z.imag) # 2.0
print(z.conjugate()) # (5-2j)
print(complex(z)) # (5+2j)
