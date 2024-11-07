print('='*40)
print('Warna Lampu Lalu Lintas ')
print('='*40)
warn = input('Masukan Warna: ').lower()

if warn == 'merah' :
    print ('berhenti')
elif warn == 'kuning' :
    print ('Hati Hati')
elif warn == 'hijau' :
    print ('Sok mangga jalan a')
else:
  print ('Lalu lintas mana yang pake',warn)