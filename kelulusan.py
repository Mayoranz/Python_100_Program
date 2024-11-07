print('='*40)
print('Program kelulusan')
print('='*40)

nilai = int(input('Masukan Nilai: '))

if nilai>= 75:
    status= 'LULUS'
elif nilai <= 75:
    status= 'TIDAK LULUS'
print('Status Kelulusan : {}'.format(status))