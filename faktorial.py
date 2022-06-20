def faktorial(n) :
    print(f'menghitung faktorial {n}')
 if n == 1:
print('nilai balik 1, iterasi berakhir')
   return 1
 else:
   hasil = faktorial(n-1)
   print(f'return {n} dikalikan dengan fungsi faktorial({n-1}) = {hasil}')
   return n * hasil
print (faktorial(10))