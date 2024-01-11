from commands import CustomCommands

def main():
    custom_terminal = CustomCommands()

    while True:
        user_input = input(">> ")

        if user_input.lower() == "exit":
            break

        custom_terminal.execute_command(user_input)

if __name__ == "__main__":
    main()
