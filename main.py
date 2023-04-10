class Produk: 
    def __init__(self, nama, harga, kuantitas):
        self.nama = nama
        self.harga = harga
        self.kuantitas = kuantitas

    def get_nama(self):
        return self.nama
    def get_harga(self):
        return float (self.harga)
    def get_kuantitas(self):
        return self.kuantitas
    def update_kuantitas(self):
        if self.kuantitas - 1 < 0:
         print('Barang sudah tidak tersedia')
         return False
        else:
            self.kuantitas -= 1
            return True
class Elektronik(Produk):
    def __init__(self, nama, harga, kuantitas, garansi):
        super().__init__(nama, harga, kuantitas)
        self.garansi = garansi

    def get_garansi(self):
        return self.garansi

class pakaian(Produk) :
    def __init__(self, nama, harga, kuantitas, ukuran):
        super().__init__(nama, harga, kuantitas)  
        self.ukuran = ukuran 

    def get_ukuran(self):
        pass

class Book(Produk):
    def __init__(self, nama, harga, kuantitas, penulis):
        super().__init__(nama, harga, kuantitas)   
        self.penulis = penulis 

    def get_penulis(self):
        pass

class Keranjang:
    def __init__(self):
        self.items = []
    def tambah_ke_keranjang(self, item):
        for i in self.items:
            if i['nama'] == item['nama']:
                i['kuantitas'] += 1
                print('Produk berhasil di tambahkan ke keranjang')
                return True
        self.items.append(item)
        print('Prouduk berhasil di tambah ke keranjang')
    def hapus_dari_keranjang(self, item):
        self.items.pop(item-1)
    def lihat_keranjang(self):
        x = 1
        for i in self.items:
            print(x, i['nama'], '- Harga: ', i['harga'], 'Kuantitas: ', i['kuantitas'] )
            x+=1
    def pemesanan(self):
        pass 

produk1 = Elektronik('Iphone (Elektronik)', 100, 50, "20 Tahun")
produk2 = Elektronik('Samsung(Elektronik)', 100, 2, "20 Tahun")
produk3 = Elektronik('Oppo (Elektronik)', 100, 50, "20 Tahun")
produk4 = Elektronik('Infinix (Elektronik)', 100, 50, "20 Tahun")
Keranjang = Keranjang()

print('Selamat Datang di sistem toko') 
print(" 1. ",produk1.get_nama(), "- Harga: ",produk1.get_harga(),"Kuantitas", produk1.get_kuantitas(), "Garansi: ", produk1.get_garansi())
print(" 2. ",produk2.get_nama(), "- Harga: ",produk2.get_harga(),"Kuantitas", produk2.get_kuantitas(), "Garansi: ", produk2.get_garansi())
print(" 3. ",produk3.get_nama(), "- Harga: ",produk3.get_harga(),"Kuantitas", produk3.get_kuantitas(), "Garansi: ", produk3.get_garansi())
print(" 4. ",produk4.get_nama(), "- Harga: ",produk4.get_harga(),"Kuantitas", produk4.get_kuantitas(), "Garansi: ", produk4.get_garansi())
while True:
    pilihan = input('Masukan no produk untuk menambahkan produk ke keranjang( atau 0 untuk keluar):')
    if pilihan == '1':
        pk1 =   {
                  'nama': produk1.get_nama(),
                  'harga': produk1.get_harga(),
                  'kuantitas': 1

                }
        if produk1.update_kuantitas():
            Keranjang.tambah_ke_keranjang(pk1)

    elif pilihan == '2':
        pk2 =   {
                    'nama':produk2.get_nama(),
                    'harga':produk2.get_harga(),
                    'kuantitas': 1
                }
        if produk2.update_kuantitas():
            Keranjang.tambah_ke_keranjang(pk2)

        

    elif pilihan == '3':
        pk3 =   {
                  'nama': produk3.get_nama(),
                  'harga': produk3.get_harga(),
                  'kuantitas': 1
                }
        if produk3.update_kuantitas():
            Keranjang.tambah_ke_keranjang(pk3)

        

    elif pilihan == '4':
        pk4 =   {
                  'nama':produk4.get_nama(),
                  'harga':produk4.get_harga(),
                  'kuantitas': 1
                }
        if produk4.update_kuantitas():
            Keranjang.tambah_ke_keranjang(pk4) 
                  

    elif pilihan == '0':
     if len(Keranjang.items) > 0:
        while True:
            Keranjang.lihat_keranjang()
            pilihan = input('Masukan 1 untuk order, 2 untuk hapus dari keranjang, 0 untuk keluar : ')
            if  pilihan == '1':
                jumlah = 0
                for i in Keranjang.items:
                    jumlah += (i['harga'] * i['kuantitas'])
                print('Ringkasan pesanan:')
                print('Total harga:',jumlah)
                print('Terima kasih telah berbelanja')
                exit()
            elif pilihan =='2':
                Keranjang.lihat_keranjang()
                pilihan = input('Masukan nomor produk yang akan di hapus : ')
                for i in Keranjang.items:
                    if i['nama']==produk1.get_nama():
                        produk1.kuantitas += Keranjang.items[int(pilihan)-1]['kuantitas']
                    elif i['nama']==produk1.get_nama():
                        produk2.kuantitas += Keranjang.items[int(pilihan)-1]['kuantitas']
                    elif i['nama']==produk1.get_nama():
                        produk3.kuantitas += Keranjang.items[int(pilihan)-1]['kuantitas']
                    else:
                        produk4.kuantitas += Keranjang.items[int(pilihan)-1]['kuantitas']
                Keranjang.hapus_dari_keranjang(int(pilihan))
            elif pilihan == '0':
                exit()
        else:
            exit()
