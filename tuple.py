tup=(1,3,3,4,4,5,2,45,6,7)
print(tup)
print(tup[3:5])
#print index
num=(1,3,3,4,4,5,2,45,6,7)
print(num.index(2))
#print count
num=(1,3,3,4,4,5,2,45,6,7)
print(num.count(4))


#Examples
#No:1 user enter name and store in a list

names= []
name1= input("Enter 1st name")
name2= input("Enter 2nd name")
name3= input("Enter 3rd name")
names.append(name1)
names.append(name2)
names.append(name3)
print(names) 

#No:2  check if list is palindrome or not

list= [1,2,1]
copy_list= list.copy()
copy_list.reverse

if(copy_list==list):
    print("Palindrome")
else:
    print("not")