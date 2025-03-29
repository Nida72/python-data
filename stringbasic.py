str= "this is a string.Here we write some names."
print(str)
#for spaces and next line
str= "this is a string.\nHere we write some names."
print(str)

str= "this is a string.\tHere we write some names."
print(str)

#concatenatin
str= "My"
str1="Nameis"
string_len=str+str1
print(str+" "+str1)
print(len(string_len))

#slicing
names= "Nida Hassan"
print(names[2])
print(names[4:])
print(names[:4])
#Functions
#endswith
str= "Nida"
print(str.endswith("ror"))
#captalize
str= "nida"
print(str.capitalize())
#replace
str= "nida"
print(str.replace("nida","Hassan"))
#find

str= "this is a string.Here we write some names."
print(str.find('a'))
#count
str= "this is a string.Here we write some names."
print(str.count("is"))

#Exercise questions : input name from user and find length of string

name= input("enter your firstname:")
print(len(name))

#No:2

