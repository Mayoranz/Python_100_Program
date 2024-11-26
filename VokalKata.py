a = str(input('Masukan Kata'))
v = "aeiou"
hasil = sum(1 for kata in a if kata in v)
print(hasil)