import random
import string

if __name__ == "__main__":
    print("Generating random text:")
    print(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k = 100)))
