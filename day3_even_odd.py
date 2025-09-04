while True:
    number = input("Enter a number (or q to quit): ")
    if number == "q":
        print("Goodbye!")
        break
    elif int(number)%2 == 0:
        print(str(number) + " is Even.")
    else:
        print(str(number) + " is Odd.")