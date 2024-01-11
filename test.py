import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

def main():
    while True:
        user_input = input(">> ")
        if user_input.lower() == "exit":
            break
        output = run_command(user_input)
        print(output)

if __name__ == "__main__":
    main()
