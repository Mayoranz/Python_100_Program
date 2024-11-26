suhu = float(input("Masukkan suhu tubuh: "))
if suhu > 37.5:
    print("Anda demam.")
elif suhu < 20.5:
    print("Anda terlalu dingin.")
else:
    print("Suhu tubuh normal.")