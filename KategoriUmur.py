usia = int(input("Masukkan usia: "))
if usia < 0:
    print("Usia tidak valid.")
elif usia <= 12:
    print("Anak-anak")
elif usia <= 19:
    print("Remaja")
elif usia <= 64:
    print("Dewasa")
else:
    print("Lansia")