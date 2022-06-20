data = [["42130108", "SHANE JOHANES WELAN", "TEKNOLOGI INFORMASI"], ["1211323028", "JOSE PEDROS", "MANAJEMEN"],
        ["82130284", "GEDE INDRA MAHESWARA", "ILMU KOMUNIKASI"]]
x = 0
print("SILAHKAN PILIH NAMA MAHASISWA BERIKUT : ")
for i in data:
    print(f"{x+1}. {data[x][1]}")
    x = x + 1

user = int(input("Pilihan anda : "))

if user == 1:
    print(data[0])
elif user == 2:
    print(data[1])
elif user == 3:
    print(data[2])
