# num1 = int(input("Enter First Number : "))
# num2 = int(input("Enter Second Number : "))
# print("Sum of Two Number : ", num1+num2)


# sideOfSquare = int (input("Enter the side of square :"))
# print("Area of Square :", sideOfSquare*sideOfSquare)

# float1 = float(input("Enter First Floating Number :"))
# float2 = float(input("Enter Second Floating Number :"))

# print("Avrage of two floating number :", (float1+float2)/2)

# a = int(input("Enter First Number : "))
# b = int(input("Enter Second Number : "))
# name = "bablu"
# print(a>=b)
# print(len(name))
# print(name[-6:-1])



# str = " I am BabluSarkar"
# print(str.capitalize())
# print(str.endswith("kar"))
# print(str.replace("kar","ji"))
# print(str.find("am"))
# print(str.count("a"))

# name = input("Enter your first name :")
# print(len(name))
# print(name.count("a"))

# num = int(input("enter days number :"))
# value = num/10
# if( value ==1):
#     print("Sunday")
# elif(value ==2):
#     print("Monday")
# elif(value ==3):
#     print("Tuesday")
# elif(value ==4):
#     print("Wednesday")
# elif(value ==5):
#     print("Thrusday")
# elif(value ==6):
#     print("Friday")
# else:
# print("Satuarday")


# count bijli bill



# unit =int(input("Plese Enter your bijli unit : "))
# amount =0;
# if  unit>400:
#     amount += (unit-400)*8
#     unit = 400
# if unit>300 and unit <=400:
#     amount +=(unit-300)*6
#     unit = 300
# if unit>200 and unit <=300:
#     amount +=(unit-200)*4
#     unit = 200
        
# if unit>100 and unit <=200:
#     amount +=(unit-100)*3
#     unit = 100
# else:
#     amount+=(unit-100)*0
#     unit=0
    
# print("Total bill amount :", amount)



# num = int(input("Enter number "))

# if (num % 2 == 0):
#     print("Even number")
# else:
#     print("Odd Number")


# switch case in python


# list = [2, 3, 4, 5, 2, 4, 5, 3, "bablu", "student"]*10



# list = [None] * 10

# list[0] = 10
# list[1] = 20
# list[2] = 30
# list[3] = 40
# list[4] = 50
# list[5] = 60
# list[6] = 70

# max_Size = len(list)
# end_Size = 0

# for i in list:
#     if i is not None:
#         end_Size += 1

# print("listay:", list)
# print("Max size:", max_Size)
# print("End size:", end_Size)



# list =[2,3,12,3]
# print(type(AttributeError))
# print(list[2:4])
# print(list[1:4])
# print(list[1:])
# print(list[:4])

# list.append(3) # add element in the last index
# list.sort() # sort in descending order
# list.sort(reverse=True) #sort is work same as inverse is take reverse == true
# list.reverse()# this is reverse the list item
# list.remove(list[2])# This is always remove item in the exist in list take one argument  
# list.insert(2,100)# This methode is take two argument first is index value and second one insert value
# list.pop(1) # delete as a last element without argument , if you pass the argument then thel deleted the item based on argument index
# list.clear() # Clear all elment in list -> array
# listval = list.copy() # this is return shalow copy of list
# print(listval)
# countval=list.count(3)  # this is always count occurance element inn list and return count occurance element
# print(countval)

# list.extend
# print(list)



# ----------- Tuple -----------------

# list =[2,3,12,3]
# tup=(2,3,4,5,5)

# print(type(list),type(tup)

# print()










# ----------------- Dictionary and set ------------------

#  dictionaries is also like a Object in javascript same as dictionaries pair of key and value

# dict = {
#     "name":"babluSarkar",
#     "cgpa":9.8,
#     "marks":[98,92,87]
# }
# print(type(dict))
# print(len(dict))
# print(dict)
# print(dict.clear()) # Clear all the element of dictionaries
# print(dict.copy()) # Copy the all dictionary item
# print(dict.get("marks")) # get the data based on key

# print(dict.items())

# print(dict.pop("name"))
# print(dict.popitem())
# print(print())w


# dict = {
#     "name":"babluSarkar",
#     "cgpa":9.8,
#     "subject":("phy","che","math","science","social science"),
#     "marks":{
#         "phy":80,
#         "che":90,
#         "math":99,
#         "science":79,
#         "social science":89
#     }
# }

# print(dict)
# print(dict.keys())
# pair = list(dict.values())
# val =list(pair[3])
# print(dict.get("marks"))

# dict.update({"name":"sarkar ji"})
# print(dict)


#  tuple is look like set of data items but do not change or set items

# university = ("svsu","ccsu","du","bhu","iit")
# print(university)










#  set : set is unordered collection of items

# student = {"mohan","sohan","sarkar",1,3,4,2}
# student.add(5)
# student.clear()
# student.copy()
# new_student = {"bitu",2,1}
# result = student.difference(new_student)
# student.discard("mohan")
# print(student)
# print(result)
# print(type(student))


# --------------- Practice questions--------------

#  store following word meanings in a python dictionary:
#  table: " a piece of furniture","list of facts & figure"


# disctionarery = {
#     "cat":"cat is small animal",
#     "table":[" a piece of furniture","list of facts & figure"]
# }

# print(disctionarery)

# set_of_classroom ={"c++","java","python","java","c++","python","java","c","c++","js","python"}
# # print("reuired class room of that subject ",set_of_classroom,"total room ", len(set_of_classroom))
 
 
# disc = {}
# disc.update({"user1":{
#     "subject":"math",
#     "marks":90
# }})
# disc.update({"user2":{
#     "subject":"english",
#     "marks":89
# }})
# disc.update({"user3":{
#     "subject":"phy",
#     "marks":80
# }})
# print(disc)










# -------- Loops in Python -------------


# while loop
# i=0
# while i<=5:
#     if i==3:
#         print(" i is equal to 3")
#     print("Number", i)
#     i+=1
# print(i)
# ----- Practice question---------------

#  1 print numbers from 1 to 100
# number = 1
# while number <=100:
#     print( number)
#     number+=1
    


# ------- print number from 100 to 1

# number = 100
# while number >=0:
#     print(number)
#     number-=1


# --------print the multiplication table of a number n

# n=int(input("enter your number : which number of table:"))
# i=1
# while i<=10:
#     print(f"{n}*{i} = ",i*n)
#     i+=1

# ----------- print the element of the following list using a loop---------

# list = [23,4,2,4,5,6,7,2,3,2,32,23,323]
# i=0
# while i<len(list):
#     print(list[i])
#     i+=1
    
    
    
# ------------- search for a number x in this tuple using loop -----------

# num=(2,3,1,2,1,2,6,32,1,212,54)
# i=0
# # print(tuple.count(x))
# x=int(input("Enter your search item "))
# while i<len(num):
#     if(x==num[i]):
#         print(f"found at index {x}->", i)
#     i+=1
        

# ------------ For loop -----------------

num=[2,1,3]  # list
# veg =["potato","onion","carret","brinjal"] # list
# tup=(2,1,2,3,2,3,4) # Tuple
# disct={
#     "name":"bablu sarkar",
#     "course":"btech",
#     "year":"4th",
#     "specilization":"cse"
# }
# for val in num:
#     print(val)
# else:
#     print("end")

# ------------- Practice question -----------

# list = [2,2,2,4,3,2,4,5]
# for num in list:
#     print(num)

# ------ search x item-----

# x= int(input("Enter the search item : "))
# for num in list:
#     if(num == x):
#         print("found the x item:", num)
        
        
# --------------- Range function in python -----------------

# val =range(5)

# print(len(val))

# for i in val:
#     print(i)


#  example range(start, stop, step)

# for i in range(10):
#     print(i)
# for i in range(2, 10,3):
#     print(i)


#  --------- Practice question---
# using for and rangr()

# print number from 1 to 100;

# for i in range(1,101,1):
#     print(i)
    
    
# print number from 1 to 100;

# for i in range(100,0,-1):
#     print(i)

#  Print the multiplication of table of a number n.

# num=int(input("Please Enter your table : number "))
# for i in range(1,11,1):
#     print(num*i)

# num = int(input("Enter the value :"))
# i=1
# sum=0
# while i<=num:
#     sum+=i
#     i+=1
# print(sum)

# ----------- find factorial of first n number--------- using for loop

# num = int(input("Please enter the value to calculate factorial :"))
# fact=1
# for i in range(1,num+1,1):
#     fact=fact*i
# print("factorial", fact)









# -------------- Function and recursion -----------

# -------- Practice function based question -------------

# 1. write a program to print the length of a list ( list is the parameter)

# list=[2,3,4,5,6,7]
# def print_fun(list_param):
#     print(len(list_param))
    
# print_fun(list)


# 2. write a program to print the list element of a list in a single line. (list is the parameter)


# list=[2,3,4,5,6,7]
# def print_list_element(list_data):
#     for i in list:
#         print("element of list : ", i)
# print_list_element(list)


# 3. write a program to fint the factorial of n. ( n is the parameter)

# nums=int(input("Enter the factorial number :"))
# def fact(num):
#     factorial=1
#     for i in range (1,num+1,1):
#         factorial=factorial*i
#     print("factorial of n number :", factorial)
    
# fact(nums)

# 3. write a program to convert USD to INR.
# doll=int(input("Please Enter the USD amount :"))
# def dollor_converter(dollor_amount):
#     INR = 91*dollor_amount
#     print(f"{dollor_amount} dollor to ", INR)
# dollor_converter(doll)





# ---------------- Recursion -----------------
# n=5
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
  
# print(fact(n))

# --------------- File Input/Output in Python----------------

# ------------ this is read mode file--------
# f = open("readme.md","r")
# data = f.read()
# data = f.readline()
# data = f.readlines()
# print(data)
# print(type(data))
# f.close()


# r = open("readme.md","r")
# data = r.read()
# print(data)
# r.close()

# ------------ this is write mode file--------

# f= open("readme.md","w")
# f.write("\n this is adding new line")

# f.close()


#--------- append and write data in file
# f= open("readme.md","a")
# f.write("\n this is adding new line 1")

# f.close()

# --------- this is with statement in file handling r+ mode--------

# f= open("readme.md","r+")
# r= f.read()
# print(r)

# import os
# with open("readme.md","r")as f:
#     data=f.read()
#     print(data)
# with open("readme.md","w") as f:
#     f.write("I ma bablu sarkar ji")
# with open("readme.md","r")as f:
#     data=f.read()
#     print(data)
# os.remove("readme.md")





# ------------ Practice question based on file handling ---------

# 1. create a new file "practice.txt" using python. add the following data in it 

# f=open("practice.txt ","w")
# f.write("Hi everyone\n")
# f.write("we are learning file i/o \n")
# f.write("using Java\n")
# f.write(" i like programming in Python")

# 2. Write a Program taht replace all occurrences of "python" and "java" in above file

# with open("practice.txt","r") as f:
#     data=f.read()
#     print(data)
#     new_data = data.replace("python","java")
#     print(new_data)
# with open("practice.txt","w") as f:
#     f.write(new_data)

# 3. Search if the word "learning" exists in the file or not

# with open("practice.txt","r") as f:
#     data=f.read()
#     print(data)

# if(data.find("learning") !=-1):
#     print("word is found")
# else:
#     print("word is not found")


# 4. Write a program in witch line of the file does the word "learning" occure first print -1 if not found
# --------- exmaple-------

# count =0
# with open("practice.txt","r") as f:
#     data = f.read()
#     print(data)
#     num=data.split(",")
#     print(type(num))
#     for i in num:
#         if(int(i)%2==0):
#             print("even")
#             count+=1
#         else:
#             print("odd")

# print("total even number", count)








#  -------------- Opps in Python | Object Oriented Programming --------------

# ----------- Class and Object in Python ------------
# class Student:
#     name="bablu Sarkar"
#     age="21"
#     courses="btech"
#     specilization="Computer Science and Engineering"
#     college="SITE"
    
# s1=Student()
# print(type(s1))

# ----------- Constructor in Python --------------

# class Student:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender

# s1=Student("bablu Sarkar",22,"Male")
# print(s1.name, s1.age, s1.gender)



# ----------- Method in Python --------------
# class Student:
#     #  it is also constructor but this is default constructor
#     def __init__(self):
#         print("This is constructor")
#         # Parameterized constructor
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender

# s1=Student("bablu Sarkar",22,"Male")
# print(s1.name, s1.age, s1.gender)



# class Student:
#     def __init__(self, name=None, age=None, gender=None):
#         if name is None:
#             print("This is default constructor")
#         else:
#             self.name = name
#             self.age = age
#             self.gender = gender

# s1 = Student()
# s2 = Student("Bablu Sarkar", 22, "Male")

# print(s2.name, s2.age, s2.gender)

# -------------- Class & Instance Attributes in Python --------------


# class Student:    
#         # Parameterized constructor
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def hello(self):# it is also know as method
#         print("hello Method", self.name)

# s1=Student("\nbablu Sarkar",22,"Male")
# s1.hello()
# print(s1.name, s1.age, s1.gender)

# -------------- Practice question based on OOPs in Python --------------

# 1. Create a student class that takes name & marks of 3 student subject as argument in constructor then create a method to print the average.

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        
#         # self.average_marks= (english+math+hindi)/3
#     def average_marks(self):
#         average =0
#         for i in (self.marks):
#              average+=i
#         print(average/len(self.marks))
                 
                 
                 

    
# s1=Student("Bablu Sarkar",[89,90,81])
# print("Student Name :", s1.name)
# s1.average_marks()




#  Static Method in Opps

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        
#         # self.average_marks= (english+math+hindi)/3
#     def average_marks(self):
#         average =0
#         for i in (self.marks):
#              average+=i
#         print(average/len(self.marks))
#     @staticmethod
#     def hello():
#         print("Hello Static Method")
                 
                 
                 

    
# s1=Student("Bablu Sarkar",[89,90,81])
# print("Student Name :", s1.name)
# s1.average_marks()
# s1.hello()










# -------------Abstraction in Python --------------
# hiding the implementation details of a class and only showing the essential features to the user

# Example

# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
#     def start(self):
#         self.acc=True
#         self.clutch=True
#         print("Car started..")

# c1=Car()
# c1.start()

# ---------------- Encapsulation in Python --------------

# wrapping data and function inti a single unit (object)

# ----- del keyword--------
#  used to delete object properties or object itself

# class Student:
#     def __init__(self,name,gender,age):
#         self.name=name
#         self.age=age
#         self.gender=gender

# s1=Student("sarkar","male",22)
# # del s1.age
# print(s1.name,s1.age)
        


 #---------------- Private(like) attributes & methods---------
 
#  Private attributes & methods are meant to be used only within the class and are not accessible from outside the class 

# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass
#     def reset_password(self):
#         print(self.__acc_pass)
        
# acc1= Account(23243,1234)
# # print(acc1.acc_pass)
# print(acc1.reset_password())




# ------------------- Inheritance --------------------------

#  When one class (child/derived) derives the properties & methods of another class (parent/base)


# class Car:
#     @staticmethod
#     def start():
#         print("Car started......")
#     @staticmethod
#     def stop():
#         print("car stopped.")
        
# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name=name
        
# car1=ToyotaCar("Toyota")
# car1.start()
# print(car1.name)

# ---- types of inheritance----------
# 1. Single Inheritance-------------------
#  class Car:
#     @staticmethod
#     def start():
#         print("Car started......")
#     @staticmethod
#     def stop():
#         print("car stopped.")
        
# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name=name
        
# car1=ToyotaCar("Toyota")
# car1.start()
# print(car1.name)




# 2. Multi-level Inheritance-------------------

# class Car:
#     @staticmethod
#     def start():
#         print("Car started......")
#     @staticmethod
#     def stop():
#         print("car stopped.")
        
# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name=name
        
# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type=type
         
# car1=Fortuner("Petrol")
# car1.start()
# c2=ToyotaCar("fortuner")
# print(c2.name,  car1.type)




# 3. Multiple Inheritance-------------------

# class A:
#     varA="Welcome to class A"
# class B:
#     varB="Welcome to class B"
# class C(A,B):
#     varC="Welcome to class C"
    
# c1=C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)



# ---------------- Super method------------


# class Car:
#     def __init__(self,type):
#         self
#         self.type=type
#     @staticmethod
#     def start():
#         print("started..")
#     @staticmethod
#     def stop():
#         print("Stoped.")
 
# class TyotaCar(Car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name=name
    
    

# car1=TyotaCar("tyota","petrol")
# # car1.start()
# print(car1.name, car1.type)





# ------------- class method

# class Person:
#     name="anonymous"
    
#     def changeName(self,name):
#         self.__class__.name=name

# p1=Person()
# print(p1.changeName("bablu"))
# print(p1.name)
       
       
# ------------ Properties in Python ------------

# class Student:
#     def __init__(self,phy,che,math):
#         self.phy=phy
#         self.che=che
#         self.math=math
#         # self.percentage=str((self.math+self.phy+self.che)/3)+"%" 
#     @property
#     def get_percentage(self):
#         return str((self.math+self.phy+self.che)/3)+"%"
        
# s1=Student(98,93,38)
# print("Total Percentage", s1.get_percentage)
# s1.phy=70
# # s1.get_percentage()
# print("Total Percentage", s1.get_percentage)


# ------------------ Polymorphism --------------

# Operator overloading : when the same operator is allowed to have different meaning according to the context

# print(3+5)# add
# print("NAME"+"BABLU")# concatenate
# print([2,3,4,5]+[3,2,3,1]) #merge
# print((3,2,3)+(3,4,2))


#  cpmplex number print

class ComplexNumber:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
        print("---------------------------")
    def __add__(self, num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img        
        return ComplexNumber(newReal,newImg)
    def __sub__(self, num2):
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        
        return ComplexNumber(newReal,newImg)
    
    
    

num1=ComplexNumber(3,2)
num2=ComplexNumber(10,20)
num1.showNumber()
num2.showNumber()

# num3=num1.add(num2)
# # print(num3)
# num3.showNumber()
num3=num1 + num2
num4=num1 - num2
# print(num3)
# num3.showNumber()
num4.showNumber()