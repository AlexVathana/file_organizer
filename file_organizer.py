import os
import shutil

FILE_CATEGORIES = {
    'Images': ['jpg', 'jpeg', 'png', 'gif'],
    'Documents': ['pdf', 'docx', 'txt'],
    'Audio': ['mp3', 'wav'],
    'Videos': ['mp4', 'mov'],
    'Archives': ['zip', 'tar', 'gz'],
}

# Folder where files are currently located
source_folder = 'C:\\Users\\pvath\\OneDrive\\Desktop\\test'


def get_file_extension(file_name):
    return file_name.split('.')[-1].lower()


def organize_files(source_folder):
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        file_extension = get_file_extension(file_name)

        # Find the corresponding folder based on the extension
        moved = False
        for folder, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                destination_folder = os.path.join(source_folder, folder)

                # Create the folder if it doesn't exist
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                # Move the file to the corresponding folder
                shutil.move(file_path, os.path.join(destination_folder, file_name))
                print(f'Moved: {file_name} -> {folder}')
                moved = True
                break

        # If no matching extension is found, move the file to an "Other" folder
        if not moved:
            other_folder = os.path.join(source_folder, 'Other')
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, os.path.join(other_folder, file_name))
            print(f'Moved: {file_name} -> Other')

if __name__ == '__main__':
    organize_files(source_folder)
