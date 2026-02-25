while True:
    try:
        print("\n--- Simple Calculator ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 5:
            print("Exiting program. Bye 👋")
            break

        if choice not in [1, 2, 3, 4]:
            print("❌ Invalid menu choice")
            continue

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if choice == 1:
            print("Result:", a + b)

        elif choice == 2:
            print("Result:", a - b)

        elif choice == 3:
            print("Result:", a * b)

        elif choice == 4:
            print("Result:", a / b)

    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero")

    except ValueError:
        print("❌ Error: Please enter valid numbers")

    except Exception as e:
        print("❌ Unexpected Error:", e)

    finally:
        print("✔ Operation completed")
