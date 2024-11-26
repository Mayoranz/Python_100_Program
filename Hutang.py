Hutang = float(input("Masukkan jumlah Hutang: "))
if Hutang < 1000000:
    bunga = 0.1
else:
    bunga = 0.08
print(f"Suku bunga: {bunga * 100}%")