#This program was made by Dhyey Dave of 10k
import requests
import hashlib
def check_password(password):
    # Hash the password using SHA-1
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]

    # Send the first 5 characters of the hash to the HIBP API to receive a list of matching hashes
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error connecting to the HIBP API")
        return

    # Check if the rest of the hash (suffix) exists in the list of matching hashes
    for line in response.text.splitlines():
        parts = line.split(':')
        if parts[0] == suffix:
            count = int(parts[1])
            if count > 0:
                print(f"This password has been seen in {count} data breaches.")
                return

    print("This password is safe!")

if __name__ == "__main__": #This block is used to contain code that should only run when the script is the main program, and not when it's imported as a module.
    password = input("Enter a password to check: ")
    check_password(password)