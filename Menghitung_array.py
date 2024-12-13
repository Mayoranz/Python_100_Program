'''dibuat tanggal 13-12-2024
oleh Andhika Noor Hidayat'''
angka_list = []
jumlah_angka = int(input("Masukkan jumlah angka yang ingin dimasukkan: "))
for i in range(jumlah_angka):
    angka = int(input(f"Masukkan angka ke-{i+1}: "))
    angka_list.append(angka)
print("\nAngka yang dimasukkan:")
for angka in angka_list:
    print(angka)
total = sum(angka_list)
print(f"\nTotal dari angka-angka tersebut adalah: {total}")