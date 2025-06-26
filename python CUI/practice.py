from datetime import datetime

def add_entries():
    entry = input("enter your journal entry:\n")
    timestamp = datetime.now().strftime("%Y-%mn-%D %H:%M:%S")
    with open("practice.txt", "a") as file:
        file.write(f"[{timestamp}] {entry}\n")
        print("entry added in journal successfully:\n ")

def view_entries():
    try:
        with open("practice.txt", "r") as file:
            content = file.read()
            print("\n----Your Journal---\n")
            print(content)
    except FileNotFoundError:
        print("No entry found in Journal:\n")

def search_entries():
    keyword = input("enter the keyword of yours:\n").lower()
    try:
        with open("practice.txt", "r") as file:
            found = False
            for line in file:
                if keyword in line.lower():
                    print(line.strip())
                    found = True
            if not found :
                print("No matching entries found in Journal:\n")
    except FileNotFoundError:
        print("Journal does not exist:\n")

def delete_entries():
    try:
        with open("practice.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No lines found:\n")
            return
        
        for index, line in enumerate(lines, start=1):
            print(f"{index} {line.strip()}")

        choice = int(input("Enter the number you wanted to delete:\n"))

        if 1 <= choice <= len(line):
            with open("practice.txt", "w") as file:
                for index, line in enumerate(lines, start=1):
                    if index != choice:
                        file.write(line)
            print("entry deleted successfull:\n")
        else:
            print("invalid  number:\n")

    except FileNotFoundError:
        print("Journal not found:\n")

    except ValueError:
        print("please enter a valid value:\n")

  
def main():
    while True:
        print("Menu: add, view, search, delete, exit")
        choice = input("choose an option:\n").lower()

        if choice == "add":
            add_entries()
        elif choice == "view":
            view_entries()
        elif choice == "search":
            search_entries()
        elif choice == "delete":
            delete_entries()
        elif choice == "exit":
            print("Goodbye !!")
            break 
        else:
            print("Invalid option!! please try again:\n")

if __name__ == "__main__":
    main()




