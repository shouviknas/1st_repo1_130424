# g = open("demo.txt","r")
# data = g.read()
# print(data)
# print(type(data))

# g.close() 


#No of charecter read-----
# g = open("demo.txt","r")
# data = g.read(7)
# print(data)

# g.close() 


# g = open("demo.txt","r")
# data = g.readline()
# print(data)

# g.close() 


#------------------------ -
# g = open("demo.txt","r")
# data = g.read(7)
# print(data)

# line = g.readline()
# print(line)

# g.close() 
#-----------------------
#re-write the multiple line of code -  code
# g = open("demo2.txt","w")
# g.write("I want to change the script")
# g.write("\n this is for next line")
# g.close()



# Create a file which is not create priviously but create  using this line
# z = open("samplefile.txt","w")
# z.close()

# x = open("samplefile2.txt","a")
# x.close()



# with sytex --------

# with open("demo4.txt","r") as k:
#     data=k.read()
# print(data)

# with open("demo4.txt","w")as l:
#     l.write("\n new data")

#delete a file

# import os
# os.remove("demo4.txt")

# with open("practice.txt","w") as t:
#     t.write("Hi Everyone")
#     t.write("\n we are learning file I\O")
#     t.write("\n using java")
#     t.write("\n i like programming in java")
#     data = t.read()
#     print(data)
#     t.close()

#--------
# with open("practice.txt","r") as t:
#        data = t.read()

# new_data = data.replace("java", "python")
# print(new_data)
   
# with open("practice.txt","w") as t:
#     t.write(new_data)


# with open("practice.txt","r") as t:
#     word = "code"
#     data = t.read()
#     if(data.find(word)!= -1 ):
#         print("data found")
#     else:
#         print("not found")
# # 
# with open("practice.txt","r") as t:
#     word = "code "
#     data = t.read()
#     if(data.find(word)!= 0 ):
#         print("data found")
#     else:
#         print("not found")


#COnvert to a function
# def check_forword():
#     word = "code "
#     with open("practice.txt","r") as t:
#         data = t.read()
#         if(data.find(word)!= -1 ):
#                 print("data found")
#         else:
#             print("not found")
        
# check_forword()

# def check_forword():
#     word = "code "
#     with open("practice.txt","r") as t:
#         data = t.read()
#         if(data.find(word)!= -1 ):
#                 print("data found")
#         else:
#             print("not found")
        
#  search a word with which number the value exsist.---
# def check_forword():
#     word = "code"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as t:
#         while data:
#             data =t.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no+=1
#     return -1

# check_forword()


#Splict method -  

# with open("practice2.txt","r") as k:
#     data = k.read()
#     print(data)

#     num = " "
#     for i in range(len(data)):
#         if (data[i]==","):
#              print(num)
#              num =" "
#         else:
#             num += data[i]

#type Cast(basic idea)--- 
# with open("practice2.txt","r") as k:
#     data = k.read()
#     print(data)

#     num = " "
#     for i in range(len(data)):
#         if (data[i]==","):
#              print(int(num))
#              num =" "
#         else:
#             num += data[i]
            
            
            
#advance idea--------- 
# with open("practice2.txt","r") as p:
#     data = p.read()
#     print(data)
#     count=0
#     num = data.split(",")
#     for val in num:
#         if(int(val) % 2 == 0 ):
#             count += 1

# print(count)
    