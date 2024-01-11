import subprocess

class CustomGitOperations:
    def custom_git(self, command):
        try:
            # Execute the Git command and capture the output
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Display the Git command and its output
            print(f"Executing Git command: {command}\n")

            if result.stdout:
                print("Output:")
                print(result.stdout)

            if result.stderr:
                print("\nError:")
                print(result.stderr)

            print("\nCommand executed successfully.")

        except subprocess.CalledProcessError as e:
            print(f"Error executing Git command: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")

    def custom_git_pull(self):
        try:
            # Execute the 'git pull' command
            result = subprocess.run("git pull", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Display the result of the 'git pull' command
            print("Performing custom Git pull\n")

            if result.stdout:
                print("Output:")
                print(result.stdout)

            if result.stderr:
                print("\nError:")
                print(result.stderr)

            print("\nGit pull completed successfully.")

        except subprocess.CalledProcessError as e:
            print(f"Error performing Git pull: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")

    def custom_git_push(self):
        try:
            # Execute the 'git push' command
            result = subprocess.run("git push", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Display the result of the 'git push' command
            print("Performing custom Git push\n")

            if result.stdout:
                print("Output:")
                print(result.stdout)

            if result.stderr:
                print("\nError:")
                print(result.stderr)

            print("\nGit push completed successfully.")

        except subprocess.CalledProcessError as e:
            print(f"Error performing Git push: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")
