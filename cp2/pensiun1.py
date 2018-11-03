nama = input("masukkan nama anda : ")
tahunlahir = input("masukkan tahun lahir anda : ")
umur = 2018 - int(tahunlahir)

if umur >= 55:
	usia = "0"
elif umur <= 18:
	usia = "2"
else:
	usia = "1"

if umur >= 60:
	batas = "1"
else:
	batas = "0"

selusia = ['tua','muda','pelajar']
selpensiun = ['belum penisun','pensiun dini','pensiun']
selsakit = ['tidak ada','ringan','berat']
selyesno = ['tidak','ya']

print ("Kategori sakit")
for i in range(0,len(selsakit)):
	print(i,selsakit[i])

katsakit = input('Masukkan angka :' )
sakit = katsakit

print ("Kategori Kehidupan")
for i in range(0,len(selyesno)):
	print(i,selyesno[i])

kathidup = input('Masukkan angka :')
hidup = kathidup

import csv
data = open('pensiun1.csv','r')
baca = csv.reader(data)
tabel = []
for i in baca:
	tabel.append(i)

for i in range(0,len(tabel)):
	if tabel[i][0] == usia:
		if tabel[i][1] == batas:
			if tabel[i][2] == sakit:
				if tabel[i][3] == hidup:
					print("Nama Anda: ",nama)
					print("Umur Anda : ",umur)
					print("kategori Usia :",usia,selusia[int(usia)])
					print("Batas :", batas,selyesno[int(batas)])
					print("kategori sakit :",sakit,selsakit[int(sakit)])
					print("Status Kehidupan :",hidup,selyesno[int(hidup)])
					print("anda dinyatakan : ",tabel[i][4],selpensiun[int(tabel[i][4])])
