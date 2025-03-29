#assign value to x and y variable
x= 10
y="Hassan"
print(x)
print(y)

#Get the datatype
print(type(x))
print(type(y))

#camelcase variable
myCarName= "Altis"
myVarName= 'Number'
print(myCarName)
print(myVarName)

#Pascal case
MyCarName= "Civic"
MyVarName= 'Ali'
print(MyCarName)
print(MyVarName)

#snake case
my_var_name= "Ahmed"
print(my_var_name)

#many value to multiple variable
a,b,c = 1,2,3
print(a)
print(b)
print(c)

#assign one value to multi variable 
x=y=z = "Number"
print(x)
print(y)
print(z)

#Global Variable
n= "Nida"
def myfunc():
  print("My name is" + n)

  myfunc()

# //other eg
x = "awesome"
def myfunc():
  x = "Ahmed"
  print("My name is  " + x)

myfunc()

print("My name is " + x)

# other eg
def myfunc():
  global x
  x = "Nida"
myfunc()
print("My name is  " + x)


