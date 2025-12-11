import os
import csv

class FeeRecord:
    def __init__(self, student_id, amount, status="Paid"):
        self.student_id = student_id
        self.amount = amount
        self.status = status

class FeeManager:
    def __init__(self):
        self.records = []
        self.count = 0

    def submit_fee(self, student_id, amount):
        # 7. Fee Submission Validation
        try:
            amount = float(amount)
            if amount <= 0:
                return False, "Please enter a valid fee amount."
        except ValueError:
             return False, "Please enter a valid fee amount."

        new_record = FeeRecord(student_id, amount)
        self.records.append(new_record)
        self.count += 1
        return True, "Fee submitted successfully!"

    def display_all(self):
        if self.count == 0:
            print("\nNo fee records found!")
            return

        print("\n--- All Fee Records ---")
        print(f"{'Student ID':<15}{'Amount':<15}{'Status':<15}")
        print("-" * 45)

        for record in self.records:
            print(f"{record.student_id:<15}{record.amount:<15.2f}{record.status:<15}")
        
        print(f"\nTotal Records: {self.count}")

    def add_fee_record(self):
        print("\n--- Submit Fee ---")
        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid ID format!")
            return

        try:
            amount = float(input("Enter Fee Amount: "))
        except ValueError:
            print("Invalid amount format!")
            return

        success, message = self.submit_fee(student_id, amount)
        print(f"\n{message}")

    def save_to_file(self):
        try:
            with open("fees.csv", "w", newline='') as file:
                writer = csv.writer(file)
                for record in self.records:
                    writer.writerow([record.student_id, record.amount, record.status])
        except IOError as e:
            print(f"Error: Could not save to file! {e}")

    def load_from_file(self):
        if not os.path.exists("fees.csv"):
            return

        try:
            with open("fees.csv", "r", newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if not row:
                        continue
                    
                    if len(row) == 3:
                        student_id = int(row[0])
                        amount = float(row[1])
                        status = row[2]
                        new_record = FeeRecord(student_id, amount, status)
                        self.records.append(new_record)
                        self.count += 1
        except IOError:
            pass
        except ValueError:
            pass

    def menu(self):
        while True:
            print("\n--- Fee Record Management ---")
            print("1. Submit Fee")
            print("2. Display All Fee Records")
            print("3. Back to Main Menu")
            
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid choice! Please try again.")
                continue

            if choice == 1:
                self.add_fee_record()
            elif choice == 2:
                self.display_all()
            elif choice == 3:
                self.save_to_file()
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice! Please try again.")
