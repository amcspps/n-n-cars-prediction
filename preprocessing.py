import os

def handle_data(folder_path):
    files = os.listdir(folder_path)
    files.sort()

    photo_index = 0

    for file_name in files:
        if file_name.endswith(('.jpg', '.jpeg', '.png')):
            photo_index += 1

            if photo_index % 10 != 0:
                file_path = os.path.join(folder_path, file_name)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

main_directory = 'D:\dev\dataset_preprocessing\Insight-MVT_Annotation_Train'

for folder_name in os.listdir(main_directory):
    folder_path = os.path.join(main_directory, folder_name)

    if os.path.isdir(folder_path):
        print(f"\nProcessing folder: {folder_path}")
        handle_data(folder_path)