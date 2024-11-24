#Read a file
f = open('data.txt','r')
print(f.readline(),end="")
print(f.readline())
print(f.readline())


#Write a file
new = open("new","w")
new.write("Python is fun!!!!")
