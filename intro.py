print("hello world")
# creating variables in python
# JS let or const, boolean or all the other types
name = "Amber"
last_name = "Patton"
age = 37
country = "united_states"
found = True
total = 12.99
print(name + last_name + "is" + str(age) + "years old")
print("Hello my name is" + name + "I am" + str(age) + "years old" + "and I am from" + country)

#if/else statement
# if(age < 100){console.log("no worries, you're not that old")}

if age > 30:
    print("You are old")
else:
    print("You are young")

#functions
#function name_of_function(parameters) --> this is the JS

name = "Amber"
last_name = "Patton"
age = 37
country = "united_states"
found = True


def say_hello():
    print("hello there!")

def say_goodybye(name):
    print("goodbye" + name)


    
# call the function
say_hello()

