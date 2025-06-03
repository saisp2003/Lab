#Write a function to check if a number is prime
def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
print(is_prime(13))

#write a function to calculate the area of a rectangle
def area_of_rectangle(length, width):
    return length * width
print(area_of_rectangle(5, 10))

#create a function to find the maximum of three numbers
def max_number(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
print(max_number(10, 20, 30))

        
#write a function to reverse a string
def reverse_string(string):
    return string[::-1]
print(reverse_string("Hello, World!"))


#create a function to count number of vowels in a string
def count_vowels(s):
    count=0
    vowels="aeiouAEIOU"
    for char in s:
        if char in vowels:
            count+=1
    return count
print(count_vowels("hello world"))

#write a function to check if a string is palindrome

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
print(is_palindrome("Anna"))

#check a function to calculate the sum of a list of numbers
def sum_of_list(num):
    total = 0
    for i in num:
        total += i
    return total
print(sum_of_list([10, 20, 30, 40, 50]))

#Write a function to convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print(celsius_to_fahrenheit(25))

#Write a function to find the minimum value in a list
def min_value(num):
    min_value = num[0]
    for i in num:
        if i < min_value:
            min_value = i
    return min_value    
print(min([10, 20, 30, 40, 50]))

#Create a function to count how many times a character appears in a string
def count_char(s, char):
    count = 0
    for i in s:
        if i == char:
            count += 1
    return count
print(count_char("Hello World", "d"))


#Write a function to check if a number is a perfect number
def perfect_number(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num
print(perfect_number(6))
