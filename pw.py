print('='*40)
print('Password')
print('='*40)

USERNAMA = 'hidayatandhika4@gmail.com'
PASSWORD = '12345678'

user = input('Masukan Username: ')
pw = input('Masukan Password: ')
true = USERNAMA and PASSWORD

#blok perjabangan
if user != USERNAMA :
    print ('username tidak di temukan')
elif user == USERNAMA and pw != PASSWORD :
    print ('password slah')
else:
  print ('selamat datang',USERNAMA)