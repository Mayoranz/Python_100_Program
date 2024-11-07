x = int(input('Masukan X: '))
y = int(input('Masukan Y: '))
z = int(input('Masukan Z: '))
#besar
if x >= y and x > z:
        print(f'Nilai terbesar adalah {x} :)')
elif y > x and y > z:
        print(f'Nilai terbesar adalah {y} :)')
elif z > x and z > y:
        print(f'Nilai terbesar adalah {z}')
#kecil
if x < y and x < z:
        print(f'Nilai terkecil adalah {x}')
elif y < x and y < z:
        print(f'Nilai terkecil adalah {y}')
elif z < x and z < y:
        print(f'Nilai terkecil adalah {z}')