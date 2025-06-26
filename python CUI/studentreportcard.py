students = {} #empty dict to store the values

while True:
    print("\n ---student report system---")
    print("1. Add Student")
    print("2. view all students")
    print("3. show topper result")
    print("4. Exit")

    choice = input("Enter your choice(1-4):\n")

    if choice == "1":
        name = input("Enter the student name:")

        math = int(input("Enter the maths marks:\n"))
        science = int(input("Enter the science marks:\n"))
        english = int(input("Enter the english marks:\n"))

        students[name] = {
            "maths": math,
            "science": science,
            "english": english
        }

        print(f"Student {name} added successfully")

    elif choice == "2":
        if not students:
            print("No students added yet...")
        else:
            for name, marks in students.items():
                print(f"\nStudents: {name}")
                for subject, score in marks.items():
                    print(f" {subject}: {score}")

    elif choice == "3":
        if not students:
            print("No students added yet...")
        else:
            topper_name = ''
            highest_avg = 0

            for name, marks in students.items():
                total = sum(marks.values())
                avg = total/len(marks)

                if avg > highest_avg:
                    highest_avg = avg
                    topper_name = name

            print(f"\nTopper:{topper_name} with average marks {round(highest_avg, 2)} ")

    elif choice == "4":
        print("Exiting program, Goodbye!")

        break 

    else:
        print("Invalid choice...!")
    

