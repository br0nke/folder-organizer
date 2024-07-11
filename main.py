import PySimpleGUI as sg
import os

def organize_files(folder_path):
    """
    Organizes files in a folder by moving them into subfolders based on their extensions.

    Args:
        folder_path (str): The path to the folder containing the files to organize.
    """

    subfolders = {"images": [".jpg", ".jpeg", ".png", ".gif", ".bmp",],
                  "videos": [".mp4", ".avi", ".wmv", ".mkv", ".mov"],
                  "documents": [".pdf", ".docx", ".xlsx", ".pptx", ".odt", ".ods", ".odp"]}
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()
            for subfolder, extensions in subfolders.items():
                if extension in extensions:
                    target_folder = os.path.join(folder_path, subfolder)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    os.rename(file_path, os.path.join(target_folder, filename))
                    break  

def main():
    layout = [
        [sg.Text("Select a folder to organize:")],
        [sg.Input(), sg.FolderBrowse()],
        [sg.Button("Organize")]
    ]

    window = sg.Window("File Organizer", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "Organize":
            selected_folder = values[0]
            if selected_folder:
                try:
                    organize_files(selected_folder)
                    sg.popup("Files organized successfully!", title="Success")
                except Exception as e:
                    sg.popup(f"Error organizing files: {str(e)}", title="Error")

    window.close()

if __name__ == "__main__":
    main()