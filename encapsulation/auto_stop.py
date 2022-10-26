# Import the required library
from tkinter import *
from tkinter import messagebox
import time
import subprocess

given_time_in_sec = 0
coundown_timer = 0


# 60 seconds countdown logic
def countdown(win, vreme_countdown):
    current = 60
    while current > 0:
        time.sleep(1)
        win.update()
        vreme_countdown.configure(text=f"{current - 1}")
        current -= 1
        coundown_timer = current
    messagebox.showinfo("", "Shutting down!")


def give_more_time(dobaveno_vreme):
    global given_time_in_sec
    given_time_in_sec += 10
    dobaveno_vreme.configure(text=f"{given_time_in_sec}")


def apply(win, top, top_admin):
    close_win(top_admin)
    close_win(top)
    close_win(win)

    time.sleep(given_time_in_sec)
    main()


# Define a function to close the popup window
def close_win(top):
    top.destroy()


def check(e, top, win):
    if e.get() == "parola":
        messagebox.showinfo("Access to admin panel")
        top_admin = Toplevel(top)
        top_admin.geometry("750x250")

        admin_label = Label(top_admin, text="Всяко натискане на бутона дава 30 мин", font='Helvetica 15 bold')
        dobaveno_vreme = Label(top_admin, text=f"{given_time_in_sec}", font='Helvetica 15 bold', fg='red')

        admin_button = Button(top_admin, text="ADMIN ONLY!", command=lambda: give_more_time(dobaveno_vreme))
        close_take_affect_button = Button(top_admin, text="Close and apply", command=lambda: apply(win, top, top_admin))

        admin_label.grid(row=2, column=4, sticky=W, pady=2)
        dobaveno_vreme.grid(row=2, column=6, sticky=W, pady=2)
        admin_button.grid(row=3, column=4, sticky=W, pady=2)
        close_take_affect_button.grid(row=3, column=6, sticky=W, pady=2)


# Define a function to open the Popup Dialogue

def popupwin(win):
    # Create a Toplevel window
    top = Toplevel(win)
    top.geometry("750x250")

    # Create an Entry Widget in the Toplevel window
    entry = Entry(top, width=25)
    entry.pack()

    # Create a Button to print something in the Entry widget
    Button(top, text="Enter Password", command=lambda: check(entry, top, win)).pack(pady=5, side=TOP)
    # Create a Button Widget in the Toplevel Window
    button = Button(top, text="Close", command=lambda: close_win(top))
    button.pack(pady=5, side=TOP)


def main():
    global given_time_in_sec
    given_time_in_sec = 0  #
    # Create an instance of tkinter frame
    win = Tk()
    win.title('Python Auto Stop System')
    # Define geometry of the window
    win.geometry("750x250")

    # Create a Label
    label = Label(win, text="Компютъра се изключва след", font='Helvetica 15 bold')
    label.grid(row=1, column=4, sticky=W, pady=2)

    vreme_countdown = Label(win, text="60", font='Helvetica 15 bold', fg='red')
    vreme_countdown.grid(row=1, column=5, sticky=W, pady=2)

    label2 = Label(win, text="секунди", font='Helvetica 15 bold')
    label2.grid(row=1, column=6, sticky=W, pady=2)

    button = Button(win, text="Още време?", command=lambda: popupwin(win), font='Helvetica 14 bold')
    button.grid(row=2, column=4, sticky=W, pady=2)

    countdown(win, vreme_countdown)

    # Create a Button


time.sleep(given_time_in_sec)  # currently 10
# SCHEDULED_TIME = 0

main()
