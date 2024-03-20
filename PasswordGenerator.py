import random
import string

# A pure function to shuffle all the characters of a string and return a new string
def shuffle_str(s):
    tempList = list(s)
    shuffledList = random.sample(tempList, len(tempList))
    return ''.join(shuffledList)

# A function to generate a random digits string of a given length
def generate_random_digits(length):
    return ''.join(random.choice(string.digits) for _ in range(length))

# A function to generate a password of a given length
def generate_password(length):
    digits = generate_random_digits(length)
    return shuffle_str(digits)

# Function to save password to a file
def save_password_to_file(password, filename):
    with open(filename, 'w') as file:
        file.write(password + '\n')

# Main program
if __name__ == "__main__":
    length = int(input("Enter the password length: "))
    password = generate_password(length)
    print(password)
    save_password_to_file(password, 'passwords.txt')
