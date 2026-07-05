print("===== EXPENSE TRACKER =====")

total = 0

while True:
    expense = input("Enter expense (or type 'quit' to finish): ")

    if expense.lower() == "quit":
        break

    try:
        expense = int(expense)

        total += expense

        print("Current Total:", total)

    except ValueError:
        print("Invalid Input! Please enter numbers only.")

print("\n===== FINAL REPORT =====")
print("Final Total Expense:", total)
print("Thank you for using Expense Tracker!")
