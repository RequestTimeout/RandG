from string import ascii_letters, digits
import random


allowed = ascii_letters + digits + "@"
UUID_allowed = "0123456789abcdef"
print("1. Number\n2. Password\n3. UUID\n")
inp = input(">>> ")

match inp:
    case "1":
        while True:
            try:
                l = int(input("Minimum: "))
                h = int(input("Maximum: "))
                print("Generated: " + str(random.randint(l, h)) + " for number in range [{}, {}]".format(l, h))
                break
            except ValueError:
                print("Invalid input")
    case "2":
        while True:
            try:
                length = int(input("Enter the password length: "))
                password = []
                for i in range(length):
                    password.append(random.choice(allowed))
                print("Generated: " + "".join(password) + " for password with a length of {}".format(length))
                break
            except ValueError:
                print("Invalid input")
    case "3":
        UUID = []
        for i in range(32):
            if i == 8 or i == 12 or i == 16 or i == 20:
                UUID.append("-")
            UUID.append(random.choice(UUID_allowed))
        UUID[14] = "4"
        UUID[19] = random.choice("89ab")
        print("Generated: " + "".join(UUID) + " for UUID")
    case _:
        print("Error: Invalid input")

print("\nmade by: Request Timeout(GitHub: https://github.com/RequestTimeout)")
