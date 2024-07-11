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
    
    