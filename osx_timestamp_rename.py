import os, sys, subprocess, tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

def get_creation_date(filepath):
    try:
        cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format_tags=creation_time', '-of', 'default=noprint_wrappers=1:nokey=1', filepath]
        creation_time = subprocess.check_output(cmd, text=True).strip()
        if creation_time:
            creation_date = datetime.strptime(creation_time, '%Y-%m-%dT%H:%M:%S.%fZ')
            return creation_date
    except Exception as e:
        print(f"Error: {e}")
    return None

def create_folder_by_day(folder_path, creation_date):
    day_folder_name = creation_date.strftime("%Y%m%d")
    day_folder_path = os.path.join(folder_path, day_folder_name)
    if not os.path.exists(day_folder_path):
        os.makedirs(day_folder_path)
    return day_folder_path

def rename_files_by_creation_date():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return

    format_selected = format_combobox.get()
    if format_selected == "Select timestamp format":
        tk.messagebox.showwarning("Warning", "Please select a timestamp format.")
        return

    format_specifiers = {
        "YYYYMMDD_HHMMSS": "%Y%m%d_%H%M%S",
        "YYYY-MM-DD_HH-MM-SS": "%Y-%m-%d_%H-%M-%S",
        "YYMMDD_HHMMSS": "%y%m%d_%H%M%S",
        "YY-MM-DD_HHMMSS": "%y-%m-%d_%H%M%S",
        "DDMMYYYY_HHMMSS": "%d%m%Y_%H%M%S",
        "DD-MM-YYYY_HH-MM-SS": "%d-%m-%Y_%H-%M-%S",
        "DDMMYY_HHMMSS": "%d%m%y_%H%M%S",
        "DD-MM-YY_HH-MM-SS": "%d-%m-%y_%H-%M-%S"
    }

    if format_selected not in format_specifiers:
        tk.messagebox.showwarning("Warning", "Invalid timestamp format selected.")
        return

    keep_original_name = keep_name_checkbox_var.get()
    create_folder = create_folder_checkbox_var.get()

    for filename in os.listdir(folder_path):
        if filename == '.DS_Store':  # Skip .DS_Store file
            continue

        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            creation_date = get_creation_date(filepath)
            if creation_date:
                timestamp = creation_date.strftime(format_specifiers[format_selected])

                if keep_original_name:
                    base_name, ext = os.path.splitext(filename)
                    new_filename = f"{timestamp}-{base_name}{ext}"
                else:
                    new_filename = f"{timestamp}.MP4"

                new_filepath = os.path.join(folder_path, new_filename)
                os.rename(filepath, new_filepath)

                if create_folder:
                    day_folder_path = create_folder_by_day(folder_path, creation_date)
                    os.replace(new_filepath, os.path.join(day_folder_path, new_filename))

    tk.messagebox.showinfo("Success", "Files renamed successfully!")

def get_image_path():
    if getattr(sys, 'frozen', False):
        # Running as a bundled app
        return os.path.join(sys._MEIPASS, "resources", "image.png")
    else:
        # Running as a standalone script
        return os.path.join("resources", "image.png")  # Relative path to the image file

# Create the APP window
app = tk.Tk()
app.title("Rename Files by Creation Date")
app.geometry("400x300")

# Load the image
image_path = get_image_path()
if os.path.exists(image_path):
    image = tk.PhotoImage(file=image_path)
else:
    image = None

# Create a label for the image
image_label = tk.Label(app, image=image)
image_label.pack(pady=5)

# Add a combobox to select timestamp format
formats = ["Select timestamp format", "YYYYMMDD_HHMMSS", "YYYY-MM-DD_HH-MM-SS", "YYMMDD_HHMMSS", "YY-MM-DD_HH-MM-SS", "DDMMYYYY_HHMMSS", "DD-MM-YYYY_HH-MM-SS", "DDMMYY_HHMMSS", "DD-MM-YY_HH-MM-SS"]
format_combobox = tk.StringVar()
format_combobox.set(formats[0])
format_menu = tk.OptionMenu(app, format_combobox, *formats)
format_menu.pack(pady=10)

# Add a checkbox to keep the original name at the end
keep_name_checkbox_var = tk.IntVar()
keep_name_checkbox = tk.Checkbutton(app, text="Keep Original Name at end", variable=keep_name_checkbox_var)
keep_name_checkbox.pack(pady=5)

# Add a checkbox to create folder by day
create_folder_checkbox_var = tk.IntVar()
create_folder_checkbox = tk.Checkbutton(app, text="Create folder by Day", variable=create_folder_checkbox_var)
create_folder_checkbox.pack(pady=5)

# Add a button to trigger the renaming process
rename_button = tk.Button(app, text="Rename Files", command=rename_files_by_creation_date)
rename_button.pack(pady=10)

# Run the main event loop
app.mainloop()