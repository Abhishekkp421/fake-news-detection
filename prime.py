s=input("enter a number")
n=int(s)
isPrime=True
for i in range (2,n):
    if n%i==0:
        print("not a prime number")
        isPrime=False
        break
if isPrime:
    print("prime number")