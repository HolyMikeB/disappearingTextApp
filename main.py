from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs.dialogs import Messagebox


# ------------------------- CONSTANTS ------------------------- #
timer = None
game_over_message = Messagebox
full_string = ''

# ------------------------- FUNCTIONS ------------------------- #


def reset_count():
    root.after_cancel(timer)
    count_down(5)


def count_down(count):
    global timer
    global game_over_message
    global full_string

    if count > 0:
        timer = root.after(1000, count_down, count - 1)
        current_text = text_box.get()
        if current_text == full_string:
            pass
        else:
            full_string = current_text
            reset_count()
        print(count)
    else:
        root.after_cancel(timer)
        text_box.config(state='disabled')
        game_over_message.ok(message='You ran out of time! Click "Start" to try again.', title='Game Over!')


def start_game():
    text_box.config(state='enabled', show='')
    text_box.delete(0, "end")
    count_down(5)


# ------------------------- UI SETUP ------------------------- #
root = tb.Window(themename='cyborg')

root.title('Disappearing Text App')
root.geometry('1000x500')

welcome_label = tb.Label(text='Welcome to the Disappearing Text App!', font=('Impact', 25), bootstyle='primary')
welcome_label.pack(pady=40)

explain_label = tb.Label(text='Keep typing or else the words get it! If you stop typing for 5 seconds,\n the words are '
                              'gone and you have to start over. Click "start" to begin!',
                         font=('Impact', 20),
                         bootstyle='warning')
explain_label.pack(pady=20)

text_box = tb.Entry(font=('Helvetica', 20), state='disabled')
text_box.pack(pady=50)

start_button = tb.Button(root, text='Start', command=start_game)
start_button.pack(pady=30)



root.mainloop()

