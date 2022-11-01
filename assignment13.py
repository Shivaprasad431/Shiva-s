items=["Java","SQL","C"]
print(type(items))
mylist = ["Java", "C", "Python"]
print(mylist.pop())
thislist = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]
for i in range( len(thislist) ):
    if thislist[i]=="SQL":
       thislist.pop(i)
       thislist.insert(i,"NOSQL")
for i in range( len(thislist) ):
   if thislist[i]=="Reactnative":
    thislist.pop(i)
    thislist.insert(i,"Flutter")
print(thislist)
mylist =["Java", "SQL", "C", "Reactnative"]
mylist.append("python")
print(mylist)
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
for i in secondlist:
    firstlist.append(i)
print(firstlist)
thislist =["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
for i in range (len(thislist)):
    print("ïndex is", i , "and element is",thislist[i])
thislist = ["Java", "SQL",
"C", "Reactjs", "Javascript", "Python"]
print(sorted(thislist))
n=int((input("Enter the list range")))
lst=[]
for i in range(n):
    x=input(f"Enter the city you want to enter in {i} position")
    lst.append(x)
print("List You Entered cities are  ", lst)
map=list(map(str,input().split()))
print(map)