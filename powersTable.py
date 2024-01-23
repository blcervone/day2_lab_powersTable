# Print formatted title
print("Learn your squares and cubes!")
print()

# Initialize flag variable
keep_going = 'y'

# Launch while loop for main program, condition on flag variable
while keep_going != 'n':
    # Ask user for integer input (assume they follow directions)
    user_input = int(input("Enter an integer: "))
    print()
    # Print formatted table headers
    print("Number\tSquared\tCubed")
    print("=======\t=======\t=======")
    # Launch for loop to iterate through range given by user input
    for i in range(1, user_input + 1):
        # Print formatted values for number, square, and cube
        print(f"{i}\t\t{i ** 2}\t\t{i ** 3}")
    print()
    # Print formatted multiplication table header row 1 using for loop
    for a in range(1, user_input + 1):
        print(f"\t{a}", end=' ')
    print()
    # Print formatted multiplication table header row 2 using for loop
    for b in range(1, user_input + 1):
        print("\t=", end=' ')
    print()
    # Print rows using double for loop (FORMATTING ISSUES WITH LARGE NUMBERS)
    for x in range(1, user_input + 1):
        print(f"{x} |", end=' ')
        for y in range(1, user_input + 1):
            print(f"{x * y}", end='\t')
        print()
    print()
    # Ask user to continue main program while loop, end loop if 'n'
    keep_going = input("Continue? (y/n) ")
    print()