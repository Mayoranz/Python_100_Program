usia = int(input("Masukkan usia: "))
if usia < 13:
    print("Film untuk anak-anak.")
elif usia < 18:
    print("Film remaja.")
else:
    print("Film dewasa.")