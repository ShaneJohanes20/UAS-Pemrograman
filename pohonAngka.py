from math import inf as infinity
 
pohonAngka = [5, [10,8], [20, [255,40,45], [300, 23,34]]]
 
def angkaTerbesar(pohon, terbesar=-infinity):
 if isinstance(pohon, list) :
   terbesarInLoop = 0
   for angka in pohon :
     hasil = angkaTerbesar(angka, terbesar)
     if(hasil > terbesarInLoop) :
      terbesarInLoop = hasil
   return terbesarInLoop   
 else :
   if(pohon > terbesar) :
     return pohon
   else :
     return terbesar
 
print(angkaTerbesar(pohonAngka))