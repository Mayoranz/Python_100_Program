nilai = int(input('Masukan Nilai: '))

if nilai>= 90:
    Grade= 'A'
elif nilai >= 80:
    Grade= 'B'
if nilai>= 70:
    Grade= 'c'
elif nilai <= 69:
    Grade= 'E'
print('Status Kelulusan : {}'.format(Grade))