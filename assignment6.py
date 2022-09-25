a=int(input("enter a number"))
if a<0:
    print("negative number")
else:
    print("postive")
if a%5==0:
    print("yes divisible by 5")   
else:
    print("no it si snot divisible by 5")
x=int(input("enter a first number"))
y=int(input("enter a second number"))
if x>y:
    print("first nbr is greater")
elif x==y:
    print("both are equal",x)
else:
    print("both are not equal")
m=input("enter a letter")
s=input("enter another letter")
if m>s:
    print("dictionary order is",s,m)
else:
    print("correct order is",m,s)
c=input("enter a theree digit number")
if len(c)==3:
    print("yes itis a 3 digit number")
else:
    print("it is not")
v=int(input("enter a number"))
if v<0:
    print("negative number")
elif v==0:
    print("its zero")
else:
    print("postive")
b=int(input("enter the value of determinant of quadratic equation"))
if b>0:
    print("it has real and disinct roots")
elif b==0:
    print("real and equal roots")
else:
    print("inaginary roots")
d=int(input("enter a year number"))
if d%4==0:
    print("yes , it is a leap year")
else:
    print("it is not leap year")
e=int(input("enter a month number"))
if e%2==0:
    print("30 days")
else:
    print("31 days")
k=complex(input("enter a comples number"))
if real(k)>img(k):
    print("yes imga and real parts are equal")
else:
    print("not equal")
