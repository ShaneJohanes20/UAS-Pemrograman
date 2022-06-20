def fib (n):
    if n == 0:
        return 0

     elif n == 1:
   return 1

    else:
   hasil = fib(n-1) + fib(n-2)
   return hasil
 
print(fib(5))
