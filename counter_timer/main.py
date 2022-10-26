from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import configparser
import winsound
import os



root = Tk()
root.geometry('700x600')
root.title('Counter Files')
root.configure(background='white')

my_dir = ''


def click_button():
    my_dir = filedialog.askdirectory()
    browsed_directory_label.config(text=my_dir)
    files = len(os.listdir(my_dir))

    config = configparser.ConfigParser()
    config.read("configfile.ini")
    config['section']['path'] = str(my_dir)
    config['section']['files'] = str(files)

    with open('configfile.ini', 'w') as configfile:
        config.write(configfile)


button_ask_directory = Button(root, width=30, height=3, text='Избери директория', font=('Helvetica', 14),
                              command=click_button)
button_ask_directory.config(fg='blue')
button_ask_directory.pack(
    ipadx=5,
    ipady=0,
    expand=True
)

browsed_directory_label = Label(root, text=my_dir, height=4, width=30, font=('Helvetica', 14))
browsed_directory_label.pack(
    ipadx=100,
    ipady=0,
    expand=True
)
label = Label(root, text="Брой файлове", height=4, width=20, font=('Helvetica', 14))
label.pack(
    ipadx=5,
    ipady=0,
    expand=True
)

label_counter = Label(root, width=10, height=3, text=f'0', font=('Helvetica', 14))
label_counter.pack(
    ipadx=5,
    ipady=0,
    expand=True
)


def scan_for_new_files():
    print(f"10 sec")

    config = configparser.ConfigParser()
    config.read("configfile.ini")

    path = config['section']['path']
    files = config['section']['files']
    scan_period = config['section']['scan_period']

    if path != '':

        updated_files = os.listdir(path)
        label_counter.config(text=len(updated_files))
        print(updated_files)

        root.update()
        if len(updated_files) > int(files):
            config['section']['files'] = str(len(updated_files))
            with open('configfile.ini', 'w') as configfile:
                config.write(configfile)
            os.startfile("VrouwYouhaveamailmessage.wav")


    root.after(scan_period, scan_for_new_files)


root.after(0, func= scan_for_new_files)
root.mainloop()


"""Deleting key_value pairs from ini file on exit"""
# config = configparser.ConfigParser()
# config.read("configfile.ini")
#
# try:
#     config.remove_option('section','files')
#     config.remove_option('section','path')
# except :
#     pass
# with open('configfile.ini', 'w') as configfile:
#     config.write(configfile)