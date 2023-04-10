print("Selamat datang di program bangun datar")
print(" ==================================== ")

print("Pilih bangun datar :")
print("    1. Segitiga     ")
print("    2. Lingkaran    ")
print("    3. Persegi      ")
print("    4. Persegi panjang      ")

pilihan =int(input("Masukkan pilihan anda : "))
if (pilihan == 1):
        print("Pilih salah satu:")
        print("   1.Luas Segitiga   ")
        print("   2.Keliling Segitiga    ")
        pilihan1 =int(input("Masukan pilihan:"))
        if pilihan1 == 1:
             print("    Menghitung luas segitiga    ")
             print("     ======================     ")
             alas = int(input("Masukkan Alas: "))
             tinggi = int(input("Masukkan Tinggi : "))
             luas = 0.5*alas*tinggi
             print("     ======================     ")
             print("Luas segitiga dari alas",alas,"cm" , "tinggi ",tinggi,"cm", "adalah: "+ str(luas),"cm")
             print("Terimakasih Telah Menggunakan program saya")
        elif pilihan1 == 2:
             print("    Menghitung Keliling Segitiga   ")
             print("    ============================    ")
             a=int(input("Masukan sisi 1 : "))
             b=int(input("Masukan sisi 2 : "))
             c=int(input("Masukan sisi 3 : "))
             kel = a + b + c
             print("    ============================    ")
             print("Keliling Segitiga Adalah:",kel)
             print("Terimakasih Telah Menggunakan program saya")
        else:
             print("Pilihan yang anda masukan tidak sesuai")
       
                         
elif (pilihan == 2):
        print("Pilih salah satu:")
        print("    1.Luas Lingkaran   ")
        print("    2.Keliling Lingkaran    ")
        pilihan1 =int(input("Masukan pilihan:"))
        if pilihan1 == 1:
             print("    Menghitung luas Lingkaran    ")
             print("     ======================     ")
             phi = 3.14
             r = float(input("Masukkan panjang jari-jari lingkaran: "))
             luas = phi*(r*r)
             print("Luas lingkaran adalah : "+ str(luas))
             print("     ======================     ")
             print("Luas Lingkaran dari phi",phi , " dan jari-jari ",r, "adalah: "+ str(luas))
             print("Terimakasih Telah Menggunakan program saya")
        elif pilihan1 == 2:
             print("    Menghitung Keliling Lingkaran   ")
             print("    ============================    ")
             phi = 3.14
             r = float(input("Masukan Jari-jari : "))
             keliling = 2*phi*r
             print("    ============================    ")
             print("Keliling Lingkaran Adalah:",keliling)
             print("Terimakasih Telah Menggunakan program saya")
        else:
             print("Pilihan yang anda masukan tidak sesuai")
elif (pilihan == 3):
        print("Pilih salah satu:")
        print("    1.Luas Persegi   ")
        print("    2.Keliling Persegi    ") 
        pilihan1 =int(input("Masukan pilihan:"))
        if pilihan1 == 1:
             print("    Menghitung luas Persegi    ")
             print("     ======================     ")
             s = float(input("\nMasukan Panjang Sisi: "))

             luas = s**2
             print("     ======================     ")
             print(print("Luas Persegi Adalah:",luas))
             print("Terimakasih Telah Menggunakan program saya")
        elif pilihan1 == 2:
             print("    Menghitung Keliling Persegi   ")
             print("    ============================    ")
             s = float(input("\nMasukan Panjang Sisi: "))
             keliling = 4 * s
             print("    ============================    ")
             print("Keliling Persegi Adalah:",keliling)
             print("Terimakasih Telah Menggunakan program saya")
        else:
             print("Pilihan yang anda masukan tidak sesuai")

elif (pilihan == 4):
        print("Pilih salah satu:")
        print("    1.Luas Persegi Panjang   ")
        print("    2.Keliling Persegi Panjang    ") 
        pilihan1 =int(input("Masukan pilihan:"))
        if pilihan1 == 1:
             print("    Menghitung Persegi Panjang    ")
             print("     ======================     ")
             panjang = float(input("Masukan Panjang: "))
             lebar = float(input("Masukan Lebar: "))
             luas = panjang*lebar
             print("     ======================     ")
             print("Luas Persegi Panjang Adalah:",luas)
             print("Terimakasih Telah Menggunakan program saya")
        elif pilihan1 == 2:
             print("    Menghitung Keliling Persegi Panjang   ")
             print("    ============================    ")
             panjang = float(input("Masukan Panjang: "))
             lebar = float(input("Masukan Lebar: "))
             keliling = 2 * (panjang+lebar)

             print("    ============================    ")
             print("Keliling Persegi  Panjang Adalah:",keliling)
             print("Terimakasih Telah Menggunakan program saya")
        else:
             print("Pilihan yang anda masukan tidak sesuai")
else:
       print("Pilihan yang anda masukan tidak sesuai")


#Tugas
# Nama:Ade Farhan G
  