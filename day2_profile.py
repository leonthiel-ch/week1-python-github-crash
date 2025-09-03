### Generates a profile based on user input

name = input("Enter your name: ")
age = int(input("Enter your age: "))
foods = input("Enter your favorite foods (comma-separated): ").split(',')
foods = set([food.strip() for food in foods])

profile = {
    "name": name,
    "age": age,
    "foods": foods
}

print("Hello " + profile["name"] + "! You are " + str(profile["age"]) + " years old.\nYour favorite foods are: " + str(profile["foods"]))