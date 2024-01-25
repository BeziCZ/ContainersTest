import random
import string

# Function for generating random string with length of 100 characters
if __name__ == "__main__":
    print("Generating random text:")
    print(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k = 100)))
