import os

def create_folders():
    directory = input("Enter the directory where you want to create the folders (e.g., C:\\Users\\YourName\\Desktop): ")

    folder_names_input = input("Enter folder names separated by commas (e.g., books, objects): ")

    folder_names = [name.strip() for name in folder_names_input.split(',')]

    for folder_name in folder_names:
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder '{folder_name}' created at: {folder_path}")
        else:
            print(f"Folder '{folder_name}' already exists.")

if __name__ == "__main__":
    create_folders()