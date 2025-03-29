employee= ["Ali","Ahmed","Ayan","Sana","Mustafa"]
print(employee)
# print any one employe
print(employee[3])
print(len(employee))
print(type(employee))

#List Slicing
numbers= [1,2,3,4,5,6]
print(numbers[3:5])
print(numbers[3:])
print(numbers[-2:-1])

#List Method
#adding element
items= [23,45,56,8]
items.append(0)
print(items)
#sorting
#ascending order
list=['mango','banana','apple']
list.sort()
print(list)
Roll= [78,45,77,2,0,42,7]
Roll.sort()
print(Roll)
#descending order
Rollno= [78,45,77,2,0,42,7]
Rollno.sort(reverse=True)
print(Rollno)
#reverse
number= [78,45,77,2,0,42,7]
number.reverse()
print(number)
#insert an element
Rollno= [78,45,77,2,0,42,7]
Rollno.insert(5,15)
print(Rollno)
#Remove and pop
values=[0,1,2,3,4]
values.pop(1)
print(values)

marks=[23,4,5,78,9,0]
marks.remove(5)
print(marks)