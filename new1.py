#write a function to calculate and return sum of two numbers
def sum_of_two_numbers(x,y):
    sum_of_two_numbers=x+y
    return sum_of_two_numbers
result= sum_of_two_numbers(4,8)
print("result:", result)

#print(sum_of_two_numbers(7,9))

#create a function that returns both area and circumference of a circle given its radius

def area_and_circumference(radius):
    pi=3.14
    area=pi*radius*radius
    circumference=2*pi*radius
    return(area,circumference)
print(area_and_circumference(10))

#write a function that greet a user if no name is provided and should greet with default name if name is provided
def greet_user(name=""):
    print("Hello, " + name + "!")
print(greet_user("John"))
print(greet_user())