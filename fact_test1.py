def factorial(n):
     if n == 0:
         return 1
     else:
         return n * factorial(n-1)
         
print factorial(4)

#Lazy Python programmer
def fact(x):
     return x > 1 and x * fact(x - 1) or 1
print fact(6)


#Lazier Python programmer
f = lambda x: x and x * f(x - 1) or 1
print f(6)