#Dibuat Oleh Andhika Noor H
#Tanggal 24/09/2024

r = int(input('masukan jari jari '))
s = int(input('masukan sisi miring '))
t = int (input('masukan tinggi '))
phi = 3.14
selimut = phi*r*s
Lpermukaan = (phi*r*s)+(phi*r*r)
volume = 1/3 * phi * r * r * t
print (f'''
Luas Selimut = {selimut}
luas permukaan = {Lpermukaan}
volume = {volume}
       ''')