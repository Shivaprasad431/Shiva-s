class Properties:
  name='Shiva prasad'
  age=21
  email="shivakoyyada431@gmail.com"
class user:
    x=("Hey programmer welcome to programming world")
programmer=user()
print(programmer.x)    
class objects:
  a=20
  b=40
shiva=objects() 
print(shiva.a)
class creator:
   def __init__(self,name,age):
         self.name=name
         self.age=age
   def del_delte(self):
     del self.age
creator_name=creator("Manjula Koyyada", 21)
print(creator_name.name)
print(creator_name.del_delte())
class laptop:
  def __init__(self,brand,ram,cpu,hdd):
    self.brand=brand
    self.ram=ram
    self.cpu=cpu
    self.hdd=hdd
  def showConfig(self):
    return f"laptop is {self.brand},ram is {self.ram},cpu is {self.cpu}  and hdd is {self.hdd}"
laptop1=laptop("dell","8","ryzen 3","256")
laptop2=laptop("lenovo","32","ryzen 3","256")
laptop3=laptop("hp","16","ryzen 3","256")
l1=[laptop1.ram,laptop2.ram,laptop3.ram]
l2=[]
for e in l1:
  l2.append(int(e))
l3=l2.sort()  
print(laptop1.showConfig())    
print(l2)
class youngest:
  def __init__(self,user1,user2,user3):
    self.user1=user1
    self.user2=user2
    self.user3=user3
  def resultyoungest(self):
      lst=[self.user1,self.user2,self.user3]
      a=min(lst)
      return f"the youngest is {a}"
ages=youngest(20, 28, 52) 
print(ages.resultyoungest())     
class School_class:
  schoolname="Kakatiya University"
  def __init__(self,name,branch,year):
    self.name=name
    self.branch=branch
    self.year=year
 
  def show_details(self):
    return f"your name is {self.name},branch is {self.branch} , year is {self.year} and the college is {self.schoolname}"
student=School_class("Shiva Prasad", "ECE", 3)
print(student.show_details())
class Employee:
  def __init__(self,empid,name,salary):
    self.empid=empid
    self.name=name
    self.salary=salary
  def return_details(self):
    return f"your id is {self.empid},your name is {self.name} and the salary is {self.salary}"
empid=input("enter your id")
name=input("enter your name")
salary=int(input("enter your salary"))
employee1=Employee(empid, name, salary)
print(employee1.return_details())