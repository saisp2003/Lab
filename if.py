num=10
if(num>0):
    print(num,"is greater than zero")
print("this is always printed")

if(num<0):

    print(num,"is less than zero")
else:
    print(num,"is greater than zero")   

# if-elif-else
age=int(input("Enter your age: "))
if (0<=age<3):
    print("no fare")
elif (3<=age<10):
    print("bus fare is 20")
elif (10<=age<20):
    print("bus fare is 30")
else:
    print ("bus fare is 50")

# Nested if
num1=0
num2=6
num3=15
if(num1>num2):
    print(num1,"is greater than",num2)
else:
    print(num1,"is less than",num2)
    if(num1>num3):
        print(num1,"is greater than",num3)
    else:
        print(num1,"is less than",num3)   
