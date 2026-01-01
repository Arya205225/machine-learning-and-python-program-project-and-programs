# conditional statement  
#marks = int(input("Enter your marks: "))
#if (marks >=90):
 #   print("Grade A")
#elif(marks >=80):
 #   print("Grade B")
#else:
 #   print("Grade C")
 
 
 # check the positive negtive and zero and not exist
#num = int(input("enter the number "))
#if(num>0):
 #       print(num," is positive number")
#elif(num<0):
 #       print(num," is negative number")
#elif(num==0):
   #     print(num," is zero")
#else:
  #  print("number does not exist")  
  
# list example
#food=["samosa","chart","pastsa","burger"]
#print(food)
#print(food[2])
#food[3]="pizza"
#print(food)     
#print(food[1:4])
#print(food[:1])
#print(food[2:])
#print(food[:-1])
#print(len(food))
#print(max(food))
#print(min(food))

#strings are immutable
#name = "aryan raj"
#name[2]="P"
#print(name) because string are immutable


marks = [45,67,89,23,90]
marks.append(78)
#print(marks)

marks.insert(2,88)
#print(marks)

marks.remove(23)
#print(marks)

marks.pop()
#print(marks)

marks.sort()
#print(marks)

marks.reverse()
#print(marks)

food=[]
#food= input("enter the food items separated by comma: ").split(",")
#print(food)
#print(len(food))


#tuple example
fruits = ("apple","banana","mango","grapes")
#print(fruits)


# fruits[1]="orange"
# print(fruits)  tuple are immutable
# error generated

#print(fruits[2]) # indexing printing mango


tup=()
#print(type(tup))

#print(fruits.count("apple")) # counting apple in the tuple
#print(fruits.index("mango")) # printing index of mango in the tuple

fruits = ("apple","banana","mango","grapes","pineapple")
#print(len(fruits))
#print(fruits.index("mango"))


# parctic assignment 

movie=[]
#movie= input("enter the movie names separated by comma: ").split(",")
#print(movie)

marks=(45,67,89,23,90)
#print(max(marks))
#print(min(marks))

#marks=int(input("enter your marks: "))
#if(marks>=90):
    #print("Grade A")
#elif(marks>=80):
    #print("Grade B")
#else:
   # print("Grade C")
 
 # dictonary
 
#student={"name":"aryan",
 #         "age":21,
  #        "courses":"BCA",
   #       }

#print(student["name"])
#student["age"]=22
#print(student)
#student["country"]="India"
#print(student)
##student.pop("country")
#print(student)
#print(student.keys())
#print(student.values())
#print(student.items())
#print(len(student))
# print(student.get("name"))
# print(student.update({"age":23}))
# print(student)
# print(type(student))
# student.clear()
# print(student)

marks={}
marks["maths"]=90
marks["science"]=85
marks["english"]=88 
print(marks)


# sets in python

# myset={"Aryan ", "Raj", 21, 21}# duplicate value not allowed in set
# print(myset)


# num = {1,2,3,4,5}
# num.add(6)
# print(num)
# num.remove(3)
# print(num)

# programinglist=["python","java","c++","javascript"]

# programingset=set(programinglist)
# print(programingset)
# print("divya knows these programing languages:",len(programingset))

# dictonary
dict={1:"apple",2:"banana",3:"mango"}
print(type(dict))

# sets
sett={1,2,3,4,5}
set2={4,5,6,7,8}
set5=sett.union(set2)
print(set5)
set3=sett.intersection(set2)
print(set3)

a={9}
b={0.9}
c=a.union(b)
print(c)