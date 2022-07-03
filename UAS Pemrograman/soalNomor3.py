data = []
x = 0
while True:
    user = input("Masukkan Angka : ")
    if user == 'n':
        break
    x += 1
    data.append(user)

Ratarata = 0
for nilai in data:
    Ratarata += int(nilai)
Ratarata /= x
print(Ratarata)
