from file_operations import CustomFileOperations
from git_operations import CustomGitOperations

class CustomCommands:
    def __init__(self):
        self.file_operations = CustomFileOperations()
        self.git_operations = CustomGitOperations()
        self.available_commands = [
            "copy", "delete", "move", "list_files", "create_directory",
            "git", "git_pull", "git_push"
        ]

    def execute_command(self, user_input):
        command_parts = user_input.split()
        base_command = command_parts[0].lower()

        if base_command == "exit":
            return

        # Auto-complete feature
        suggestions = [cmd for cmd in self.available_commands if cmd.startswith(base_command)]
        if len(suggestions) == 1:
            # If there is only one suggestion, complete the command
            user_input = f"{suggestions[0]} {' '.join(command_parts[1:])}"

        if base_command.startswith("copy"):
            _, source, destination = user_input.split()
            self.file_operations.custom_copy(source, destination)

        elif base_command.startswith("delete"):
            _, file_path = user_input.split()
            self.file_operations.custom_delete(file_path)

        elif base_command.startswith("move"):
            _, source, destination = user_input.split()
            self.file_operations.custom_move(source, destination)

        elif base_command.startswith("list_files"):
            # Optional: Handle directory argument if provided
            self.file_operations.custom_list_files()

        elif base_command.startswith("create_directory"):
            _, directory_name = command_parts
            self.file_operations.custom_create_directory(directory_name)

        elif base_command.startswith("git"):
            git_command = " ".join(command_parts[1:])
            self.git_operations.custom_git(git_command)

        elif base_command.startswith("git_pull"):
            self.git_operations.custom_git_pull()

        elif base_command.startswith("git_push"):
            self.git_operations.custom_git_push()

        else:
            print("Unknown command. Type 'exit' to quit.")
        
        # Optional: Print auto-complete suggestions
        if suggestions:
            print("Auto-complete suggestions:", suggestions)
