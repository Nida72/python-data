#while loop
"""i = 1
while i < 6:
  print(i)
  i += 1
#eg
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)"""
#eg
age = 19
while age > 18:
    break
    print('You can vote')
#print number

number = 4
while number > 0:
    number -= 1
    if number == 3:
     print(number)
#another eg
# Take user input
number = int(input("enter the number: ")) 
while number < 510 :  
    # Find mod of 2
    if number%2 == 0:  
        print("The number "+str(number)+" is even")
    else:
        print("The number "+str(number)+" is odd")
    number = number+1
#another eg
i = 3
while(i < 60):
 j = 3
 while(j <= (i/j)):
   if not(i%j): break
   j = j + 1
 if (j > i/j) : print (i, " is prime")
 i = i + 1
