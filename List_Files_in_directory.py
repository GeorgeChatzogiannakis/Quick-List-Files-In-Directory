import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def list_files_and_folders_in_directory(directory_path):
    try:
        # Check if the provided path is a directory
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(f"'{directory_path}' is not a valid directory.")
        
        # Get a list of all files and folders in the directory
        contents = os.listdir(directory_path)
        
        if not contents:
            print(f"No files or folders found in '{directory_path}'.")
            messagebox.showinfo("Empty directory",f"No files or folders found in {directory_path}")
        else:
            print(f"Contents in '{directory_path}':")

            for item in contents:
                print(item)
                
            # Generate a unique output file name
            output_file_path = os.path.join(directory_path, 'directory_contents.txt')
            count = 1
            while os.path.exists(output_file_path):
                output_file_path = os.path.join(directory_path, f'directory_contents_{count}.txt')
                count += 1
            
            # Write the output to the unique .txt file in the specified directory
            with open(output_file_path, 'w') as file:
                file.write('\n'.join(contents))
                print(f"\nOutput written to '{output_file_path}'.")
                messagebox.showinfo("Operation successful",f'Output written to {output_file_path}')
    
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error!",f"An error occured: {e}")

def browse_button():
    global selected_directory
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        directory_label.config(text=f"Selected Directory: {selected_directory}")
        run_button.config(state=tk.NORMAL)
    else:
        directory_label.config(text="Selected Directory: ")
        run_button.config(state=tk.DISABLED)

def run_button_clicked():
    if selected_directory:
        list_files_and_folders_in_directory(selected_directory)
        result_label.config(text="File created! Check the specified directory for the output file.")
    else:
        result_label.config(text="Please select a directory first.")

# Create main window
root = tk.Tk()
root.title("Directory Content Lister")
root.geometry("350x160")

# Create and place widgets
directory_prompt = tk.Label(root, text="Please Select a Directory:")
directory_prompt.pack()
browse_button = tk.Button(root, text="Browse", command=browse_button)
browse_button.pack(pady=10)

directory_label = tk.Label(root, text="Selected Directory: ")
directory_label.pack()

run_button = tk.Button(root, text="Run", command=run_button_clicked, state=tk.DISABLED)
run_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()
