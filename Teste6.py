num = 5
def recur_factorial(n):
   if n == 1:
       return n
   elif n < 1:
       return ("NA")
   else:
       return n*recur_factorial(n-1)

print (recur_factorial(int(num)))