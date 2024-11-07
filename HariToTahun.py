TAHUN_HARI = 365
BULAN_HARI = 30
hari1 = int(input('hari : '))
tahun = int(hari1/TAHUN_HARI)
hari1 = hari1 % TAHUN_HARI
bulan = int(hari1/BULAN_HARI)
hari1 = hari1 % BULAN_HARI

print (tahun,'tahun',bulan,'bulan',hari1,'hari')