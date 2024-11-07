while True:
    print('\n\033[92m=================================')
    print('\033[31m       Tulisan Diskon      ')
    print('\033[92m=================================')

    br1 = input('\033[33mMasukan harga barang 1: Rp. ')
    br2 = input('\033[33mMasukan harga barang 2: Rp. ')
    br3 = input('\033[33mMasukan harga barang 3: Rp. ')
    br4 = input('\033[33mMasukan harga barang 4: Rp. ')

    Total = int(br1)+int(br2)+int(br3)+int(br4)

    print(f'\n\033[37mTotal Belanja: Rp. {Total}')

    if Total >= 100000:
        print(' selamat Anda mendapatkan Diskon')

    elif Total <= 100000:
        print('Belanja dikit lagi dong biar daper diskon')