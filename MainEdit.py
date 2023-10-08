#---------------------------------------------------------------- Fungsi Matematika -------------------------------------------------------------

#------------------------------------------------------------------- Aritmatika ------------------------------------------------------------------
import math
import statistics

def penjumlahan():
    total = 0
    while True:
        num = int(input("Operasikan penjumlahan : "))
        total += num
        lanjut = int(input("Lanjut penjumlahan?\n1. Ya\n2. Tidak\nPilih : "))
        if lanjut == 1: 
            continue
        elif lanjut == 2: 
            print(f"Hasil penjumlahan = {total}\n")
            break

def pengurangan():      
    total = int(input("Masukkan angka : "))
    while True: 
        num = int(input("Kurangkan dengan : "))
        total -= num
        lanjut = int(input("Lanjut pengurangan?\n1. Ya\n2. Tidak\nPilih : "))
        if lanjut == 1: 
            continue
        elif lanjut == 2:
            print(f"Hasil pengurangan : {total}")
            break

def perkalian(): 
    awal = int(input("Masukkan angka : "))
    while True:
        num = int(input("Kalikan dengan : "))
        awal *= num
        lanjut = int(input("1. Ya\n2. Tidak\nLanjut perkalian? "))
        if lanjut == 1:
            continue
        elif lanjut == 2: 
            print(f"Hasil perkalian : {awal}")
            break

def pembagian(): 
    awal = float(input("Masukkan angka : "))
    while True:
        num = float(input("Bagi dengan : "))
        awal /= num
        lanjut = int(input("Lanjut perkalian?\n1. Ya\n2. Tidak\nPilih : "))
        if lanjut == 1: 
            continue
        elif lanjut == 2: 
            print(f"Hasil pembagian : {awal}")
            break

def Un():
    a = int(input("Suku pertama : "))
    b = int(input("Beda barisan : "))
    n = int(input("jumlah suku : "))
    hasil = a + (n-1) * b
    print(f"Suku ke n adalah : {hasil}")
    return hasil

def Sn(): 
    a = int(input("Suku pertama : "))
    b = int(input("Beda barisan : "))
    n = int(input("jumlah suku : "))
    hasil = n/2 * (2*a + (n - 1) * b)
    print(f"Jumlah {n} suku pertama adalah {hasil}")
    return hasil


#------------------------------------------------------------------ Bangun Datar --------------------------------------------------------------------
def persegi():
    run = 1
    while run == 1:
        pilih = int(input("1. Luas\n2. Keliling\n3. Back to menu\nPilih : "))
        if pilih == 1: 
            p = int(input("Masukkan panjang : "))
            k = 4 * p
            print(f"keliling persegi adalah : {k}")
        elif pilih == 2: 
            p = int(input("Masukkan panjang : "))
            k = 4 * p
            print(f"keliling persegi adalah : {k}")
        elif pilih == 3:
            run = 0

def persegiPanjang():
    run = 1
    while run == 1:
        pilih = int(input("1. Luas\n2. Keliling\n3. Back to menu\nPilih : "))
        if pilih == 1:
            p = int(input("Masukkan panjang : "))
            l = int(input("Masukkan lebar : "))
            luas = p * l
            print(f"Luas persegi panjang adalah : {luas}")
        elif pilih == 2:
            p = int(input("Masukkan panjang : "))
            l = int(input("Masukkan lebar : "))
            k = 2 * (p + l)
            print(f"Keliling persegi panjang adalah : {k}")
        elif pilih == 3:
            run = 0

def sSamaSisi(): 
    run = 1
    while run == 1:
        pilih = int(input("1. Luas\n2. Keliling\n3. Pilih jenis segitiga\nPilih : "))
        if pilih == 1: 
            a = float(input("Masukkan alas : "))
            t = ((a/2)**2) + (a**2)
            tinggi = math.sqrt(t)
            l = (a * tinggi) / 2
            print(f"Luas segitiga sama sisi adalah : {l}")
        elif pilih == 2: 
            s = float(input("Masukkan panjang sisi : "))
            k = s * 3
            print(f"Keliling segitiga sama sisi adalah : {k}")
        elif pilih == 3: 
            run = 0

def sSamaKaki():
    run = 1
    while run == 1: 
        pilih = int(input("1. Luas\n2. Keliling\n3. Pilih jenis segitiga\nPilih : "))
        if pilih == 1: 
            a = float(input("Masukkan alas : "))
            t = float(input("Masukkan tinggi : "))
            l = (a * t) / 2
            print(f"Luas segitiga sama kaki adalah : {l}")
        elif pilih == 2: 
            s = float(input("Masukkan panjang sisi yang sama : "))
            a = float(input("Masukkan panjang alas : "))
            k = a + (2 * s)
            print(f"Keliling segitiga sama kaki adalah : {k}")
        elif pilih == 3: 
            run = 0

def sSembarang():
    run = 1
    while run == 1: 
        pilih = int(input("1. Luas\n2. Keliling\n3. Pilih jenis segitiga\nPilih : "))
        if pilih == 1: 
            a = float(input("Masukkan alas : "))
            t = float(input("Masukkan tinggi : "))
            l = (a * t) / 2
            print(f"Luas segitiga sama kaki adalah : {l}")
        elif pilih == 2: 
            a = float(input("Masukkan panjang sisi 1 : "))
            b = float(input("Masukkan panjang sisi 2 : "))
            c = float(input("Masukkan panjang sisi 3 : "))
            k = a + b + c
            print(f"Keliling segitiga sama kaki adalah : {k}")
        elif pilih == 3: 
            run = 0

def lingkaran():
    run = 1 
    while run == 1:
        pilih = int(input("1. Luas\n2. Keliling\n3. Back to menu\nPilih : "))
        pi = 22/7
        if pilih == 1:
            r = float(input("Masukkan jari-jari lingkaran : "))
            l = pi * r * r
            luas = round(l, 2)
            print(f"Luas lingkaran adalah : {luas}")
        elif pilih == 2: 
            r = float(input("Masukkan jari-jari lingkaran : "))
            k = pi * r * 2
            keliling = round(k, 2)
            print(f"Keliling lingkaran adalah : {keliling}")
        elif pilih == 3: 
            run = 0

def trapesium():
    run = 1
    while run == 1:
        pilih = int(input("1. Luas\n2. Keliling\n3. Back to menu\nPilih : "))
        if pilih == 1: 
            a = float(input("Masukkan alas a : "))
            b = float(input("Masukkan alas b : "))
            t = float(input("Masukkan tinggi : "))
            luas = (a + b) * t / 2
            print(f"Luas trapesium sama kaki adalah : {luas}")
        elif pilih == 2: 
            a = float(input("Masukkan panjang sisi a : "))
            b = float(input("Masukkan panjang sisi b : "))
            c = float(input("Masukkan panjang sisi c : "))
            d = float(input("Masukkan panjang sisi d : "))
            k = a + b + c + d
            print(f"Keliling trapesium sama kaki adalah : {k}")
        elif pilih == 3: 
            run = 0

def jajarGenjang():
    run = 1
    while run == 1:
        pilih = int(input("1. Luas\n2. Keliling\n3. Back to menu\nPilih : "))
        if pilih == 1: 
            a = float(input("Masukkan alas : "))
            t = float(input("Masukan tinggi : "))
            luas = a * t
            print(f"Luas jajar genjang adalah : {luas}")
        elif pilih == 2: 
            a = float(input("Masukkan panjang alas : "))
            s = float(input("Masukkan panjang sisi miring : "))
            k = (a + s) * 2
            print(f"Keliling jajar genjang adalah : {k}")
        elif pilih == 3: 
            run = 0

def belahKetupat():
    run = 1
    while run == 1: 
        pilih = int(input("1. Luas\n2. Keliling\n3. Back to menu\nPilih : "))
        if pilih == 1: 
            d1 = float(input("Masukkan panjang diagonal 1 : "))
            d2 = float(input("Masukkan panjang diagonal 2 : "))
            l = (d1 * d2) / 2
            print(f"Luas belah ketupat adalah : {l}")
        elif pilih == 2: 
            s = float(input("Masukkan panjang sisi : "))
            k = s * 4
            print(f"Keliling belah ketupat adalah : {k}")
        elif pilih == 3:
            run = 0

def layangLayang():
    run = 1
    while run == 1: 
        pilih = int(input("1. Luas\n2. Keliling\n3. Back to menu\nPilih : "))
        if pilih == 1: 
            d1 = float(input("Masukkan panjang diagonal 1 : "))
            d2 = float(input("Masukkan panjang diagonal 2 : "))
            l = (d1 * d2) / 2
            print(f"Luas layang-layang adalah : {l}")
        elif pilih == 2: 
            sA = float(input("Masukkan panjang sisi pendek : "))
            sB = float(input("Masukkan panjang sisi panjang : "))
            k = (sA + sB) * 2
            print(f"Keliling layang-layang adalah : {k}")
        elif pilih == 3:
            run = 0

#------------------------------------------------------------------ Bangun Ruang --------------------------------------------------------------------

def kubus():
    run = 1
    while run == 1: 
        pilih = int(input("1. Volume\n2. Luas Permukaan\n3. Back to menu\nPilih : "))
        if pilih == 1: 
            s = float(input("Masukkan panjang sisi : "))
            v = s * s * s
            print(f"Volume kubus adalah : {v}")
        elif pilih == 2: 
            s = float(input("Masukkan panjang sisi : "))
            lp = 6 * (s * s)
            print(f"Luas permukaan kubus adalah : {lp}")
        elif pilih == 3: 
            run = 0

def balok():
    run = 1
    while run == 1: 
        pilih = int(input("1. Volume\n2. Luas Permukaan\n3. Back to menu\nPilih : "))
        if pilih == 1: 
            p = float(input("Masukkan panjang balok : "))
            l = float(input("Masukkan lebar balok : "))
            t = float(input("Masukkan tinggi balok : "))
            v = p * l * t
            print(f"Volume balok adalah : {v}")
        elif pilih == 2: 
            p = float(input("Masukkan panjang balok : "))
            l = float(input("Masukkan lebar balok : "))
            t = float(input("Masukkan tinggi balok : "))
            lp =  2 * ((p * l) + (p * t) + (l * t))
            print(f"Luas permukaan balok adalah : {lp}")
        elif pilih == 3: 
            run = 0
    
def tabung():
    run = 1 
    while run == 1:
        pilih = int(input("1. Volume\n2. Luas Permukaan\n3. Back to menu\nPilih: "))
        pi = 22/7
        if pilih == 1: 
            r = float(input("Masukkan jari-jari : "))
            t = float(input("Masukkan tingi : "))
            v = pi * r * r * t
            volume = round(v, 2)
            print(f"Volume tabung adalah : {volume}")
        elif pilih == 2: 
            r = float(input("Masukkan jari-jari : "))
            t = float(input("Masukkan tingi : "))
            lA = pi * r * r
            lAlas = round(lA, 2)
            lS = pi * r * t * 2 
            lSelimut = round(lS, 2)
            lP = (lA * 2) + lS
            lPermukaan = round(lP, 2)
            print(f"luas alas dan luas tutup tabung adalah : {lAlas}")
            print(f"luas selimut tabung adalah : {lSelimut}")
            print(f"Luas permukaan tabung = {lPermukaan}")

        elif pilih == 3: 
            run = 0

def prismaSegitiga():
    run = 1
    while run == 1: 
        pilih = int(input("1. Volume\n2. Luas Permukaan\n3. Pilih prisma\nPilih : "))
        if pilih == 1: 
            s = float(input("Masukkan panjang sisi alas prisma : "))
            tA = (s * s) - ((s / 2) * (s / 2))
            lA = (s * tA) / 2
            tP = float(input("Masukkan tinggi prisma : "))
            v = lA * tP
            print(f"Volume prisma segitiga sama sisi adalah : {v} ")
        elif pilih == 2:
            s = float(input("Masukkan panjang sisi alas prisma : "))
            tA = (s * s) - ((s / 2) * (s / 2))
            lA = (s * tA) / 2
            tP = float(input("Masukkan tinggi prisma : "))
            lp = tP * (3 * s) + (2 * lA)
            print(f"Luas permukaan prisma segitiga : {lp}")
        elif pilih == 3: 
            run = 0

def prismaPersegi(): 
    run = 1
    while run == 1: 
        pilih = int(input("1. Volume\n2. Luas Permukaan\n3. Pilih Prisma\nPilih : "))
        if pilih == 1: 
            p = float(input("Masukkan panjang sisi alas prisma : "))
            l = float(input("Masukkan lebar sisi alas prisma : "))
            tP = float(input("Masukkan tingi prisma : "))
            v = p * l * tP
            print(f"Volume prisma segiempat adalah : {v}")
        elif pilih == 2: 
            p = float(input("Masukkan panjang sisi alas prisma : "))
            l = float(input("Masukkan lebar sisi alas prisma : "))
            tP = float(input("Masukkan tingi prisma : "))
            lP = ((p * l) + (p * tP) + (l * tP)) * 2
            print(f"Luas permukaan prisma segiempat : {lP}")
        elif pilih == 3: 
            run = 0

def limasSamaSisi(): 
    run = 1
    while run == 1: 
        pilih = int(input("1. Volume\n2. Luas Permukaan\n3. Pilih jenis limas\nPilih : "))
        if pilih == 1: 
            s = float(input("Masukkan panjang rusuk : "))
            tA = (s ** 2) - ((s/2) ** 2)
            tinggiAlas = math.sqrt(tA)
            lA = s * tinggiAlas / 2
            tL = s * math.sqrt(6) / 3
            v = (lA * tL) / 3
            print(f"volume limas segitiga sama sisi adalah {v}")            
        elif pilih == 2: 
            s = float(input("Masukkan panjang rusuk : "))
            tA = (s ** 2) - ((s/2) ** 2)
            tinggiAlas = math.sqrt(tA)
            lA = s * tinggiAlas / 2
            lP = 4 * lA
            print(f"luas permukaan limas segitiga sama sisi : {lP}")
        elif pilih == 3: 
            run = 0

def limasSegiempat(): 
    run = 1 
    while run == 1: 
        pilih = int(input("1. Volume\n2. Luas Permukaan\n3. Pilih limas\nPilih : "))
        if pilih == 1: 
            s = float(input("Masukkan panjang alas : "))
            sm = float(input("Masukkan panjang sisi miring : "))
            lA = s ** 2
            tSM = (sm ** 2) - ((s/2) ** 2)
            tSisiMiring = math.sqrt(tSM)
            tL = (tSisiMiring ** 2) - ((s/2) ** 2)
            tinggiLimas = math.sqrt(tL)
            v = lA * tinggiLimas / 3
            print(f"volume limas segiempat : {v}")
        elif pilih == 2: 
            s = float(input("Masukkan panjang alas : "))
            sm = float(input("Masukkan panjang sisi miring : "))
            lA = s ** 2
            tSM = (sm ** 2) - ((s/2) ** 2)
            tSisiMiring = math.sqrt(tSM)
            lST = s * tSisiMiring / 2
            luasP = lA + (4 * lST)
            print(f"luas permukaan limas segiempat : {luasP}")
        elif pilih == 3: 
            run = 0

def kerucut(): 
    run = 1
    while run == 1: 
        pi = 22/7
        go = 1
        while go == 1:
            pilih = int(input("1. Volume\n2. Luas Permukaan\n3. Back to menu\nPilih : "))
            if pilih == 1: 
                s = float(input("Masukkan panjang garis pelukis : "))
                r = float(input("Masukkan panjang jari-jari alas : "))
                if s < r:
                    print("Maaf, garis pelukis harus lebih besar dari jari-jari")
                else :
                    t = (s * 2) - (r * 2)
                    tinggi = math.sqrt(t)
                    v = pi * (r ** 2) * tinggi / 3
                    print(f"volume kerucut : {v}")
                
            elif pilih == 2: 
                s = float(input("Masukkan panjang garis pelukis : "))
                r = float(input("Masukkan panjang jari-jari alas : "))
                l = pi * r * (r + s)
                print(f"Luas permukaan kerucut : {l}")

            elif pilih == 3: 
                go = 0
                run = 0

#  ---------------------------------------------------------------- Statistika ------------------------------------------------------------------
def statistika():   
    run = 1
    while run == 1: 
        pilih = int(input("1. Cari Mean, Median, dan Modus Data\n2. Back to menu\nPilih : "))
        if pilih == 1: 
            deret = input("Masukkan barisan bilangan (pisahkan dengan koma) : ")
            data = []

            for i in deret.split(","): 
                data.append(float(i))
            
            jmlh_data = sum(data)
            jmlh_Elemen = len(data)
            mean = jmlh_data / jmlh_Elemen

            tengah = len(data) / 2
            if tengah % 2 == 0: 
                tengah = int(len(data) / 2)
                index1 = tengah - 1
                median = data[tengah] + data[index1] / 2
            else : 
                tengah = int(len(data) / 2)
                median = data[tengah]
            
            modus = statistics.mode(data)

            print(f"Rata-rata barisan bilangan : {mean}")
            print(f"Median barisan bilangan : {median}")
            print(f"Modus barisan bilangan : {modus}")
        elif pilih == 2: 
            run = 0


# ------------------------------------------------------------- Sin Cos Tan --------------------------------------------------------------------
def SinCosTan(): 
    run = 1
    while run == 1: 
        pilih = int(input("1. Cari Sin, Cos, Tan\n2. Back to menu\nPilih : "))
        if pilih == 1: 
            sudut = float(input("Masukkan besar sudut : "))
            rad = math.radians(sudut)
            sin = math.sin(rad)
            cos = math.cos(rad)
            tan = math.cos(rad)
            print(f"Sinus {sudut} derajat adalah {sin}")
            print(f"Cosinus {sudut} derajat adalah {cos}")
            print(f"Tangen {sudut} derajat adalah {tan}")
        elif pilih == 2: 
            run = 0
#Fisika
def massaJenis():
    massaJenis = 0
    massa = float(input("Masukkan massa benda (kg) : "))
    volume = float(input("Masukkan volume benda (m^3) : "))
    massaJenis = massa/volume
    print(f"Massa jenis dari benda yang memiliki massa {massa} kg dan volume {volume} m^3 adalah {massaJenis} kg/m^3")

def gaya():
    gaya = 0
    massa = float(input("Masukkan massa benda (kg) : "))
    percepatan = float(input("Masukkan percepatan benda (m/s^2) : "))
    gaya = massa*percepatan
    print(f"Gaya dari benda yang memiliki massa {massa} kg dan percepatan {percepatan} m/s^2 adalah {gaya} newton")

def frekuensi():
    frekuensi = 0
    x = int(input("""1. Jumlah getaran dan waktu yang dibutuhkan untuk melakukan getaran\n
                  2. Kecepatan gelombang dan panjang gelombang\n
                  3. Periode\n
                  Pilih salah satu variabel yang sudah diketahui (atau ketik '0' apabila tidak ada satupun di atas dan ingin kembali) : """))
    if x == 0:
        return
    elif x == 1:
        jumlahGetaran = float(input("Masukkan jumlah getaran : "))
        waktuUntukBergetar = float(input("Masukkan waktu yang dibutuhkan untuk melakukan getaran (s) : "))
        frekuensi = jumlahGetaran/waktuUntukBergetar
        print(f"""Frekuensi gelombang dengan jumlah getaran {jumlahGetaran} dan 
              waktu yang dibutuhkan untuk melakukan getaran {waktuUntukBergetar} s adalah {frekuensi} Hz""")
    elif x == 2:
        kecepatanGelombang = float(input("Masukkan kecepatan gelombang (m/s) : "))
        panjangGelombang = float(input("Masukkan panjang gelombang (m) : "))
        frekuensi = kecepatanGelombang/panjangGelombang
        print(f"""Frekuensi gelombang dengan kecepatan gelombang {kecepatanGelombang} m/s dan 
              panjang gelombang {panjangGelombang} m adalah {frekuensi} Hz""")
    elif x == 3:
        periode = float(input("Masukkan periode (s) : "))
        frekuensi = 1/periode
        print(f"Frekuensi gelombang dengan periode {periode} s adalah {frekuensi} Hz")

def periode():
    periode = 0
    x = int(input("""1. Jumlah getaran dan waktu yang dibutuhkan untuk melakukan getaran\n
                  2. Kecepatan gelombang dan panjang gelombang\n
                  3. Frekuensi\n
                  Pilih salah satu variabel yang sudah diketahui (atau ketik '0' apabila tidak ada satupun di atas dan ingin kembali) : """))
    if x == 0:
        return
    elif x == 1:
        jumlahGetaran = float(input("Masukkan jumlah getaran : "))
        waktuUntukBergetar = float(input("Masukkan waktu yang dibutuhkan untuk melakukan getaran (s) : "))
        periode = waktuUntukBergetar/jumlahGetaran
        print(f"""Periode gelombang dengan jumlah getaran {jumlahGetaran} dan 
              waktu yang dibutuhkan untuk melakukan getaran {waktuUntukBergetar} s adalah {periode} s""")
    elif x == 2:
        kecepatanGelombang = float(input("Masukkan kecepatan gelombang (m/s) : "))
        panjangGelombang = float(input("Masukkan panjang gelombang (m) : "))
        periode = kecepatanGelombang*panjangGelombang
        print(f"""Periode gelombang dengan kecepatan gelombang {kecepatanGelombang} m/s dan 
              panjang gelombang {panjangGelombang} m adalah {periode} s""")
    elif x == 3:
        frekuensi = float(input("Masukkan frekuensi (Hz) : "))
        periode = 1/frekuensi
        print(f"Periode gelombang dengan frekuensi {frekuensi} Hz adalah {periode} s")

def kecepatanGelombang():
    kecepatanGelombang = 0
    x = int(input("""1. Jarak dan waktu yang dibutuhkan untuk melakukan getaran\n
                  2. Panjang gelombang dan frekuensi\n
                  3. Panjang gelombang dan periode\n
                  Pilih salah satu variabel yang sudah diketahui (atau ketik '0' apabila tidak ada satupun di atas dan ingin kembali) : """))
    if x == 0:
        return
    elif x == 1:
        jarak = float(input("Masukkan jarak (m) : "))
        waktuUntukBergetar = float(input("Masukkan waktu yang dibutuhkan untuk melakukan getaran (s) : "))
        kecepatanGelombang = jarak/waktuUntukBergetar
        print(f"""Kecepatan gelombang dengan jarak {jarak} m dan 
              waktu yang dibutuhkan untuk melakukan getaran {waktuUntukBergetar} s adalah {kecepatanGelombang} m/s""")
    elif x == 2:
        panjangGelombang = float(input("Masukkan panjang gelombang (m) : "))
        frekuensi = float(input("Masukkan frekuensi (Hz) : "))
        kecepatanGelombang = panjangGelombang*frekuensi
        print(f"Kecepatan gelombang dengan panjang gelombang {panjangGelombang} m dan frekuensi {frekuensi} Hz adalah {kecepatanGelombang} m/s")
    elif x == 3:
        panjangGelombang = float(input("Masukkan panjang gelombang (m) : "))
        periode = float(input("Masukkan periode (s) : "))
        kecepatanGelombang = panjangGelombang/periode
        print(f"Kecepatan gelombang dengan panjang gelombang {panjangGelombang} m dan periode {periode} s adalah {kecepatanGelombang} m/s")

def energi():
    x = int(input("1. Energi Potensial\n2. Energi Kinetik\nIngin mencari apa? "))
    if x == 1:
        gravitasiBumi = 9.8
        massa = float(input("Masukkan massa benda (kg) : "))
        tinggi = float(input("Masukkan tinggi benda (m) : "))
        ep = massa*gravitasiBumi*tinggi
        print(f"Energi potensial benda dengan massa {massa} kg dan tinggi {tinggi} m adalah {ep} joule")
    elif x == 2:
        massa = float(input("Masukkan massa benda (kg) : "))
        kecepatan = float(input("Masukkan kecepatan benda (m/s) : "))
        ek = 1/2(massa*kecepatan*kecepatan)
        print(f"Energi kinetik benda dengan massa {massa} kg dan kecepatan {kecepatan} m/s adalah {ek} joule")

def hukumOhm():
    x = int(input("Pilih yang ingin dicari : "))
    if x == 1:
        voltase = float(input("Masukkan nilai voltase (V): "))
        hambatan = float(input("Masukkan nilai hambatan (Ohm): "))
        arus = voltase / hambatan
        print(f"Arus dalam rangkaian: {arus} A")
    elif x == 2:
        arus = float(input("Masukkan nilai arus (A): "))
        hambatan = float(input("Masukkan nilai hambatan (Ohm): "))
        voltase = arus * hambatan
        print(f"Voltase dalam rangkaian: {voltase} V")
    elif x == 3:
        voltase = float(input("Masukkan nilai voltase (V): "))
        arus = float(input("Masukkan nilai arus (A): "))
        hambatan = voltase / arus
        print(f"Hambatan dalam rangkaian: {hambatan} Ohm")

def hukumKirchhoff():
    teganganSumber = float(input("Masukkan nilai tegangan sumber (V): "))
    jumlahMasuk = int(input("Masukkan jumlah arus masuk: "))
    arusMasuk = []
    for i in range(jumlahMasuk):
        arus = float(input(f"Masukkan nilai arus masuk {i+1} (A): "))
        arusMasuk.append(arus)
    jumlahKeluar = int(input("Masukkan jumlah arus keluar: "))
    arusKeluar = []
    for i in range(jumlahKeluar):
        arus = float(input(f"Masukkan nilai arus keluar {i+1} (A): "))
        arusKeluar.append(arus)
    teganganJatuh = teganganSumber - sum(arusMasuk) + sum(arusKeluar)
    print(f"Tegangan jatuh dalam rangkaian: {teganganJatuh} V")

def hambatanPengganti():
    jumlahHambatan = int(input("Masukkan jumlah hambatan: "))
    hambatan = []
    for i in range(jumlahHambatan):
        nilaiHambatan = float(input(f"Masukkan nilai hambatan {i+1} (Ohm): "))
        hambatan.append(nilaiHambatan)
    tipeRangkaian = int(input("1. Seri\n2. Paralel\nMasukkan tipe rangkaian : "))
    if tipeRangkaian == 1:
        totalHambatan = sum(hambatan)
    elif tipeRangkaian == 2:
        totalHambatan = 1 / sum(1 / hambatan)
    print(f"Hambatan pengganti dalam rangkaian: {totalHambatan} Ohm")

#-------------------------------------------------------------- Main -----------------------------------------------------------------

print("Selamat Datang Di Program Kami")
while True:  
    choice = int(input("\n1. Matematika\n2. Fisika\n3. Keluar program\nSilahkan pilih bidang ilmu : "))
    if choice == 1:
        material = 1
        while material == 1: 
            getMath = int(input("""\n1. Aritmatika
                                \n2. Bangun Datar
                                \n3. Bangun Ruang
                                \n4. Statistika
                                \n5. Cari Sin, Cos, Tan
                                \n6. Menu Utama
                                \nPilih materi : """))
            if getMath == 1:
                run = 1
                while run == 1:
                    materi = int(input("\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Deret Aritmatika\n6. Pilih materi\nPilih : "))
                    if materi == 1: 
                        penjumlahan()
                    elif materi == 2: 
                        pengurangan()
                    elif materi == 3:
                        perkalian()
                    elif materi == 4: 
                        pembagian()
                    elif materi == 5: 
                        stat = 1
                        while stat == 1: 
                            pilih = int(input("1. Cari jumlah suku ke-n\n2. Cari jumlah n suku pertama\n3. Back to menu\nPilih : "))
                            if pilih == 1:
                                Un()
                            elif pilih == 2: 
                                Sn()
                            elif pilih == 3:
                                stat = 0
                    elif materi == 6: 
                        run = 0
            elif getMath == 2:
                run = 1
                while run == 1: 
                    bangunDatar = int(input("""\n1. Persegi
                                            \n2. Persegi Panjang
                                            \n3. Segitiga
                                            \n4. Lingkaran
                                            \n5. Trapesium
                                            \n6. Jajar Genjang
                                            \n7. Belah Ketupat
                                            \n8. Layang-Layang
                                            \n9. Pilih Materi
                                            \nPilih : """))
                    if bangunDatar == 1: 
                        persegi()
                    elif bangunDatar == 2:
                        persegiPanjang()
                    elif bangunDatar == 3:
                        segitiga = 1
                        while segitiga == 1: 
                            jenisSegitiga = int(input("1. Sama Sisi\n2. Sama kaki\n3. Sama Sembarang\n4. Back to menu\nPilih : "))
                            if jenisSegitiga == 1:
                                sSamaSisi()
                            elif jenisSegitiga == 2 : 
                                sSamaKaki()
                            elif jenisSegitiga == 3:
                                sSembarang()
                            elif jenisSegitiga == 4: 
                                segitiga = 0
                    elif bangunDatar == 4:
                        lingkaran()
                    elif bangunDatar == 5: 
                        trapesium()
                    elif bangunDatar == 6:
                        jajarGenjang()
                    elif bangunDatar == 7:
                        belahKetupat()
                    elif bangunDatar == 8: 
                        layangLayang()
                    elif bangunDatar == 9: 
                        run = 0
            elif getMath == 3: 
                run = 1
                while run == 1:
                    pilih = int(input("\n1. Kubus\n2. Balok\n3. Tabung\n4. Prisma\n5. Limas\n6. Kerucut\n7. Pilih Materi\nPilih : "))
                    if pilih == 1: 
                        kubus()
                    elif pilih == 2: 
                        balok()
                    elif pilih == 3: 
                        tabung()
                    elif pilih == 4: 
                        prisma = 1
                        while prisma == 1: 
                            jenisPrisma = int(input("1. Prisma Segitiga Sama Sisi\n2. Prisma Segiempat\n3.Back to menu\nPilih : "))
                            if jenisPrisma == 1:
                                prismaSegitiga() 
                            elif jenisPrisma == 2: 
                                prismaPersegi()
                            elif jenisPrisma == 3: 
                                prisma = 0
                    elif pilih == 5: 
                        limas = 1
                        while limas == 1: 
                            jenisPrisma = int(input("1. Limas Segitiga Sama Sisi\n2. Limas Segiempat\n3. Back to menu\nPilih : "))
                            if jenisPrisma == 1: 
                                limasSamaSisi()
                            elif jenisPrisma == 2: 
                                limasSegiempat()
                            elif jenisPrisma == 3: 
                                limas = 0
                    elif pilih == 6: 
                        kerucut()
                    elif pilih == 7: 
                        run = 0
            elif getMath == 4 : 
                statistika()
            elif getMath == 5 : 
                SinCosTan()
            elif getMath == 6:
                material = 0

    elif choice == 2:
        material = 1
        while material == 1: 
            getPhysics = int(input("\n1. Massa Jenis\n2. Gaya\n3. Gelombang\n4. Energi\n5. Rangkaian Listrik\n6. Menu Utama\nPilih materi : "))
            if getPhysics == 1:
                massaJenis()
            elif getPhysics == 2:
                gaya()
            elif getPhysics == 3: 
                run = 1
                while run == 1:
                    pilih = int(input("\n1. Frekuensi Gelombang\n2. Periode Gelombang\n3. Kecepatan Gelombang\n4. Pilih Materi\nPilih : "))
                    if pilih == 1: 
                        frekuensi()
                    elif pilih == 2: 
                        periode()
                    elif pilih == 3: 
                        kecepatanGelombang()
                    elif pilih == 4: 
                        run = 0
            elif getPhysics == 4:
                energi()
            elif getPhysics == 5:
                run = 1
                while run == 1:
                    pilih = int(input("\n1. Hukum Ohm\n2. Hukum Kirchhoff\n3. Hambatan Pengganti\n4. Pilih Materi\nPilih : "))
                    if pilih == 1: 
                        hukumOhm()
                    elif pilih == 2: 
                        hukumKirchhoff()
                    elif pilih == 3: 
                        hambatanPengganti()
                    elif pilih == 4: 
                        run = 0
            elif getPhysics == 6:
                material = 0

    elif choice == 3: 
        print("Terimakasih")
        break
