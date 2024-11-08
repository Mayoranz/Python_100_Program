print('='*40)
print('Password')
print('='*40)

USERNAM = 'hidayatandhika4@gmail.com'
PASSWORD = '12345678'

user = input('Masukan Username: ')
pw = input('Masukan Password: ')
true = USERNAM and PASSWORD

#blok perjabangan
if user != USERNAM :
    print ('username tidak di temukan')
elif user == USERNAM and pw != PASSWORD :
    print ('password slah')
else:
  print ('selamat datang',USERNAM)