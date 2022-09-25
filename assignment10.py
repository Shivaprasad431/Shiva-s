for i in range(1,11):
    print(i*5)
n=int(input("enter the range"))
for i in range(n+1):
    print(i*10)
n=int(input("enter the multiplier"))
m=int(input("enter the multiple"))
for i in range(m+1):
    print(n*i)
n=int(input("enter the range of 10 multiples"))
lst=[]
for i in range(1,11):
    a=10*i
    lst.append(a)
lst.sort(reverse=True)
for i in lst:
    print(i)  
m=int(input("enter a number you want to know the table"))
for i in range (1,11):
    print(i*m)
n=int(input("enter the numbers "))
for i in range (1,n+1):
    if i%2==0:
     print(i)
n=int(input("enter the numbers "))
for i in range(1,n+1):
    if i%2!=0:
      print(i)
n=int(input("entee the range"))
for i in range(0,n+1):
    print(i**2)
n=int(input("enter the range"))
for i in range(0,n+1):
    print(i**3)
start=15
end=45
for i in range(start,end+1):
    if (i>1):
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)
