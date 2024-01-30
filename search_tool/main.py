

def main():
    print("------------------------------------------")
    print("Welcome to the Stack Overflow Search Tool!")
    print("------------------------------------------")
    print()

    print("                 You'll have 3 options:")
    print("-------------------------------------------------------------")
    print("1) If you would like to access a small block of code type: 'b'")
    print("2) If you would like to check you error specifically type: 's'")
    print("3) To exit the program type: 'q'")
    print("-------------------------------------------------------------")

    user_input = input("Type - b/s/q: ")

    while True:
        if user_input == "b":
            pass
        elif user_input == "s":
            pass
        elif user_input == "q":
            exit()
        else:
            pass
main()