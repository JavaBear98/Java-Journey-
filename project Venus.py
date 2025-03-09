#Ask for the person's name
name= input("What is your name?")
print("Hello", name, "It is nice to meet you!")
#Ask for the person's birth year and store it
birth_date = int(input("When were you born?"))
print(birth_date)
#Calculate the person's age
current_year = 2025
age = current_year - birth_date
print("You are", age, "years old")
#Ask the user if they want to find out what their age is on Venus
venus_years = 0.62 * age #a year on Venus is 0.62 times a year on Earth
response = input("Would you like to find out your age on Planet Venus?")
if response == "yes":
  print("Your age on Venus is", venus_years)
if response == "no":
  print("I guess you prefer having your feet on the ground.")



