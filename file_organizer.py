import os
import shutil

FILE_CATEGORIES = {
    'Images': ['jpg', 'jpeg', 'png', 'gif'],
    'Documents': ['pdf', 'docx', 'txt'],
    'Music': ['mp3', 'wav'],
    'Videos': ['mp4', 'mov'],
    'Compressed': ['zip', 'tar', 'gz'],
    'Programs': ['exe']
}


source_folder = 'C:\\Users\\Downloads'


def get_file_extension(file_name):
    return file_name.split('.')[-1].lower()


def organize_files(source_folder):
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)


        if os.path.isdir(file_path):
            continue


        file_extension = get_file_extension(file_name)


        moved = False
        for folder, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                destination_folder = os.path.join(source_folder, folder)


                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)


                shutil.move(file_path, os.path.join(destination_folder, file_name))
                print(f'Moved: {file_name} -> {folder}')
                moved = True
                break

        if not moved:
            other_folder = os.path.join(source_folder, 'Other')
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, os.path.join(other_folder, file_name))
            print(f'Moved: {file_name} -> Other')


if __name__ == '__main__':
    organize_files(source_folder)
