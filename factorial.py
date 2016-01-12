#1 method
#factorial program
def fact(n):
     if(n==1):
        return 1;
     else:
        return n*fact(n-1);
        
print fact(9)

#2 method
def factorial(n):
     if n == 0:
         return 1
     else:
         return n * factorial(n-1)
         
print factorial(4)

#3 method
#Lazy Python programmer
def fact1(x):
     return x > 1 and x * fact1(x - 1) or 1
print fact1(6)


#4 method
#Lazier Python programmer
f = lambda x: x and x * f(x - 1) or 1
print f(6)
