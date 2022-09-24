x=int(input())
print("postive" if x>0 else "Negative")
print("yes" if x%5==0 else "NO")
print("even" if x%2==0 else "ODD")
a,b=map(int,input().split())
print(a if a>=b else b)
a,b=input().split()
if a>b:
    print(b,a)
else:
    print(a,b)
