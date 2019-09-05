# Take an input of numbers.
# Stop the program when a negative number is written.
# When a negative number is entered find the highest number of the input.
# Print out the higest value.

num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = 0
while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    num_int = int(input("input a number: "))
print("The maximum is", max_int)    # Do not change this line