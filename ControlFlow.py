# Programmer: Mr. Lange
# Date: 12.16.19
# Program: Guess My Number

myNumber = 7

print("\nGuess a number between 1 & 10\n")

# Ask users to guess
guess = int(input("Enter a Guess: "))

# Keep asking users to guess my number until
# it is equal to myNumber
while guess != myNumber:
    print("\nNope, guess again: ")
    guess = int(input("Enter a Guess: "))

print("\nCongratulations, you guessed my number!!!\n")




# Programmer: Mr. Lange
# Date: 12.19.19
# Program: 1 - 10

x = 1

# While loop will see if a condition has been met
# If not is will run again until the condition
# has been met

while x <= 10:
    print(x)
    x+=1



# Programmer: Mr. Lange
# Date: 1.6.20
# Program: Running Total, Part II

# This program asks users for five numbers
# It then sums up the numbers


sum = 0
how_many_numbers = int(input("\nHow many numbers would you like to sum up: "))
print("")

for i in range(how_many_numbers):
    enter_a_number = int(input("Enter a number: "))
    sum = sum + enter_a_number

print("\nSum of your numbers is: " + str(sum))



# Programmer: Mr. Lange
# Date: 1.7.20
# Program: Average Test Scores

# This program asks users how many tests they wish to average


total = 0
how_many_tests = int(input("\nHow many tests would you like to average: "))
print("")

for i in range(how_many_tests):
    enter_a_score = float(input("Enter a score: "))
    total = total + enter_a_score

average = total / how_many_tests

print("\nAverage: " + str(round(average, 2)))

