import random
import string
import sys


# Function for generating random string of specified length and specified exit code
if __name__ == "__main__":
    print("Generating random text:")
    if len(sys.argv) > 1:
        print(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k = int(sys.argv[1]))))
    else:
        print("Length not specified using default value")
        print(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k = 100)))
    if len(sys.argv) > 2:
        sys.exit(int(sys.argv[2]))
    else:
        sys.exit(0)