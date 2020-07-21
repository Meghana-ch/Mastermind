from random import randint


def check(n, g):
    global moveCounter
    inplace = 0
    outplace = 0
    num = [n0, n1, n2]
    guess = [g0, g1, g2]
    for inputs in num:
        for digits in guess:
            if inputs == digits:
                outplace += 1
                if num.index(inputs) == guess.index(digits):
                    inplace += 1
                    outplace -= 1
    print('''                                                                 In place  Out of place
                                                            --------  ------------
                     {0}.Your guess:,
                     {1}
                            You entered: {2}        {3}           {4} '''.format(moveCounter, g, g, inplace, outplace))
    moveCounter += 1
    if g == n:
        print("Correct answer! You win!")
        exit(1)
    elif g == 000:
        print(n)
    elif g == 999:
        print("Better luck next time.")
        exit(1)
    else:
        pass


print("                        ######################### Game Mastermind #############################")
print()
print()
print("                                 You have 10 moves to guess the number. Good luck!\n")
print('''NOTE: Input of 000 will display the hidden number & input of 999 exits the program.\n''')

choice = input("Press 's' to set the three digits, or 'r' to randomize them: ")
if choice == 's':
    n = int(input("Enter three distinct digits each in the range 0..9: "))
    n0 = (n % 1000) // 100
    n1 = (n % 100) // 10
    n2 = (n % 10)
elif choice == 'r':
    n = randint(100, 1000)
    n0 = (n % 1000) // 100
    n1 = (n % 100) // 10
    n2 = (n % 10)
else:
    print("Please enter either 's' or 'r'.")

moveCounter = 1
while moveCounter < 12:
    g = int(input("Please guess your 3 digit number: "))
    temp0 = (g % 1000)
    temp1 = (g % 100)
    temp2 = g % 10
    tempList = [temp0, temp1, temp2]

    while len(tempList) != 3:
        print("That is not a 3 digit number,please enter a 3 digit number only.")
        g = int(input("Please guess your 3 digit number:"))

    g0 = (g % 1000) // 100
    g1 = (g % 100) // 10
    g2 = (g % 10)
    check(n, g)

if moveCounter >11:
    print("All guesses have been used!")
    print("The hidden number was: %c" % n)

