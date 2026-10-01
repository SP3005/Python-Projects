import os
from datetime import datetime
class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename
    def add_entry(self):
        try:
            entry = input("\nEnter your journal entry: ").strip()
            if entry == "":
                print("Error: Journal entry cannot be empty.")
                return
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(f"[{timestamp}]\n")
                file.write(f"{entry}\n\n")
            print("\nEntry added successfully!")
        except PermissionError:
            print("Error: Permission denied. Cannot write to the journal file.")
        except OSError as error:
            print("Error while writing to the journal file:", error)
        except Exception as error:
            print("Unexpected error:", error)
    def view_entries(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()
                if content.strip() == "":
                    print("\nNo journal entries found.")
                    return
                print("\nYour Journal Entries:")
                print("-" * 35)
                print(content)
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Error: Permission denied. Cannot read the journal file.")
        except OSError as error:
            print("Error while reading the journal file:", error)
        except Exception as error:
            print("Unexpected error:", error)
    def search_entry(self):
        try:
            keyword = input("\nEnter a keyword or date to search: ").strip()
            if keyword == "":
                print("Error: Search keyword cannot be empty.")
                return
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()
            if content.strip() == "":
                print("\nNo journal entries found.")
                return
            entries = content.strip().split("\n\n")
            matching_entries = []
            for entry in entries:
                if keyword.lower() in entry.lower():
                    matching_entries.append(entry)
            if len(matching_entries) > 0:
                print("\nMatching Entries:")
                print("-" * 35)
                for entry in matching_entries:
                    print(entry)
                    print()
            else:
                print(f"\nNo entries were found for the keyword: {keyword}.")
        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")
        except PermissionError:
            print("Error: Permission denied. Cannot read the journal file.")
        except OSError as error:
            print("Error while searching the journal file:", error)
        except Exception as error:
            print("Unexpected error:", error)
    def delete_all_entries(self):
        try:
            if not os.path.exists(self.filename):
                print("\nNo journal entries to delete.")
                return
            confirmation = input("\nAre you sure you want to delete all entries? (yes/no): ").strip().lower()
            if confirmation == "yes":
                with open(self.filename, "w", encoding="utf-8") as file:
                    file.write("")
                os.remove(self.filename)
                print("\nAll journal entries have been deleted.")
            elif confirmation == "no":
                print("\nDelete operation cancelled.")
            else:
                print("\nInvalid input. Please enter yes or no.")
        except PermissionError:
            print("Error: Permission denied. Cannot delete the journal file.")
        except OSError as error:
            print("Error while deleting the journal file:", error)
        except Exception as error:
            print("Unexpected error:", error)
    def demonstrate_create_mode(self):
        try:
            with open(self.filename, "x", encoding="utf-8") as file:
                file.write("")
            print("\nJournal file created successfully using 'x' mode.")
        except FileExistsError:
            print("\nJournal file already exists. 'x' mode cannot create an existing file.")
        except PermissionError:
            print("Error: Permission denied.")
        except OSError as error:
            print("Error:", error)
    def display_menu(self):
        while True:
            print("+------------------------------------+")
            print("|      PERSONAL JOURNAL MANAGER      |")
            print("+------------------------------------+")
            print("|1. Add a New Entry                  |")
            print("|2. View All Entries                 |")
            print("|3. Search for an Entry              |")
            print("|4. Delete All Entries               |")
            print("|5. Exit                             |")
            print("+------------------------------------+")
            choice = input("Please select an option: ").strip()
            if choice == "1":
                self.add_entry()
            elif choice == "2":
                self.view_entries()
            elif choice == "3":
                self.search_entry()
            elif choice == "4":
                self.delete_all_entries()
            elif choice == "5":
                print("\nThank you for using Personal Journal Manager. Goodbye!")
                break
            else:
                print("\nInvalid option. Please select a valid option from the menu.")

journal = JournalManager()
journal.display_menu()