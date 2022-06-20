hitung = 0

while hitung < 20 :
   hitung += 1
   print(hitung)
   
   data = []

while len(data) < 6 :
   inputUser = input("masukkan angka: ")
   data.append(int(inputUser))

print(data)

data = []

while len(data) < 6 :
   inputUser = input("masukkan angka: ")
   if int(inputUser) % 2 == 0 :
       break
   data.append(int(inputUser))

print(data)

data = []

while len(data) < 6 :
   inputUser = input("masukkan angka: ")
   if int(inputUser) % 2 == 0 :
       continue
   data.append(int(inputUser))

print(data)