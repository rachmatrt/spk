print("======================================== CAPAIAN EVALUASI 1 ===================================================")
rambu = [
	{"lampu": 1, "value":""},
	{"lampu": 2, "value":""},
	{"lampu": 3, "value":""},
	{"lampu": 4, "value":""},
]

nyala = 3

for i in range(0,len(rambu)):
	if rambu[i]["lampu"] == nyala :
		rambu[i]["value"] = "hijau"
	else:
		rambu[i]["value"] = "merah"

print(rambu)

print("===============================================================================================================")

arrjalan = [
	{"dari" : "0", "ke" : "1", "jarak" : 13},
	{"dari" : "0", "ke" : "2", "jarak" : 4},
	{"dari" : "1", "ke" : "3", "jarak" : 6},
	{"dari" : "1", "ke" : "2", "jarak" : 2},
	{"dari" : "2", "ke" : "4", "jarak" : 1},
	{"dari" : "3", "ke" : "5", "jarak" : 5},
	{"dari" : "4", "ke" : "3", "jarak" : 5},
	{"dari" : "4", "ke" : "5", "jarak" : 13},
]

jalan = ""
hasil = ""
counter = 0
JarakTotal = 0
Ditempuh = 0

for i in range(0,len(arrjalan)):
	#dimulai dari 0
	if arrjalan[i]["dari"] == "0": 
		print("\n data ke- ",i)
		for y in range(i,len(arrjalan)): 
		#data pertama
			if arrjalan[i]["dari"] == "0" and counter == 0 :
				hasil = "{} ---> {}".format(arrjalan[i]["dari"],arrjalan[i]["ke"])
				jalan = arrjalan[i]["ke"]
				counter += 1
				JarakTotal = arrjalan[y]["jarak"]
			elif jalan == arrjalan[y]["dari"] and arrjalan[y]["dari"] < arrjalan[y]["ke"]:
				jalan = arrjalan[y]["ke"]
				hasil += " ---> {}".format(arrjalan[y]["ke"])
				JarakTotal += arrjalan[y]["jarak"]
				if jalan == "5":
					print (" Jalur yang Dipilih = ", hasil , "\n dengan Jarak Total = ", JarakTotal , "KM")
					Ditempuh = JarakTotal

	jalan = ""
	counter = 0
	if JarakTotal <= Ditempuh:
		Ditempuh = JarakTotal
	else:
		JarakTotal = 0

print ("\n Jarak Terpendek adalah ", Ditempuh, "KM")