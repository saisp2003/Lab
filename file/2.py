lines=["line  A\n","line B\n","line C\n"]
f=open("example.txt","w")
f.writelines(lines)
f.close()
f=open("example.txt","r")
content=f.read()
print(content)
f.close()
