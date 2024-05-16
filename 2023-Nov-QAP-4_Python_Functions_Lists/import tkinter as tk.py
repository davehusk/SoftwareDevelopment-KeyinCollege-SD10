import tkinter as tk
import os
from tkinter import filedialog, ttk, scrolledtext

# Global reference to the main window
window = None

def initialize_gui():
    global window
    window = tk.Tk()
    window.title("Main Application")
    window.geometry("800x600")

    create_file_system_viewer()

    window.mainloop()

def create_file_system_viewer():
    global window
    clear_window()

    directory_label = tk.Label(window, text="Selected Directory: ")
    directory_label.pack()

    # Button for selecting directory and processing text files
    select_button = tk.Button(window, text="Select Directory", command=lambda: handle_directory_selection(directory_label))
    select_button.pack()

    # Button for processing Markdown files
    md_button = tk.Button(window, text="Process Markdown Files", command=lambda: process_markdown_files(directory_label.cget("text")[20:]))
    md_button.pack()

    refresh_button = tk.Button(window, text="Refresh", command=create_file_system_viewer)
    refresh_button.pack()

def clear_window():
    global window
    for widget in window.winfo_children():
        widget.destroy()

def handle_directory_selection(label):
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        label.config(text="Selected Directory: " + selected_directory)

def process_files(directory):
    if directory:
        master_file_path = os.path.join(directory, 'master.txt')
        with open(master_file_path, 'w') as master_file:
            for filename in os.listdir(directory):
                if filename.endswith('.txt'):
                    file_path = os.path.join(directory, filename)
                    with open(file_path, 'r') as file:
                        content = file.read().replace('#', '').replace('*', '')
                        master_file.write(content + '---')
        tk.messagebox.showinfo("Success", "Text files processed into master.txt")

def process_markdown_files(directory):
    if directory:
        # Create a side panel for listing markdown files
        side_panel = tk.Toplevel(window)
        side_panel.title("Markdown Files")
        side_panel.geometry("400x600")

        # Create a listbox to list markdown files
        md_listbox = tk.Listbox(side_panel)
        md_listbox.pack(fill=tk.BOTH, expand=True)

        # Populate the listbox with markdown files
        md_files = [f for f in os.listdir(directory) if f.endswith('.md')]
        for md_file in md_files:
            md_listbox.insert(tk.END, md_file)

        # Create a preview area
        preview_area = scrolledtext.ScrolledText(side_panel, wrap=tk.WORD)
        preview_area.pack(fill=tk.BOTH, expand=True)

        # Function to update preview area with selected file's content
        def update_preview(event):
            selected_file = md_listbox.get(md_listbox.curselection())
            with open(os.path.join(directory, selected_file), 'r') as file:
                content = file.read()
                preview_area.delete('1.0', tk.END)
                preview_area.insert(tk.INSERT, content)

        md_listbox.bind('<<ListboxSelect>>', update_preview)

        # Button to create master.md file
        create_master_button = tk.Button(side_panel, text="Create Master.md", command=lambda: create_master_md(directory, md_files))
        create_master_button.pack()

def create_master_md(directory, md_files):
    master_content = ""
    for md_file in md_files:
        with open(os.path.join(directory, md_file), 'r') as file:
            content = file.read()
            # Compare each paragraph with existing content in master.md
            for paragraph in content.split('\n\n'):
                if paragraph not in master_content:
                    master_content += paragraph + '\n\n'

    # Write the unique content to master.md
    with open(os.path.join(directory, 'master.md'), 'w') as master_file:
        master_file.write(master_content)

    tk.messagebox.showinfo("Success", "master.md file created with unique content.")

if __name__ == "__main__":
    initialize_gui()
