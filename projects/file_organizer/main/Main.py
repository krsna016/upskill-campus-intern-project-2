import os
import shutil
import tkinter as tk
from tkinter import filedialog

class ConfidentialFileAssistant:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Organizer")

        self.label_dir = tk.Label(master, text="Target Directory:")
        self.label_dir.pack(pady=10)

        self.button_browse = tk.Button(master, text="Choose Directory", command=self.choose_directory)
        self.button_browse.pack(pady=10)

        self.button_organize = tk.Button(master, text="Organize Data", command=self.organize_data)
        self.button_organize.pack(pady=20)

    def choose_directory(self):
        selected_directory = filedialog.askdirectory()
        if selected_directory:
            self.label_dir.config(text=f"Selected: {selected_directory}")
            self.target_directory = selected_directory

    def organize_data(self):
        if hasattr(self, 'target_directory'):
            self.prepare_folders()
            self.arrange_data()
            tk.messagebox.showinfo("Process Complete", "Data organized successfully!")
        else:
            tk.messagebox.showwarning("Warning", "Please select a directory first.")

    def prepare_folders(self):
        folders_list = ['Images', 'Docs', 'Videos', 'Misc']
        for folder_name in folders_list:
            folder_path = os.path.join(self.target_directory, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

    def arrange_data(self):
        for file_name in os.listdir(self.target_directory):
            file_path = os.path.join(self.target_directory, file_name)
            if os.path.isfile(file_path):
                file_category = self.identify_category(file_name)
                destination_folder = os.path.join(self.target_directory, file_category)
                shutil.move(file_path, os.path.join(destination_folder, file_name))

    def identify_category(self, file_name):
        file_extension = file_name.split('.')[-1].lower()
        image_types = ['jpg', 'jpeg', 'png', 'gif']
        doc_types = ['pdf', 'docx', 'txt']
        video_types = ['mp4', 'mov', 'avi']

        if file_extension in image_types:
            return 'Images'
        elif file_extension in doc_types:
            return 'Docs'
        elif file_extension in video_types:
            return 'Videos'
        else:
            return 'Misc'


if __name__ == "__main__":
    root = tk.Tk()
    app = ConfidentialFileAssistant(root)
    root.mainloop()
