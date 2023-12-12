print("Hello World")

#integer 
num = 53

#float 
pi = 3.14

#strings

name = "john dee"

num = "54"
num_i = int(num)
num_s = str(num_i)
num_f = float(num)

x = 5
y = 7

#Add 
add = x+y
print(add)

sub = x - y 
print(sub)

#Division
div = x/y
print(div)

#modulus
mod = x % y
print(mod)

# =============================================================================
# Lists 
# =============================================================================
lis = []

lis.append(1)
lis.append(1.23)
lis.append("Python")
lis.append([1,2,3])


lis[2]

#replacing or inserting a value into index 
lis.insert(2,"java")

lis[3] = "java"

#removing elements in List 
lis.remove(1)
#deleting value based on your index

del lis[3]

#set 
set_123 = set(lis)

lst1 = [1,2,2,3,3,3,3,34,4,4,4,4,434]
set_1233 = set(lst1)

lst2 = ["Python","python","python"]
set123 = set(lst2)

set123.append([1,2,3])
set123.append("python")


