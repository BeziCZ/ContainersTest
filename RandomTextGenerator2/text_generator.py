import random
import string
import sys

# Function for generating random string of specified length if length is not provided it deafults to 100
if __name__ == "__main__":
    print("Generating random text:")
    if len(sys.argv) > 1:
        print(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k = int(sys.argv[1]))))
    else:
        print("Length not specified using default value")
        print(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k = 100)))