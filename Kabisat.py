a = int(input('masukan Tahun '))
if a%1000 == 0 or a%4 == 0 :
    print(f'tahun {a} adalah tahun kabisat')
else :
    print(f'tahun {a} bukan tahun kabisat')