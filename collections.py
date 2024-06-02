#list ---> array in js
color = ["white", "red", "yellow"]

#add
color.append("pink")
print(color)

#for loop
for current_value in color:
    print(current_value)
# for(i=0,i<color.length;i++)
# current_p = color[i]

#Dictionaries
me = {
    "first_name":"Amber",
    "last_name":"Patton",
    "age":37
}

#get a value

print(me["first_name"])
print(type(me))
#add
me["color"]="blue"

print(me)
print(me["first_name"]+" "+ str(me["age"]))
print(color[1], color[3])

ages = [32, 74, 78, 20, 69, 52, 26, 31, 37, 98, 43, 18, 26, 39, 14, 23, 45, 8, 40, 51, 13, 22, 99, 3, 21, 30, ]
# print all the numbers
# print all the numbers greater or equal to 20
# print all numbers greater than 21
def printall():
    count = 0
    for age in ages:
        if age >=21:
            print(age)
            count +=1
    print("there was "+str(count)+" numbers greater than 21")

#call the function
printall()

users = [
    {
        'id': 1,
        'name': 'Alice',
        'gender': 'female',
        'age': 25,
        'preferred color': 'blue'
    },
    {

        'id': 2,
        'name': 'Bob',
        'gender':'male',
        'age': 30,
        'preferred color': 'green'
    },
    {
        'id': 3,
        'name': 'Charlie',
        'gender': 'female',
        'age': 20,
        'preferred color': 'blue'
    },
    {
        'id': 4,
        'name': 'Dave',
        'gender':'male',
        'age': 25,
        'preferred color': 'green'
    },
    {
        'id': 5,
        'name': 'Eve',
        'gender': 'female',
    },
    {
        'id': 6,
        'name': 'Frank',
        'gender':'male',
        'age': 35,
        'preferred color': 'blue'
    },
    {
        'id': 7,
        'name': 'Grace',
        'gender': 'female',
        'age': 22,
        'preferred color': 'green'
    },
    {
        'id': 8,
        'name': 'Harry',
        'gender':'male',
        'age': 28,
        'preferred color': 'blue'
    },
    {
        'id': 9,
        'name': 'Irene',
        'gender': 'female',
        'age': 24,
        'preferred color': 'green'
    },
    {
        'id': 10,
        'name': 'Jane',
        'gender': 'female',
        'age': 27,
        'preferred color': 'blue'
    }
]

def printNames():
    for user in users:
        print(user["name"])

def printHowMany():
    female = 0
    male = 0
    for user in users:
        gender = user["gender"]
        if gender == "female":
            female += 1
        elif gender == "male":
            male += 1
#string formatting
    print(f"there are {female} females and {male} males")
printHowMany()

def findById(id):
    for user in users:
        if user["id"]==id:
            print(user)

findById(1)

printNames()


