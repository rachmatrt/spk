nomor1 = 1
nomor2 = 2
nama = "Rachmat"
if nomor2 > nomor1 and nama == "Rachmat":
	print("nomor 2 lebih dari nomor 1")
elif nomor2 > nomor1 and nama != "Rachmat":
	print("nomor 1 lebih dari nomor 2")
else:
	print("lainnya")

for i in range(0,5): 
	print(i)
print("=================")
arrdata = [3,4,5,6] #arrray
for i in arrdata:
	print(i)
print("=================")
arrdatajson = [{'nama':'rachmat','kelas':9},{'nama':'risanto','kelas':8},{'nama':'tiesa','kelas':7}]

for i in arrdatajson: #mulai dr 0
	print(i["nama"])
print("=================")
for i in range(1,len(arrdatajson)): #mulai dari 1
	print(arrdatajson[i]["nama"])

def kelas():
	print("=================")
	for i in range(0,len(arrdatajson)): #mulai dari 0
		print(arrdatajson[i]["kelas"])
kelas()
