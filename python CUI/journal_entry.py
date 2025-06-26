from datetime import datetime

def add_entry():
    entry = input("Write your Journal:\n")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Fixed datetime usage
    with open("journal.txt", "a") as file:  # Changed to 'a' to append, not overwrite
        file.write(f"[{timestamp}] {entry}\n")
    print("Entry added\n")

def view_entries():
    try:
        with open("journal.txt", "r") as file:  # Make sure file name matches
            content = file.read()
            print("\n--- Your Journal ---")
            print(content)
    except FileNotFoundError:
        print("Journal file not found.\n")

def search_entries():
    keyword = input("Enter keyword to search:\n").lower()
    try:
        with open("journal.txt", "r") as file:  # 'r' not 's', and correct filename
            found = False
            for line in file:
                if keyword in line.lower():
                    print(line.strip())
                    found = True
            if not found:
                print("No matching entries found.\n")  # Moved outside the loop
    except FileNotFoundError:
        print("Journal file not found.\n")

def delete_entries():
    confirm = input("Are you sure you want to delete all entries? (yes/no):\n").lower()
    if confirm == "yes":
        open("journal.txt", "w").close()
        print("All entries deleted.\n")
    else:
        print("Deletion cancelled.\n")

def main():
    while True:
        print("Menu: add, view, search, delete, exit")
        choice = input("Choose an option:\n").lower()

        if choice == "add":
            add_entry()
        elif choice == "view":
            view_entries()
        elif choice == "search":
            search_entries()
        elif choice == "delete":
            delete_entries()
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please try again.\n")

if __name__ == "__main__":
    main()
