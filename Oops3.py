#del Key word example - 
"""class student:
    def __init__(self, name):
    self.name = name

s1 = student("shouvk")
print(s1.name)
del s1.name
print(s1.name)
"""
# -  change the attribute - 

"""class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
        
    def reset_pass(self):
        print(self.__acc_pass)
        
acc1 = Account("12345","abcd")
print(acc1.acc_no)
print(acc1.reset_pass())

"""

#Inheritance method example -- 

"""class car:
    color =  "blue"
    @staticmethod
    def start():
        print("Car started")
        
    @staticmethod
    def stop():
        print("car stopped")
        
class TATACar(car):
    def __init__(self,name):
        self.name = name 
        
car1 = TATACar("safari")
car2 = TATACar("harir")

print(car1.name)
print(car1.start()) 
print(car1.color)
"""

#Multi -level inheritance 
"""class car:
    color =  "blue"
    @staticmethod
    def start():
        print("Car started")
        
    @staticmethod
    def stop():
        print("car stopped")
        
class TATACar(car):
    def __init__(self,name):
        self.brand = brand 
  
  
class Indigo(TATACar):
      def __init__(self, type): 
        self.type= type
      
      
car1 = Indigo("petrol")
car1.start()"""

# car1 = TATACar("safari")---
# car2 = TATACar("harir")

# print(car1.name)
# print(car1.start()) 
# print(car1.color)=----

"""#Multiple Inheritence 

class A:
    varA="welcome to class A"
    
class B:
    varB = "Welcome to calss B"
    
class C(A,B):
    varC=" Welcome to class C  "
c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

"""

"""#Super method ----
class car:
    def __init__(self, type): 
        self.type= type
        

    color =  "blue"
    @staticmethod
    def start():
        print("Car started")
        
    @staticmethod
    def stop():
        print("car stopped")
        
class TATACar(car):
    def __init__(self,name,type):
        self.name = name
        '''self.type = type'''# this line is not work
        super().__init__(type) #Paretn code  theke code inherient kora  
        super().start()
car1 = TATACar("Harir","petrol")
print(car1.type)
 """

"""#class method1 ---
class Person:
    name = "anonynomous"

    def changeName(self,name):
        Person.name = name
 
p1 = Person()
p1.changeName("shouvik")
print(p1.name)
print(Person.name)
"""
"""#class method2---
class Person:
    name = "anonynomous"

    def changeName(self,name):
        self.__class__.name = "Rahul"  #<-person class
        'Person.name = name'
 
p1 = Person()
p1.changeName("shouvik")
print(p1.name)
print(Person.name)
"""

"""
#Class method Actural
class Person:
    name = "anonynomous"

    #def changeName(self,name):
     #   self.__class__.name = "Rahul"  #<-person class
      #  'Person.name = name'
 
    @classmethod
    def changeName(cls, name):
         cls.name = name
p1 = Person()
p1.changeName("shouvik")
print(p1.name)
print(Person.name)

"""

"""#Property Decorators2---------
class student:
    def __init__(self, phy,chem,math):
         self.phy = phy
         self.math = math
         self.chem = chem
         #self.Percentage = str ((self.phy+self.math +self.chem)/3) + "%"      

            #def calcPercentage(self):
                #   self.Percentage
     
    @property
    def Percentage(self):
         return str ((self.phy+self.math +self.chem)/3) + "%"
     
     
     
     
stu1 = student(98,96,98)
print(stu1.Percentage)

stu1.phy = 92
#print(stu1.Percentage)
#stu1.calcPercentage()

print(stu1.Percentage)"""

# Polymosphisam ---------------

"""
class complex:
    def __init__(self,real,img):
        self.real= real
        self.img = img
        
    def shownumber(self):
        print(self.real,"i+",self.img"j")
        
    def add(self,num1,num2):
        numreal = self.real+num2.real
        numimg = self.img +num2.img
        return complex(numreal,numimg)

num1 = complex(2,3)
num1.shownumber()

num2 = complex(4,7)
num2.shownumber()
num3 = num1.add(num2)
num3.shownumber()



""" 

class order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
        

    def __gt__(self, ord2):
        return self.price >ord2.price


ord1 = order("popcorn",20)
ord2 = order("coco",30)

print(ord1>ord2) #if ture then








