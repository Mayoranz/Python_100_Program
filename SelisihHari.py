TAHUN = 356
BULAN = 30
hari1= int(input('masukan tanggal pertama '))
bulan1= int(input('masukan bulan pertama '))
tahun1= int(input('masukan tahun pertama '))
hari2= int(input('masukan tanggal kedua '))
bulan2= int(input('masukan bulan kedua '))
tahun2= int(input('masukan tahun kedua '))

tanggal1=hari1+bulan1+tahun1
tanggal2=hari2+bulan2+tahun2
selisih=tanggal1-tanggal2

tahun = int(selisih/TAHUN)
bulan4 = selisih % TAHUN
bulan = int(bulan4/BULAN)
hari3= bulan4 % BULAN
