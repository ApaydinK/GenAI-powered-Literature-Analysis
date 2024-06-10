"""
This module serves as the entry point to the PDF Summarizer APP.
"""

from src.Modern_GUI2 import GUI
import customtkinter


if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    app = GUI()
    app.mainloop()

import subprocess
import os


def open_file(file_path):
    """
    Opens a file using the default program associated with the file type on Windows.

    Parameters:
    file_path (str): The path to the file to be opened.
    """
    try:
        if os.path.exists(file_path):
            # Using start command to open the file with the default application
            subprocess.run(['start', '', file_path], shell=True, check=True)
            print(f"File {file_path} opened successfully.")
        else:
            print(f"File {file_path} does not exist.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to open file {file_path}. Error: {e}")


# Example usage:
file_path = r'"C:\Users\Kaan Apaydin\Downloads\main.pdf"'
open_file(file_path)