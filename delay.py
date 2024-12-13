'''dibuat tanggal 13-12-2024
oleh Andhika Noor Hidayat'''
import time
def hitung_mundur(jumlah_detik):
    while jumlah_detik:
        menit, detik = divmod(jumlah_detik, 60)
        timer = '{:02d}:{:02d}'.format(menit, detik)
        print(timer, end="\r")
        time.sleep(1)
        jumlah_detik -= 1
    print("Waktu habis!")
try:
    detik_input = int(input("Masukkan jumlah detik untuk hitung mundur: "))
    hitung_mundur(detik_input)
except ValueError:
    print("Silakan masukkan angka yang valid.")