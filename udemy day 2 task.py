print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age >= 18:
        bill = 12
        print("Adult tickets are $12")
    elif age <= 16:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 5
        print("Child tickets are of $5")

    wants_photo = input("do you want to have a photo take? Type y for yes and n for no.")
    if wants_photo == "y":
            # Add $3 to their bill
           bill += 3

    print(f"your final bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
