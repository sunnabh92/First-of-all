# Input a length of the sequence.
# Program will add together 3 last numbers in sequence to find the next number in the sequence.
# Prints out numbers one by one until the lenght of the sequence input.

n = int(input("Enter the length of the sequence: ")) # Do not change this line

A = 0
B = 1
count = 0
while count < n:
    C = A + B
    print(C)
    B = A
    A = C
    count +=1