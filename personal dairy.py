import datetime
import os
import tkinter as tk

def create_directory():
    current_date = datetime.date.today()
    directory_name = current_date.strftime('%Y-%m-%d')
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)

def save_entry():
    current_date_time = datetime.datetime.now()
    file_name = current_date_time.strftime('%Y-%m-%d %H-%M-%S')
    entry = text_entry.get('1.0', 'end-1c')
    directory_name = current_date_time.strftime('%Y-%m-%d')
    file_path = os.path.join(directory_name, file_name + '.txt')
    
    with open(file_path, 'w') as file:
        file.write(entry)
    text_entry.delete('1.0', 'end')  # Clear the entry after saving

# Set up the main application window
root = tk.Tk()
root.title('Diary')

# Create the text entry field
text_entry = tk.Text(root, height=20, width=50)
text_entry.pack()

# Create the save button
save_button = tk.Button(root, text='Save', command=save_entry)
save_button.pack()

# Create the quit button
quit_button = tk.Button(root, text='Quit', command=root.quit)
quit_button.pack()

# Create the directory for today's date
create_directory()

# Start the Tkinter main loop
root.mainloop()
