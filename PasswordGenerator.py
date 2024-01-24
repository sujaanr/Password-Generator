import random
import string

# A function to shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# Main program starts here

# Generate 10 digits
digits = ''.join(random.choice(string.digits) for _ in range(10))

# Generate password using all the digits, in random order
length = int(input("Enter the password length: "))
password = ''.join(random.choice(string.digits) for _ in range(length))

# Output
print(password)

# Save to an output file
with open('passwords.txt', 'w') as file:
    file.write('\n'.join(password))
