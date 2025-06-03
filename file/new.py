import os 

if os.path.exists("new_example.txt"):
    print("File exists")
else:
    print("File does not exist")


files=os.listdir()
print(files)