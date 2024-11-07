detik1 = int(input('detik : '))
menit1 = int(detik1 / 60)
detik = detik1 % 60
jam1 = int(menit1/60)
menit = menit1 % 60
hari1 = int(jam1/24)
jam = jam1 % 24
hari = hari1 % 24

print (detik1,'adalah',hari,'hari',jam,'jam',menit,'Menit dan',detik,'detik')