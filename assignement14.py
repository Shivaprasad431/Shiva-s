n=int(input())
lst=[i for i in range(1,n+1)]
print(lst)
n=int(input())
lst=[i for i in range(n+1) if i%2!=0]
print(lst)
n=int(input())
lst=[i for i in range(n+1) if i%2==0]
print(lst)
n=int(input("Enter the no of elements"))
lst=[int(input(f"enter the {i+1} element")) for i in range(n+1)]
print(max(lst))
n=int(input("Enter the no of elements"))
lst=[int(input(f"enter the {i+1} element")) for i in range(n+1)]
print(min(lst))
n=int(input("Enter the no of elements"))
lst=[int(input(f"enter the {i+1} element")) for i in range(n+1)]
print(sum(lst))
lst=[1,'a','b',2,3,4,5]
print(lst)
res=[i for i in lst if  isinstance(i,int)]
print(res)
lst=[1,2,3,3,3,3,4,4,4,5,6,7,7,8,8,9]
for i in lst:
 print(f" count of {i} is {lst.count(i)}")
lst=[1,2,3,3,3,3,4,4,4,5,6,7,7,8,8,9]
for i in range(len(lst)):
    print(f"the index of {lst[i] } is {i+1}")
lst=[1,2,3,3,3,3,4,4,4,5,6,7,7,8,8,9]
lst.sort(reverse=True)
print(lst)