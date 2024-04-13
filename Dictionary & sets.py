"""info = {"Key": "value",
        "name": "Shouvik",
        "learning": "Coding",
        "marks": 96.5,
        "subject ": ["Python","C","java"], #list value 
        "topics": ("dict","set") #tuple
        }
print(info)
"""
"""info = {"Key": "value",
        "name": "Shouvik",
        "learning": "Coding",
        "marks": 96.5,
        "subject": ["Python","C","java"], #list value 
        "topics": ("dict","set") #tuple
        }
print(info["name"])
print(info["marks"])
print(info["subject"])
"""
"""info = {"Key": "value",
        "name": "Shouvik",
        "learning": "Coding",
        "marks": 96.5,
        "subject": ["Python","C","java"], #list value 
        "topics": ("dict","set") #tuple
        }
info["name"] = "Shouvik Naskar"
print(info)
"""
"""
#create a null dictionary and add new keys 
info = {"Key": "value",
        "name": "Shouvik",
        "learning": "Coding",
        "marks": 96.5,
        "subject": ["Python","C","java"], #list value 
        "topics": ("dict","set") #tuple
        }

null_dict = {}
print(null_dict)

"""
"""
#create  a new key with null dictionary.
info = {"Key": "value",
        "name": "Shouvik",
        "learning": "Coding",
        "marks": 96.5,
        "subject": ["Python","C","java"], #list value 
        "topics": ("dict","set") #tuple
        }

null_dict = {}
null_dict["name"]= "Shouvek Naskar"
print(null_dict)
"""
"""
#create dictionary and add new keys 
info = {"Key": "value",
        "name": "Shouvik",
        "learning": "Coding",
        "marks": 96.5,
        "subject": ["Python","C","java"], #list value 
        "topics": ("dict","set") #tuple
        }

info["name"] = "Shouvik Naskar"
info["surname"] = "Naskar"
info["marks"]=  96.8
print(info)
"""

#Nesting code-------------
"""student = {
    "name" : "Shouvik Naksar",
        "subject" : {
                    "math":98,
                    "phy":96,
                    "chem":95
            
                 }
}
print(student["subject"])
"""
"""
# for particuler data found
student = {
    "name" : "Shouvik Naksar",
        "subject" : {
                    "math":98,
                    "phy":96,
                    "chem":95
            
                 }
}
print(student["subject"]["math"])
"""
"""#for all keys
student = {
    "name" : "Shouvik Naksar",
        "subject" : {
                    "math":98,
                    "phy":96,
                    "chem":95
            
                 }
}
print(student.keys())

"""
"""
#type casting in dictionary
student = {
    "name" : "Shouvik Naksar",
        "subject" : {
                    "math":98,
                    "phy":96,
                    "chem":95
            
                 }
}
float()
print(list(student.keys()))
"""
"""
#retun values
student = {
    "name" : "Shouvik Naksar",
        "subject" : {
                    "math":98,
                    "phy":96,
                    "chem":95
            
                 }
}
print(student.values())
print(list(student.values()))
print(student.items())
print(student["name"])
print(student.get("name"))
print(student["name2"]) #if we write name2,output will be error.
print(student.get("name2")) #if we write name2, output will be None.

"""
"""
student = {
    "name" : "Shouvik Naksar",
        "subject" : {
                    "math":98,
                    "phy":96,
                    "chem":95
            
                 }
}
new_dict = {"city":"kolkata"}
student.update(new_dict)
print(student)
"""
"""
student = {"name" : "Shouvik Naskar",
           "subject" :{
                        "phy":98,
                        "math":96,
                        "chem":94
                  }
        }
print("BEFOR")
print(student("name2")) #error
print("After")
"""
"""student = {"name" : "Shouvik Naskar",
           "subject" :{
                        "phy":98,
                        "math":96,
                        "chem":94
                  }
        }
#student.update("City": "Kolkata")
new_dict = {"city": "kolkata"}
student.update(new_dict) 
 
print(student)
"""

#SET--------------

"""collection = {1,2,3,4}
print(collection)
print(type(collection))

collection = {1,2,3,4}
print(collection)
print(len(collection))
"""
"""collection = {1,2,2,"to","to","shoo",3,4}
print(collection)
print(type(collection))
print(len(collection)) #total number of items
"""
"""
collection = set()
print(type(collection)) #for empty dictionary
"""
"""collection = set()
collection.add(1) # add() in sets
collection.add(2)
collection.add(2)
print(collection)
print(type(collection))
"""
"""collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.remove(1) # values removes from sets
print(collection)
print(type(collection))
"""
"""collection = set()
collection.add(1)
collection.add(2)
collection.add("shouvik naskar")
collection.add((1,2,3)) #tuple value
collection.add([1,2,3]) #list value or found error
collection.remove(1) # values removes from sets
print(collection)
print(type(collection))
"""
""" collection = set()
collection.add(1)
collection.add(2)
collection.add("shouvik naskar")
collection.add((1,2,3)) #tuple value

collection.clear() #
print(collection)
print(type(collection))
"""
"""
collection = {"hello","shouvik","naskar"}
print(collection.pop())
"""
"""
set1= {1,2,3}
set2= {3,4,5}
print(set1.union(set2)) #{1,2,3,4} only unique value return  in new sets
"""
"""set1= {1,2,3}
set2= {3,4,5}
print(set1.intersection(set2)) #{3,} only common value return  in new sets
"""
"""
dictionary =  {
    "cat": "a small animal",
    "table": ["a piece of furniture", " list of facts & figures"]
}
print(dictionary)
"""
"""subject = {"python","java","C++"," python", "javascript" ,"java", "pyton", "java", "C++", "C"}
print(len(subject))
"""

"""marks = {}
x= int(input("enter Phy :"))
marks.update({"phy":x})
x= int(input("enter math :"))
marks.update({"math":x})
x= int(input("enter chem :"))
marks.update({"chem":x})
print(marks)
"""
"""values = {9, 9.0}
print(values)
   """ #OR
   """
values ={
    ("float",9.0),
    ("int",9)
}
print(values)
"""