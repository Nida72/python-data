list = [1,5,6,7,3,2,9]
for el in list:
    print(list)

#print the value
num = [1,2,3,4,5]
for val in num :
    print(val)
#print character
str = "NidaHassan"
for char in str :
 print(char)

 #exercise
 #NO1:
number = [1,3,4,5,6,3,8,9,54]
for val in number:
   print(val)

#idx
tuple = (1,5,6,7,8,3,5,7)
x= 5
idx= 0

for val in tuple:
   if(val==x):
    print("value found at index" ,idx)
    break
   idx+=1

#Range function
seq = range(6)
for el in seq:
   print(el)
#print odd number
item = range(1,100,3)
for val in item:
   print(val)
#print even number
item = range(2,100,2)
for val in item:
   print(val)
#other method to print odd number
for el in range(1,100,3):
 print(el)

#practice question 
#print number from 1 to 100
for num in range(1,101):
   print(num)

#print number from 100 to 1
for i in range(100, 0 ,-1):
   print(i)

#print multiplication table of any number
#first take input from user
number = int(input("enter the number"))
for x in range(1*11):
   print(number*x)
# factorial number
n= 6
i=1
fact= 1
while i<=n :
   fact*=i
   i+=1 
   print("facrorial " , fact)

# factorial number
n= 6
fact= 1
for i in range(1,n+1):
   fact*=i
   i+=1 
   print("facrorial " , fact)


   
