kalori = int(input("Masukkan jumlah kalori: "))
if kalori < 200:
    print("Makanan rendah kalori.")
elif 200 <= kalori < 500:
    print("Makanan sedang kalori.")
else:
    print("Makanan tinggi kalori.")