# Task 1

#print simple string
print("hello, Python World!")



# Task 2

# set variables
name = str("Ian")
age = int(23)
height = float("1.7")

# print variables
print(f"My name is: {name}")
print(f"My age is {age}")
print(f"My height is {height} m")



# Task 3

# create list and print list
favorite_food = ["Panang curry","Lamb saag","Sushi"]
print(favorite_food)

# create dictionary and print it
book_info = {
    "title":"1984",
    "author":"George Orwell",
    "year":1949
}
print(book_info)



# Task 4

# set number to test
number = 2

# test number for positive, negative, or zero
if number > 0:
    print("number is positive")
elif number < 0:
    print("number is negative")
else:
    print("number is zero")

# print each item within favorite food list
for food in favorite_food:
    print(food)



#Task 5

# create greet function
def greet(name):
    print(f"Hello {name}")

# call greet function
greet("Alice")



#Task 6

#Function for task 6
def task6(name,age):
    age_plus_5 = age + 5
    print(f"Hello {name}, you will be {age_plus_5} in 5 years")

#get user inputs for function
name = input("What is your name?: ")
age = int(input("What is your age?: "))

#call function
task6(name,age)
