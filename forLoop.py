data = [
   {'nama' : 'mahasiswa 1', 'nim': '1812831203', 'aktif': True},
   {'nama' : 'mahasiswa 2', 'nim': '1813452345', 'aktif': True},
   {'nama' : 'mahasiswa 3', 'nim': '1812452345', 'aktif': False},
   {'nama' : 'mahasiswa 4', 'nim': '1816523452', 'aktif': False},
   {'nama' : 'mahasiswa 5', 'nim': '1814563454', 'aktif': True}
]


for i in data :
   print(f"nim: {i['nim']}")
   print(f"nama: {i['nama']}")
   print("=" * 100)
   if i['aktif'] == False :
       break
data = [
   {'nama' : 'mahasiswa 1', 'nim': '1812831203', 'aktif': True},
   {'nama' : 'mahasiswa 2', 'nim': '1813452345', 'aktif': True},
   {'nama' : 'mahasiswa 3', 'nim': '1812452345', 'aktif': False},
   {'nama' : 'mahasiswa 4', 'nim': '1816523452', 'aktif': False},
   {'nama' : 'mahasiswa 5', 'nim': '1814563454', 'aktif': True}
]

for i in data :
   if i['aktif'] == False :
       continue
   print(f"nim: {i['nim']}")
   print(f"nama: {i['nama']}")
   print("="*100)
data = [
   {'nama' : 'mahasiswa 1', 'nim': '1812831203', 'aktif': True},
   {'nama' : 'mahasiswa 2', 'nim': '1813452345', 'aktif': True},
   {'nama' : 'mahasiswa 3', 'nim': '1812452345', 'aktif': False},
   {'nama' : 'mahasiswa 4', 'nim': '1816523452', 'aktif': False},
   {'nama' : 'mahasiswa 5', 'nim': '1814563454', 'aktif': True}
]

for i in data :
   print(f"nim: {i['nim']}")
   print(f"nama: {i['nama']}")
   print("=" * 100)
   if i['aktif'] == False :
       continue