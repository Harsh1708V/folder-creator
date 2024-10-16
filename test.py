import os

def create_folders():
    directory = input("Enter the directory where you want to create the folders (e.g., C:\\Users\\YourName\\Desktop): ")

    folder_names_input = input("Enter folder names separated by commas (e.g., books, objects): ")
    folder_names = [name.strip() for name in folder_names_input.split(',')]

    created_folders = {}

    # Create folders
    for folder_name in folder_names:
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            created_folders[folder_name] = folder_path
            print(f"Folder '{folder_name}' created at: {folder_path}")
        else:
            print(f"Folder '{folder_name}' already exists.")

    # Ask the user if they want to rename folders or exit
    user_choice = input("\nDo you want to rename folders or exit? Type 'rename' to rename or 'exit' to quit: ").lower()

    if user_choice == 'rename':
        rename_folders(created_folders, directory)
    elif user_choice == 'exit':
        print("Exiting the program.")
    else:
        print("Invalid choice. Exiting the program.")

def rename_folders(created_folders, directory):
    # Get the number of folders the user wants to rename
    total_folders = len(created_folders)
    print(f"\nTotal folders available: {total_folders}")

    rename_count = int(input(f"How many folders would you like to rename (max {total_folders})? "))

    # Ensure the rename count is valid
    if rename_count <= 0 or rename_count > total_folders:
        print(f"Please enter a number between 1 and {total_folders}.")
        return

    # Get the folder names to rename
    print("\nExisting folders: ", ', '.join(created_folders.keys()))
    selected_folders_input = input(f"Enter {rename_count} folder names you want to rename, separated by commas: ")
    selected_folders = [name.strip() for name in selected_folders_input.split(',')]

    if len(selected_folders) != rename_count:
        print(f"You must select exactly {rename_count} folders to rename.")
        return

    # Validate if the selected folders exist
    for folder in selected_folders:
        if folder not in created_folders:
            print(f"Folder '{folder}' does not exist. Please enter valid folder names.")
            return

    # Get new names from the user
    new_names_input = input(f"Enter {rename_count} new names for the selected folders, separated by commas: ")
    new_names = [name.strip() for name in new_names_input.split(',')]

    if len(new_names) != rename_count:
        print(f"You must provide exactly {rename_count} new names.")
        return

    # Rename the selected folders
    for i, old_folder in enumerate(selected_folders):
        old_folder_path = created_folders[old_folder]
        new_folder_name = new_names[i]
        new_folder_path = os.path.join(directory, new_folder_name)

        # Handle case-insensitive renaming by renaming to a temporary name first if necessary
        if old_folder.lower() == new_folder_name.lower():
            temp_folder_path = os.path.join(directory, old_folder + "_temp")
            os.rename(old_folder_path, temp_folder_path)  # Rename to temporary
            os.rename(temp_folder_path, new_folder_path)  # Rename to final name
            print(f"Renamed folder '{old_folder}' to '{new_folder_name}' (handled case sensitivity).")
        elif not os.path.exists(new_folder_path):
            os.rename(old_folder_path, new_folder_path)
            print(f"Renamed folder '{old_folder}' to '{new_folder_name}'")
        else:
            print(f"Folder with the name '{new_folder_name}' already exists. Skipping.")

        # Update the created_folders dictionary with the new name
        del created_folders[old_folder]
        created_folders[new_folder_name] = new_folder_path

if __name__ == "__main__":
    create_folders()
