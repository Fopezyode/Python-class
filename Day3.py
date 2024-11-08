print("Welcome to the Roller Coaster")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the Roller Coaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child tickets are $5. ")
        bill  = 5
    elif age <= 18:
        print("Teenager tickets are $7. ")
        bill = 7
    elif age <= 25:
        print("Young Adults ticket are $15")
        bill = 15
    else:
        print("Adults tickets are $30. ")
        bill = 30
    photo = input("Do you want to take a Photo? Type Y for Yes and N for No.")
    if photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("You have to grow before you can ride")
