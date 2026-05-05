from passwordGenerator import PasswordGenerator

if __name__ == "__main__":
    passwordGenerator = PasswordGenerator(5, count=5)

    print(f"Current next = {passwordGenerator.current}")
    print(next(passwordGenerator))
    print(f"Current next = {passwordGenerator.current}")
    print(next(passwordGenerator))

    for password in passwordGenerator:
        print(f"Current for = {passwordGenerator.current}")
        print(password)