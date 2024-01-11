import shutil
import os
from tabulate import tabulate

class CustomFileOperations:
    def custom_copy(self, source, destination):
        try:
            # Check if the source file exists
            if not os.path.isfile(source):
                raise FileNotFoundError(f"Source file '{source}' not found.")

            # Check if the destination directory exists, create it if not
            destination_dir = os.path.dirname(destination)
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)

            # Perform the file copy
            shutil.copy(source, destination)

            print(f"Successfully copied {source} to {destination}")
        except Exception as e:
            print(f"Error during copy: {e}")

    def custom_delete(self, file_path):
        try:
            # Check if the file exists
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"File '{file_path}' not found.")

            # Perform the file deletion
            os.remove(file_path)

            print(f"Successfully deleted {file_path}")
        except Exception as e:
            print(f"Error during deletion: {e}")

    def custom_move(self, source, destination):
        try:
            # Check if the source file exists
            if not os.path.isfile(source):
                raise FileNotFoundError(f"Source file '{source}' not found.")

            # Check if the destination directory exists, create it if not
            destination_dir = os.path.dirname(destination)
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)

            # Perform the file move (or rename) operation
            shutil.move(source, destination)

            print(f"Successfully moved {source} to {destination}")
        except Exception as e:
            print(f"Error during move: {e}")

    def custom_list_files(self, directory=".", show_details=False):
        try:
            # Get a list of files in the specified directory
            files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

            if not show_details:
                # Display a simple list of file names
                print("Listing files in", directory)
                for file_name in files:
                    print(file_name)
            else:
                # Display a detailed table with file information
                file_details = [(f, os.path.getsize(os.path.join(directory, f)), os.path.getctime(os.path.join(directory, f))) for f in files]

                # Sort files based on creation time (oldest to newest)
                sorted_files = sorted(file_details, key=lambda x: x[2])

                # Prepare data for tabulate
                table_data = [{"File": file_name, "Size (bytes)": size, "Date Created": self.format_creation_time(creation_time)} for file_name, size, creation_time in sorted_files]

                # Display the table
                print(tabulate(table_data, headers="keys", tablefmt="pretty"))
        except Exception as e:
            print(f"Error during file listing: {e}")

    def format_creation_time(self, timestamp):
        return str(timestamp)  # You can customize the date format as needed

    def custom_create_directory(self, directory_name):
        try:
            # Check if the directory already exists
            if os.path.exists(directory_name):
                raise FileExistsError(f"Directory '{directory_name}' already exists.")

            # Create the directory
            os.makedirs(directory_name)

            print(f"Successfully created directory: {directory_name}")
        except Exception as e:
            print(f"Error during directory creation: {e}")