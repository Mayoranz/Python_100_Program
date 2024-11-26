a = int(input("Masukkan jumlah angka: "))
positif = 0
negatif = 0
for _ in range(a):
    angka = float(input("Masukkan angka: "))
    if angka > 0:
        print("Positif")
    elif angka < 0:
        print("Negatif")