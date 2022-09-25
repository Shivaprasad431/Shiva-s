lst=[]
n=int(input("enter the range"))
for i in range(n+1):
      lst.append(i)
print("sum of n natural numbers is ",sum(lst))   
count=0
m=int(input("enter the range"))   
for i in range(m+1):
    count=count+(i**2)
print("sum of squares is",count)
count=0
m=int(input("enter the range"))   
for i in range(m+1):
    count=count+(i**3)
print("sum of the cubes is",count)
count=0
m=int(input("enter the range"))   
for i in range(m+1):
    if i%2!=0:
     count=count+(i)
print("sum of the cubes is",count)
count=0
m=int(input("enter the range"))   
for i in range(m+1):
    if i%2==0:
     count=count+(i)
print("sum of the cubes is",count)
factorial=1
m=int(input("enter the range"))
for i in range(1,m+1):
    factorial=factorial*i
print(f"factorial of {m} is {factorial}")
count=0
m=input("enter a number")
for i in m:
    count=count+1
print("digits count in given nbr is",count)
count=[]
m=(input("enter a number"))
for i in m:
    count.append(int(i))
print("sum of digits in given nbr is",sum(count))
#get input and initialize variables
decimal = int(input("Enter a decimal number \n"))
binary = 0
ctr = 0
temp = decimal 
while(temp > 0):
    binary = ((temp%2)*(10**ctr)) + binary
    temp = int(temp/2)
    ctr += 1     
print("Binary of {x} is: {y}".format(x=decimal,y=binary))
decimal = int(input("Enter a decimal number :"))

print("The octal equivalent is :",decimal_to_octal(decimal))

def decimal_to_octal(decimal):
    octal = 0
    i = 1
    while (decimal != 0):
        octal = octal + (decimal % 8) * i
        decimal = int(decimal / 8)
        i = i * 10
    return octal