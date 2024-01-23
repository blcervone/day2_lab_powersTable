# Print formatted title
print("Learn your squares and cubes!")
print()

# Initialize flag variable
keep_going = 'y'

# Launch while loop for main program, condition on flag variable
while keep_going != 'n':
    # Ask user for integer input (assume they follow directions)
    user_input = int(input("Enter and integer: "))
    print()
    # Print formatted table headers
    print("Number\tSquared\tCubed")
    print("=======\t=======\t=======")
    # Launch for loop to iterate through range given by user input
    for i in range(1, user_input + 1):
        # Print formatted values for number, square, and cube
        print(f"{i}\t\t{i ** 2}\t\t{i ** 3}")
    print()
    # Ask user to continue, end loop if 'n'
    keep_going = input("Continue? (y/n)")
    print()