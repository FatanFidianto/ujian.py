def menu():
    print("""
===================================
SELAMAT DATANG DI RESTORAN MAKANAN
===================================
1. cek produk
2. cek ketersediaan
3. beli
4. cetak struk
5. exit
""")
    
def lihat_produk():
    print('\nList Makanan : ')
    print('1. rendang    = Rp.25000/makanan')
    print('2. tunjang    = Rp.35000/makanan')
    print('3. ayam bakar = Rp.25000/makanan/n')

def cek_ketersediaan(rendang, tunjang, ayam_bakar):
    print('\nList ketersediaan : ')
    print(f'1. rendang    = {rendang}')
    print(f'2. tunjang    = {tunjang}')
    print(f'3. ayam bakar = {ayam_bakar}')

def beli_produk(saldo, rendang, tunjang, ayam_bakar):
    if pilihan == '1':
        saldo
        jenis = 'rendang'
        harga = 25000
        jumlah = int(input('berapa banyak : '))
        total = harga * jumlah
        pembelian = saldo - total
        if rendang < jumlah:
            print('maaf stok makanan tidak ada')
        else:
            if total > saldo:
                print('maaf saldo tidak cukup')
            else:
                print(f'Berhasil membeli {jenis}, dengan harga {harga}')
                print(f'saldo saat ini : {pembelian}')
            try:
                except Exception 
                with open('struk.txt','a') as struk:
                    struk.write('===================')
                    struk.write('  STRUK PEMBELIAN  ')
                    struk.write('===================')
                    struk.write(f'jenis makanan  = {jenis}')
                    struk.write(f'Harga satuan   = {harga}')
                    struk.write(f'jumlah makanan = {jumlah}')
                    struk.write(f'total harga    = {total}')
                    struk.write(f'kembalian      = {pembelian}')
                except Exception as e:
                    print(e)


    elif pilihan == '2':
        saldo
        jenis = tunjang
        harga = 30000
        jumlah = int(input('berapa banyak : '))
        total = harga * jumlah
        pembelian = saldo - total
        if rendang < jumlah:
            print('maaf stok makanan tidak ada')
        else:
            if total > saldo:
                print('maaf saldo tidak cukup')
            else:
                print(f'Berhasil membeli {jenis}, dengan harga {harga}')
                print(f'saldo saat ini : {pembelian}')
            try:
                except Exception 
                with open('struk.txt','a') as struk:
                    struk.write('===================')
                    struk.write('  STRUK PEMBELIAN  ')
                    struk.write('===================')
                    struk.write(f'jenis makanan  = {jenis}')
                    struk.write(f'Harga satuan   = {harga}')
                    struk.write(f'jumlah makanan = {jumlah}')
                    struk.write(f'total harga    = {total}')
                    struk.write(f'kembalian      = {pembelian}')
                except Exception as e:
                    print(e)

    elif pilihan == '3':
        saldo
        jenis = ayam_bakar
        harga = 25000
        jumlah = int(input('berapa banyak : '))
        total = harga * jumlah
        pembelian = saldo - total
        if rendang < jumlah:
            print('maaf stok makanan tidak ada')
        else:
            if total > saldo:
                print('maaf saldo tidak cukup')
            else:
                print('Berhasil membeli {jenis}, dengan harga {harga}')
                print(f'saldo saat ini : {pembelian}')
            try:
                except Exception 
                with open('struk.txt','a') as struk:
                    struk.write('===================')
                    struk.write('  STRUK PEMBELIAN  ')
                    struk.write('===================')
                    struk.write(f'jenis makanan  = {jenis}')
                    struk.write(f'Harga satuan   = {harga}')
                    struk.write(f'jumlah makanan = {jumlah}')
                    struk.write(f'total harga    = {total}')
                    struk.write(f'kembalian      = {pembelian}')
                except Exception as e:
                    print(e)

    else:
        print('error')

def cetak_struk():
    try:
        with open()

def exit():
    print('Terima kasih telah membeli!!')

def main():
    saldo = 200000
    rendang = 50
    tunjang = 50
    ayam_bakar = 50

    while True:
        main()
        pilihan = int(input('pilih menu : '))
        if pilihan == '1':
            lihat_produk()
        elif pilihan == '2':
            cek_ketersediaan(rendang, tunjang, ayam_bakar)
        elif pilihan == '3':
            beli_produk(saldo, rendang, tunjang, ayam_bakar)
        elif pilihan == '4':
            cetak_struk()
        elif pilihan == '5':
            exit()
            break
        else:
            print('pilihan error')

if __name__ == '__main__':
    main()
