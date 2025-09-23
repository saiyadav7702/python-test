a=int(input("enter your birth year"))
r=int(input("enter your present year"))
t=int(input("enter your present month"))
b=int(input("enter your birth month"))
c=int(input("enter your birth day"))
u=int(input("enter your present day"))
years=r-a
months=12-b+t 
days=c
print (years, abs(months), days)