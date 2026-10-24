# Week 8 Final Project: Personal Mini-Toolkit


# Tool 1: Performs basic arithmetic on two numbers.
def simple_calculator():
    print("\n--- Simple Calculator ---")

    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))

        print("Choose an operation: +, -, *, /")
        operation = input("Operation: ").strip()

        if operation == "+":
            result = first + second
        elif operation == "-":
            result = first - second
        elif operation == "*":
            result = first * second
        elif operation == "/":
            if second == 0:
                print("You cannot divide by zero.")
                return
            result = first / second
        else:
            print(f"Sorry, '{operation}' is not a valid operation.")
            return

        print(f"Result: {first} {operation} {second} = {result}")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: Lets the user add, view, and remove tasks from a list.
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an action (1-4): ").strip()

        if choice == "1":
            task = input("Enter a task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task added: {task}")
            else:
                print("A task cannot be empty.")

        elif choice == "2":
            if tasks:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
            else:
                print("Your to-do list is empty.")

        elif choice == "3":
            if tasks:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                task_number = input(
                    "Enter the number of the task to remove: "
                ).strip()

                try:
                    index = int(task_number) - 1

                    if 0 <= index < len(tasks):
                        removed_task = tasks.pop(index)
                        print(f"Task removed: {removed_task}")
                    else:
                        print("That task number is not on your list.")

                except ValueError:
                    print("Please enter a valid whole number.")
            else:
                print("There are no tasks to remove.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please choose a number from 1 to 4.")


# Tool 3: Identifies whether a number is positive, negative, or zero.
def number_checker():
    print("\n--- Number Checker ---")

    try:
        number = float(input("Enter a number: "))

        if number > 0:
            print(f"{number} is positive.")
        elif number < 0:
            print(f"{number} is negative.")
        else:
            print("The number is zero.")

    except ValueError:
        print("Please enter a valid number.")


# Main program: Repeats the menu until the user chooses to quit.
def main():
    print("Welcome to My Personal Mini-Toolkit!")

    while True:
        print("\nPlease choose a tool:")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Checker")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            simple_calculator()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            number_checker()
        elif choice == "4":
            print("Thank you for using My Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print(f"Sorry, '{choice}' is not a valid choice. Please try again.")


if __name__ == "__main__":
    main()
