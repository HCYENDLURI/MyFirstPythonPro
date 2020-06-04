def Fn(n):
   if n <= 1:
       return n
   else:
       return(Fn(n-1) + Fn(n-2))

# take input from the user
n = int(input("Enter a Number: "))

# check if the number is valid
if n <= 0:
   print("Invalid")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(Fn(i))
