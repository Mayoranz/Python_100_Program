'''dibuat tanggal 13-12-2024
oleh Andhika Noor Hidayat'''
n = int(input("Masukkan batas atas: "))
print("Bilangan prima hingga", n, ":")
for num in range(2, n + 1):
    is_prima = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prima = False
            break
    if is_prima:
        print(num, end=' ')