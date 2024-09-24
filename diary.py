import json
from datetime import datetime

DIARY_FILE = 'diary_entries.json'

def load_entries():
    try:
        with open(DIARY_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_entries(entries):
    with open(DIARY_FILE, 'w') as file:
        json.dump(entries, file)

def add_entry(entries):
    content = input("Enter your diary entry: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entries.append({'timestamp': timestamp, 'content': content})
    save_entries(entries)
    print("Entry added!")

def view_entries(entries):
    if not entries:
        print("No entries found.")
    else:
        for index, entry in enumerate(entries):
            print(f"{index + 1}. [{entry['timestamp']}] {entry['content']}")

def delete_entry(entries):
    view_entries(entries)
    try:
        entry_num = int(input("Enter the number of the entry to delete: ")) - 1
        if 0 <= entry_num < len(entries):
            entries.pop(entry_num)
            save_entries(entries)
            print("Entry deleted!")
        else:
            print("Invalid entry number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    entries = load_entries()

    while True:
        print("\nPersonal Diary Application")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Delete Entry")
        print("4. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            add_entry(entries)
        elif choice == '2':
            view_entries(entries)
        elif choice == '3':
            delete_entry(entries)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
