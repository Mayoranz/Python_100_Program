suhu = float(input("Masukkan suhu (°C): "))
if suhu < 20:
    print("Cuaca dingin.")
elif 20 <= suhu < 30:
    print("Cuaca sejuk.")
else:
    print("Cuaca panas.")