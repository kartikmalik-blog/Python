# # # Example
# # # name = "Kenshin"
# # # age = 24
# # # height = 5.9
# # # is_student = True

# # # print(name, age, height, is_student)


# # # name =  input("what is your name:")
# # # age = input("enter your age:")
# # # print("Hello"+ name + "I am " + age + "years old !!")

# # name = "Kartik"
# # age = 23
# # height = 60.5 
# # if_student = True
# # print(name,age,height,if_student)


# name = input("what is your name:")
# age = input("enter your age:")
# height = input("enter your height:")
# if_student = input("are you a student: (yes/no)").lower()
# print(f"Hello I am {name}, my age is {age}, my height is{height}, I am student{if_student}")

# print(type(name))
# print(type(age))
# print(type(height))
# print(type(if_student))

# age = int(input("enter your age:"))
# if age < 13:
#     print("you are just a child")
# elif age <=19:
#     print("you are an teenager")
# else:
#     print("you are an adult")


# age = int(input("enter your age:"))
# is_Student = input("are you a student (yes/no)").lower() == "yes"

# if age > 18 and is_Student:
#     print("congratulations you get a student discount")
# else:
#     print("you are not a student you will not get a discount")

# count = 0

# while count < 5:
#     print("Count is:", count)
#     count+= 1

# for i in range(5):
#     print("steps i", i)

# for Hello in range(5):
#     print("Hello",Hello)

# for i in range(1,6):
#     print("*" * i)

# fruits = ["apple", "banana", "Grapes"]
# print(fruits)

# print(fruits[0])
# print(fruits[2])

# fruits[1] = "mango"
# print(fruits)

# fruits.append("orange")
# print(fruits)

# fruits.remove("apple")
# print(fruits)

# for fruit in fruits:
#     print(fruit)

# favourite_movies = ["The Dark Knight", "The Godfather", "Interstellar", "Pulp fiction", "Goodfellas"]

# print(favourite_movies[2])

# favourite_movies[4] = "Schindler's List"
# print(favourite_movies)

# favourite_movies.append("Fight club")
# print(favourite_movies)

# for movies in favourite_movies:
#     print(movies)

# def greet():
#     print("Hello there !!")
# greet()

# def greet(name):
#     print("Hello",name)
# greet("Sai")

# def square(x):
#     return x * x

# result = square(5)
# print(result)


# def discount_eligibility(age, is_student):
#     if age > 18 and is_student == "yes":
#         return "Discount given"
#     else:
#         return "No discount"
    
# age = int(input("Enter your age: "))
# is_student = input("Are you a student? (yes/no): ").lower()

# result = discount_eligibility(age, is_student)
# print(result)

# def discount_eligibility(age, is_student):
#     if age > 18 and is_student == "yes":
#         return "Discount given"
#     else:
#         return "No discount"
    
# age = int(input("Enter your age: "))
# is_student = input("Are you a student? (yes/no): ").lower()

# result = discount_eligibility(age, is_student)
# print(result)

# def can_vote(age, citizenship_status):
#     if age >= 18 and citizenship_status == "yes":
#         return "You are eligible to vote"
#     else:
#         return "You are not eligible to vote"
    
# age = int(input("Enter your age: "))
# citizenship_status = input("Are you a citizen? (yes/no): ").lower()

# result = can_vote(age,citizenship_status)
# print(result)

# person = {
#     "name" : "Kartik",
#     "age" : 30,
#     "is_student" : False 
# }

# person["age"] = 31

# person["country"] = "Germany"

# del person["is_student"]

# print(person["name"])
# print(person["age"])

# book = {
#     "title" : "the silent sea",
#     "author" : "James Rollins",
#     "pages": 428,
#     "availaible": True
# }

# print(book["title"])
# print(book["pages"])

# library_book = {
#     "title" : "The wandering earth",
#     "author" : "Liu Cixin",
#     "copies" : 3
# }

# for i in range(3):
#     print(f"\nBorrow attempt #{i+1}")  

#     if library_book["copies"] <= 0:
#         print("Book not available")
#     else:
#         library_book["copies"] -= 1
#         print("Book issued. Remaining Book:", library_book["copies"])


# age = int(input("enter your age: "))
# is_student = input("Are you a student? (yes/no): ").lower()

# if age >= 18:
#     if is_student == "yes":
#         print("you are a student you get the discount")
#     else:
#         print("you are not eligible for discount")
# else:
#     print("you are far too young for any discount")

# book = {
#     "title": "1984",
#     "author": "Geroge Orwell",
#     "copies": 5
# }

# print(book["title"])
# book["year"] = 1949
# book["copies"] -= 1
# del book["author"]
# print(book)


# cordinates = (10,20)
# print(cordinates[0])
# print(cordinates[1])

# def greet_people(names):
#     for name in names:
#         print("Hello" + name)

# greet_people(["Alice", "Bob", "Charlie"])

# def calculate_stats(numbers):
#     total = sum(numbers)
#     count = len(numbers)
#     average = total/count
#     return total,count,average

# numbers = [1,3,4,5,6,7,8,10]
# total,count,average = calculate_stats(numbers)

# print("Total:", total)
# print("count:", count)
# print("average:", average)

# number1 = int(input("enter the number: "))
# number2 = int(input("enter the number: "))
# number3 = int(input("enter the number: "))

# total = sum([number1 + number2 + number3])
# average = total/3
# print(round(total,2))
# print(total)

# set1 = {1,2,3}
# set2 = {3,4,5}

# print(set1 | set2)
# print(set1 & set2)
# print(set1 - set2)
# set1.add(10)
# set1.remove(10)
# print(3 in set1)

# math_students = {"Alice", "Bob", "Charlie", "Diana"}
# science_students = {"Bob", "Diana", "Edward"}

# print(math_students & science_students)
# print(math_students - science_students)
# print(math_students | science_students)

# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def greet(self):
#         print(f"Hello my name is {self.name} and I am {self.age} years old")

# student1 = student("Alice",20)
# student1.greet()

# class book:
#     def __init__(self,title,author,copies):
#         self.title = title
#         self.author = author
#         self.copies = copies

#     def borrow_book(self):
#         if self.copies > 0:
#             self.copies -= 1
#             print("Book Borrowed Successfully")
#             print(f"show books{self.copies}")
#         else:
#             print("Sorry, no copies left")

#     def return_book(self):
#         self.copies += 1
#         print("Book returned successfully")
#         print(f"show copies{self.copies}")

# book1 = book("A song of fire and ice", "Geroge R.R martin", 5 )
# book1.borrow_book()
# book1.borrow_book()
# book1.return_book()


# class car:
#     def __init__(self,brand,model,fuel):
#         self.brand = brand
#         self.model = model
#         self.fuel = fuel
    
    
#     def drive(self):
#         if self.fuel > 0:
#             print(f"Driving the {self.brand} {self.model}")
#             self.fuel -= 1
#             print(f"show fuel {self.fuel}")
#         else:
#             print("out of fuel")

#     def refuel(self):
#         self.fuel += 5
#         print("Refueled")
#         print(f"show fuel {self.fuel}")

# my_car = car("Audi","Fat_Bob", 100)
# my_car.drive()
# my_car.refuel()


# class bank_account:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.balance = balance

#     def amount(self):
#         self.balance = 100
#         print("Deposited 100$, New Balance 100$")

#     def withdraw(self):
#         self.balance -= 50
#         print(f"the new balance is {self.balance}")
        
#     def display_balance(self):
#         print(f"the current balance is {self.balance}")

# amount1 = bank_account("Alice",100)
# amount1.amount()
# amount1.withdraw()
# amount1.display_balance()

    
# class vehicle:
#     def __init__(self,brand,speed):
#         self.brand = brand
#         self.speed = speed

#     def drive(self):
#         print(f"The {self.brand} is driving at {self.speed} km/h")

# class car(vehicle):
#     def __init__(self, brand, speed, fuel_type):
#         super().__init__(brand,speed)
#         self.fuel_type = fuel_type

#     def honk(self):
#         print("Beep beep")

# my_car = car("Toyota", 120, "Petrol")
# my_car.drive()
# my_car.honk()
# print(my_car.fuel_type)

# class Vehicle:
#     def __init__(self,brand,speed):
#         self.brand = brand
#         self.speed = speed

#     def describe(self):
#         print(f"The brand of the car is {self.brand} and the speed of the car is {self.speed}")

# class Car(Vehicle):
#     def __init__(self, brand, speed, plat_number):
#         super().__init__(brand, speed)
#         self.plat_number = plat_number

#     def drive(self):
#         print(f"the car with {self.plat_number}  was smoothee")

# class Bike(Vehicle):
#     def __init__(self, brand, speed, number):
#         super().__init__(brand, speed)
#         self.number = number

#     def ride(self):
#         print(f"the bike with {self.number}  was fast")

# my_car = Car("Audi", 100, "BH0012")
# my_bike = Bike("Honda", 100, "HG0011")

# my_car.describe()
# my_car.drive()

# my_bike.describe()
# my_bike.ride()

# class Transport():
#     def __init__(self,mode,capacity):
#         self.mode = mode
#         self.capacity = capacity

#     def show_info(self):
#         print(f"the mode of transport is {self.mode} and the capacity of transport is {self.capacity}")

# class Train(Transport):
#     def __init__(self, mode, capacity, train_number):
#         super().__init__(mode, capacity)
#         self.train_number = train_number

#     def departs(self):
#         print(f"the train number {self.train_number} is departing")

# class Airplane(Transport):
#     def __init__(self, mode, capacity, flight_number):
#         super().__init__(mode, capacity)
#         self.flight_number = flight_number

#     def take_off(self):
#         print(f"the flight number {self.flight_number} is taking off")

# my_train = Train("Express", 500000, "BH0011")
# my_flight = Airplane("Business class", 5000, "BHD121")

# my_train.show_info()
# my_train.departs()

# my_flight.show_info()
# my_flight.take_off()


# with open("file.txt", "w") as file:
#     file.write("Hello this my first text file\n")
#     file.write("Python is powerful")
    

# with open("file.txt", "a") as file:
#     file.write("\nThis is a new line in the file")

# with open("file.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("file.txt", "r") as file:
#     for line in file:
#         print("Line:", line.strip())
#     print("Done writing code in file.txt")

# data = input("write what you like: ")

# with open("file.txt", "w") as file:
#     file.write(f"{data}")

# with open("file.txt", "a") as file:
#     file.write(f"{data}")
#     print(f"Done write in file.txt {data}")

# with open("file.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("file.txt", "r") as file:
#     for line in file:
#         print("Line:", line.strip())   

# from datetime import datetime

# from datetime import datetime

# data = input("Enter a message or type 'view' to see the log: ")

# # If user wants to view the file
# if data.lower() == "view":
#     try:
#         with open("file.txt", "r") as file:
#             content = file.read()
#             print("\n--- Log Contents ---")
#             print(content)
#     except FileNotFoundError:
#         print("No log file found yet.")

# elif data.lower() == "delete":
#     open("file.txt", "w").close()
#     print("Log cleared: ")

# elif data.lower().startswith("hello"):
#     keyword = data[7:]
#     try:
#         with open("file.txt", "r") as file:
#             found = False
#             for line in file:
#                 if keyword.lower() in line.lower():
#                     print(line.strip())
#                     found = True
                
#                 if not found:
#                     print(f"No logs found under '{keyword}'")
    
#     except FileNotFoundError:
#         print("Log file not found")
# else:
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     with open("file.txt", "a") as file:
#         file.write(f"[{timestamp}] {data}\n")
#         print(f"Message saved: [{timestamp}] {data}")




