# class student:
#     name="shouvik","anik"
    
# s1=student()
# print(s1)
# print(s1.name)


# class car:
#     color = "blue"
#     brand ="tata"
    
# car1 =car()
# print(car1.color)
# print(car1.brand)

#_ _init_ _ funtion------
# class student:
    
#     name="shouvik","anik"
#     def __init__(self):  //default constructor //
#         print(self)
#         print("adding new studnet data base:")


# s1=student()
# print(s1)
# print(s1.name)

# 2nd ----
# class student:
    
    
#     def __init__(self,fullname,marks):   //Parameterized constructor//
#         self.name = fullname
#         self.marks = marks
#         print("adding new studnet data base:")


# s1=student("shouvik",98)
# print(s1.name,s1.marks)
# s2=student("Anik",99)
# print(s2.name,s2.marks)
# ----------------------------------------------------------
# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks


#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name,"your scroe is: ", sum/3)

# s1= student("Shoucvik Naskar",[98,94,97])

# s1.get_avg()

# s1.name = "Anik"# If we  directly change the name of shouvik to anik then  dot this.

# s1.get_avg()


#----------------------------------------------------------------------------