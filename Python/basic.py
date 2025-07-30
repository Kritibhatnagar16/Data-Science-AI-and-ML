
print("hiiii")
a = "hello"
num = 20
# - ctrl + ? (to comment all)
Age = 23
age = 23
print(age)
print(Age)

name = "kriti"
print(name)

print(type(name))
print("my name is",name)

print(" name datatypes",type(name))
print(" len of name :",len(name))

###indexing
print(name[0])
print(name[4])


### Slicing in python ###########
name = "kriti"
print(name[0:4])


#### operation
name = "kriti"


print(name.count("r"))

name = "kriti"

name= "kriti"
reversed_name = name[::-1]
print("Reversed name is:", reversed_name)


number = "5656460000"
reversed_number = number[::-1]
print("Reversed no is:", reversed_number)

name = "kRIti"
upper_case=name.upper()
print(upper_case)

lower_case = name.lower()
print(lower_case)


# >>>>>>>>>>>>>>>list>>>>>>>>>>>

list = [1,2,3,4,5,6,"rohit",2.3]
#list
mutable
duplicated values
order
array ----
homogeneous 
print(list)
print("my first list:",list)
print("len of list:",len(list))
print("type of list",type(list))

print(list[0])
print(list[6])


print(list[0:5])

list = [1,2,3,4,5,6,2.3]
list.pop()
print(list)

list.append(100)  ##add in last
print(list)

list.insert(0,1000)
print(list)

copy_list = list.copy()
print(copy_list)
list.reverse()
list.remove(3)
print(list)
list.sort()
print(list)

print(list.count(2))
print(list)

list.clear()
print(list)


#>>>>>>>>>>>>>>tuple>>>>>>>>>>>>>>
tpl =(1,2,3,4,345, "kriti",2.3)
print("my first tuple:",tpl)
print("len of tuple:",len(tpl))


print(tpl[0])
print(tpl[0:6])


a=1,2,3,4,5,6,
print(a)
print(type(a))
print(len(a))

###tuple unpacking
a,b,c,d = (1,2,3,4)
print(a)
print(b)
print(c)
print(d)


tuple = (1,56,78,388)
print("max or tpl",max(tuple))
min(tuple)
sum(tuple)


#######Dictionary

my_dict = {
    "name": "rohit",
    "class": "2nd year",  ### name,class-keys
    "Address": "jpr"      #### rohiy-value   total is item
}

print("my first dict:",my_dict)
print("length of dict", len(my_dict))

print(my_dict['name'])
print(my_dict['class'])
print(my_dict['Address'])
my_dict['Address']= "bharatpur"
print(my_dict['Address'])

my_dict['branch']= "ai"
print(my_dict)

#####################################
list = [ 1,2,3,4,[2,5],7 ]  ## 5 accesss
print(list[4][1])
#####################################

a = [1,2,3,4]
a.reverse()
print(a)

#################OPERATORS##########

x =  int(input("Enter x: "))
x += 10
print("after adding value",x)


list = [ 1,2,3,4,7 ]
print(list[::-1])    ####slicing

a = [1,2,3,[4,5,6]]
a.pop()
print(a)
###############################################

# task = use update function to update dict
# get function >>>> 5 example or []  acces using this bracket

###############################################

my_dict = {
   "name": "rohit",
    "class": "2nd year",  ### name,class-keys
    "Address": "jpr"      #### rohiy-value   total is item
 }

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# copy_dict=my_dict.copy()
# print(copy_dict)

# a = input("enter a no.")
# b = input("enter  secondno.")
# print(type(a))

#########type casting

# a = int(input("enter a no."))
# b = int(input("enter  second no."))
# print(a*b)

# lst = [1,2,3,4,5]
# print("thsi is my list" , lst)
# print("type of list" , type(lst))
# tpl =tuple(lst)
# print("this is my tuple" , tpl)
# print("type of tuple" ,type(lst))

##############SET##############

# my_set = {1,2,1,3,4,4,5,6, "jay"}   ######id didn't allow duplicate 
# print("this is my firrst set" , my_set)
# print("len of srt" , len(my_set))
# print("type of srt" , type(my_set))


# lst = list(my_set)

# lst.append(100)
# print(set(lst))



# # task = use update function to update dict
# # get function >>>> 5 example or []  acces using this bracket

# ### set task
# ### my_set.union() ,my_set.intersection() , my_set.diff.()
# ### operator all code

##################################TASK SECTION#########################################################


# # task = use update function to update dict
student = {
    "name": "Kriti",
    "age": 20,
    "course": "AI"
}
student.update({"age": 21, "grade": "A"})
print(student)
############################

# # get function >>>> 5 example or []  acces using this bracket

students = [
    {"name": "Kriti", "age": 20},
    {"name": "Hardik", "city": "Jaipur"},
]

print(students[0].get("age"))               
print(students[1].get("age")) 
print(students[0].get("name")) 
print(students[1].get("grade"))
print(students[1].get("city",))
print(students[0].get("place"))

#### my_set.union() ,my_set.intersection() , my_set.diff.()

a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a.union(b)) 
print("Union:", b.union(a)) 
print("Intersection:", a.intersection(b))  
print("Intersection:", b.intersection(a))  
print(" a - b:", a.difference(b))  
print("b - a:", b.difference(a))  


a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)





























