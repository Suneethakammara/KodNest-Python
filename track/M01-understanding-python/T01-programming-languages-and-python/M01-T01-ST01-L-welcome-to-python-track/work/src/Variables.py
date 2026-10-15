   #VARIABLES
name="Suneetha"
age=22
print(name)
print(id(name))
print(type(name))

print("Hello Python",end=" - ")
print("Thank you python")

print("Hello python \nThank you python")

# My name is Suneetha and age is 22 str + str
print("My name is "+ name + " age is ", age)
print("My name is "+ name + " age is "+ str(age))

#String Formatting ()f strings
print(f"My name is {name} and age is {age}")

#single line comments
""" multi line comments
used in dictionaries to explain something about the code
"""
#multiple values into multi varialbles in single line
a,b,c =10,20,30
print(a+b+c)
a=b=c=10
print(a+b+c)

a, b, c ="ram", "hari", "shiv"
print(b)
print(a+b+c)

x,y,z= 30,4,8
print(x+z) #=38
print(a+str(x)) #= ram30
print(b+c) #= harishiv
print(a,x) #=ram 30


##DATATYPES
a=10
print(type(a),a)