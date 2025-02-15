
import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize the main window
window = tk.Tk()
window.title("Virus Scanner Tool")
window.geometry("600x400")

# Label
label = tk.Label(window, text="Welcome to the Virus Scanner Tool", font=("Arial", 16))
label.pack(pady=20)

# Textbox to display scan results
text_box = tk.Text(window, height=10, width=60)
text_box.pack(pady=10)

def scan_file(file_path):
    """
    Function to scan the selected file.
    Add your virus scanning logic here.
    """
    text_box.insert(tk.END, f"Scanning file: {file_path}\n")
    print(f"Scanning file: {file_path}")
    # For demonstration purposes, we'll simulate a scan result.
    # Replace the following lines with your actual scanning logic.
    result = "SAFE"  # Placeholder result.
    text_box.insert(tk.END, f"Scan result: {result}\n")

def select_file():
    """
Function to handle file selection.
    Opens a file dialog and passes the chosen file to the scan_file function.
    """
    file_path = filedialog.askopenfilename(title="Select a File")
    if file_path:
        text_box.insert(tk.END, f"Selected file: {file_path}\n")
        scan_file(file_path)

# Button to select a file
select_button = tk.Button(window, text="Select File to Scan", command=select_file)
select_button.pack(pady=10)

# Run the GUI
window.mainloop()
