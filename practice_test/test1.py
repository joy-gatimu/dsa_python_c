print("Hello python")
name="Joy"
name2="Joy"


print(id(name))#same id value coz they store the same value
print(id(name2))

num=25
balance=159.08
flag=True

"""

Multiple line comments

"""

print(type(name))
print(type(num))
print(type(balance))
print(type(flag))
print("Hello"+" "+name)

# for loop
for  i in range(5):
    print(i)

print("Using a loop")
items=[1,2,3,4,5,6,7,8]
for item in items:
     print(item)
     
print("using range")
for i in range(2,18,2):
    print(i)
 
   
for i in range(18):
     if i==17:
        print(i)