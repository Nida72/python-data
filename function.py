def cal_sum(a,b):
    sum= a+b
    print(sum)
    return sum
cal_sum(30,7)
cal_sum(50,0)

#print length of a list
names = ["nida","hassan","ahmed","sana"]
age = [10,11,67,9,34,2,4,7,8]
def print_len(list):
    print(len(list))


    print_len(names)
    print_len(age)

#print element of list in one line
names = ["nida","hassan","ahmed","sana"]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
     print(item, end=" ") 


print_list(names)

#find factorial of n

n=5

def cal_fact(n):
   fact= 1
   for i in range(1,n+1):
      fact*= i
      print(fact)


cal_fact(2)

#convert usd into pkr

def converter(usd_val):
   pkr_value= usd_val*279.66
   print(usd_val, "USD =", pkr_value, "PKr")


converter(1000)














#lamda function
greetings = lambda : print("Hello, Welcome to the future of AI")


greetings()


def introduction(name):
    print("Hello,", name)

introduction("Nida")

greetings = lambda name : print("Hello,", name)

greetings("Nida")





Car = lambda model,color,price,plate_no : print("Model", model,"\ncolor",color,"\nprice",price,"\nplate No",plate_no)

Car(2020,"Black","2 Cror","5555")
