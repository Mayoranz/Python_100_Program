#Dibuat Oleh Andhika Noor H
#Tanggal 24/09/2024
print('='*40)
print('Program tabung')
print('='*40)

r = int(input("masukan jari-jari dalam cm: "))
t = int(input("masukan tinggi dalam cm: "))
phi = 3.14


volume = 2*phi*r*t
luas_permukaan=(phi*r*r)+(2*phi*r*t)

print(f"Volume tabung adalah ={volume} cm3")
print(f"luas tabung adalah ={luas_permukaan} cm2")