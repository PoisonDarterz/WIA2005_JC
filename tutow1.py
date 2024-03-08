# this is a comment

x = "Algorithm is fun"
print(x)

m1 = 12+15
m2 = 15-12
m3 = 24/6
m4 = 9*3
print(m1)
print(m2)
print(m3)
print(m4)

l1 = 12<13
l2 = 12>13
l3 = 18!=17
print(l1)
print(l2)
print(l3)

for x in range (5):
    print(x)

for x in range(2,30,4):
    print(x)
    
animal = ["cat", "dog", "fish"]
for x in animal:
    print(x)
    
numbers = [11,3,7,5,4]
numbers.sort()
print(numbers)

# prompt user to enter name
name = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age)
year = (2022 - age) + 100
print("You will be 100 years old in the year", year)


a = [1,4,9,16,25,36,49,81,100]
b = [x for x in a if x%2==0]
print(b)