#print a number pattern using for loop and range function
#take levels from user

levels=int(input("Enter number of levels:"))
for level in range(1,levels+1):
    for num in range(level):
        print(level,end=" ")
    print("/n")
