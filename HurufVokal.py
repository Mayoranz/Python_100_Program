print ('='*40)
a = str(input('masukan huruf\n'))

if a in 'aiueo':
    print ('ini vokal bang')
elif a.isdigit():
    print("ini bukan huruf bang")
else:
    print ('ini konsonan bang')