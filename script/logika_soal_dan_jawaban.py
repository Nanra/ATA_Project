import time
import sys

print "*" * 50

# TODO Bagian Deklarasi
kunci = ["A", "B", "C"]
urut = ["PERTAMA", "KEDUA", "KETIGA"]
soal = ["Apa nama Ibukota Indonesia ? \n A. Jakarta \n B. Bandung \n C. Medan \n D. Batam", "Apa Nama Ibukota Provinsi Jawa Barat ? \n A. Jakarta \n B. Bandung \n C. Medan \n D. Batam", "Apa nama Ibukota Provinsi Sumatera Utara ? \n A. Jakarta \n B. Bandung \n C. Medan \n D. Batam"]
benar = 0
salah = 0
catatan = ""
i = 0
jwb = []

while i < len(soal):
    # TODO Bagian Mengisi Jawaban
    print soal[i]
    jawaban = raw_input(" \nMasukkan Jawaban : ")
    i += 1
    jwb.append(jawaban)
    print "*" * 50
    print "\n"

print " \nJawaban anda adalah : "

n = 0

for n in range(i):
    # TODO Bagian Menguji Jawaban
    if jwb[n] == kunci[n]:
        print "Jawaban ", urut[n], " BENAR"
        benar += 1
    else:
        print "Jawaban ", urut[n], " SALAH"
        salah += 1

if benar == 3:
    catatan = "Anda Luar Biasa"
elif benar == 2:
    catatan = "Cukup"
elif benar == 1:
    catatan = "Buruk"
else:
    catatan = "Anda belum Lulus"

# TODO Bagian Menampilkan Result
print "\nHasil Keseluruhan :"
print "Jumlah Jawaban Benar = ", benar
print "Jumlah Jawaban Salah = ", salah
print "Catatan Pencapaian : ", catatan
print "*" * 50
raw_input("Tekan ENTER untuk keluar ....")
