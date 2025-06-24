"""
Muhammad Rafie 2025

=====READ=====
This is my first solo project working with tkinter!
This is a simple To-Do App allowing users to:

- Create tasks with titles and descriptions
- Have multiple tasks to toggle complete, delete, and view descriptions
- See total task progression
- View randomly changing motivational messages (to keep you not-blue) :)

I hope you enjoy! There's more to come.
==============
"""
import json
import math
import random
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image


class Todo(tk.Frame):
    def __init__(self, parent, title, desc, root):
        # Initialize Variables
        self.completed = False
        self.parent = parent
        self.title = " ".join(title.split())
        self.desc = " ".join(desc.split())
        self.root = root
        
        # Configure Right Frame Goal Title Display
        display_text = self.title
        if len(display_text) > 14:
            display_text = display_text[0:11] + '...'

        # Initialize Goal Frame and Contents
        super().__init__(parent, bg=root.blue3, height=80, width=750)
        self.propagate(False)
        self.pack(pady=20, padx=30)

        self.tf_label = tk.Button(self, text=display_text, font=(self.root.mfont, self.root.font_bmed),
                                  highlightbackground=root.blue2)
        self.tf_label.pack(side=LEFT, expand=TRUE, fill=BOTH, padx=10, pady=10)

        self.tf_desc = tk.Button(self, text='check notes!', font=(self.root.mfont, self.root.font_bmed),
                                 highlightbackground=root.blue2, command=self.open_goal_tab)
        self.tf_desc.pack(side=LEFT, expand=TRUE, fill=BOTH, padx=10, pady=10)

        self.tf_complete = tk.Button(self, text='complete!', font=(self.root.mfont, self.root.font_bmed),
                                     highlightbackground=root.blue2, command=self.complete_goal)
        self.tf_complete.pack(side=LEFT, expand=TRUE, fill=BOTH, padx=10, pady=10)

        self.tf_delete = tk.Button(self, text='delete!', font=(self.root.mfont, self.root.font_bmed),
                                   highlightbackground=root.blue2, command=self.delete_goal)
        self.tf_delete.pack(side=LEFT, expand=TRUE, fill=BOTH, padx=10, pady=10)

        parent.bind("<Configure>", lambda e: root.right_canvas.configure(scrollregion=root.right_canvas.bbox("all")))

        # Update Goal Count and Update Progress
        root.goal_count += 1

        self.root.progupdate()

    def open_goal_tab(self):
        # Init new window
        self.new_window = tk.Toplevel()
        self.new_window.geometry("1042x945")
        self.new_window.title('My Task!')
        self.new_window.config(bg=self.root.blue1)

        # Init item frames
        # Top Frame: Task Title
        self.f1 = tk.Frame(self.new_window, width=100, height=100, bg=self.root.blue2)
        self.f1.propagate(FALSE)
        self.f1.pack(fill=X, padx=58, expand=True, pady=0)

        self.f1f = tk.Frame(self.f1, bg=self.root.blue3)
        self.f1f.pack(fill=BOTH, padx=50, pady=10, expand=True)

        self.f1l = tk.Label(self.f1f, text=self.title, bg=self.root.blue3, fg='black', font=(self.root.mfont, self.root.font_big))
        self.f1l.pack(fill=BOTH, expand=True, padx=50, pady=10)

        # Middle Frame: Task Description
        self.f2 = tk.Frame(self.new_window, width=100, height=400, bg=self.root.blue2)
        self.f2.propagate(FALSE)
        self.f2.pack(fill=X, padx=58, expand=True)

        self.f2f = tk.Frame(self.f2, bg=self.root.blue3)
        self.f2f.pack(fill=BOTH, expand=TRUE, padx=50, pady=20)

        self.f2l = tk.Label(self.f2f, text=self.desc, bg=self.root.blue3, fg='black', font=(self.root.mfont, self.root.font_bmed), wraplength=250, justify=CENTER)
        self.f2l.pack(fill=BOTH, expand=TRUE, padx=10, pady=10)

        # Bottom Frame: Buttons
        self.f3 = tk.Frame(self.new_window, width=100, height=100, bg=self.root.blue3)
        self.f3.propagate(False)
        self.f3.pack(fill=X, padx=58, expand=True)

        # Return button
        self.rb = tk.Button(self.f3, text='return home!', command=self.new_window.destroy, font=(self.root.mfont, self.root.font_bmed))
        self.rb.pack(side=LEFT, fill=BOTH, expand=TRUE, padx=10, pady=10)

        # Complete toggle button
        self.cb = tk.Button(self.f3, text='', command=self.alt_complete_goal, font=(self.root.mfont, self.root.font_bmed))
        self.cb.pack(side=LEFT, fill=BOTH, expand=TRUE, padx=10, pady=10)

        # Check if Goal is Completed; Change text accordingly
        if not self.completed:
            self.cb.configure(text='complete!')
        else:
            self.cb.configure(text='undo complete!')

        # Delete button
        self.db = tk.Button(self.f3, text='delete!', command=self.alt_delete_goal, font=(self.root.mfont, self.root.font_bmed))
        self.db.pack(side=LEFT, fill=BOTH, expand=TRUE, padx=10, pady=10)

    def complete_goal(self):
        if not self.completed:
            self.completed = True
            self.root.completed += 1
            self.tf_complete.configure(text='undo complete!')
        else:
            self.completed = False
            self.root.completed -= 1
            self.tf_complete.configure(text='complete!')

        self.root.progupdate()

    def alt_complete_goal(self):
        self.complete_goal()
        # Change self.cb text accordingly based on current status
        if self.completed:
            self.cb.configure(text='undo complete!')
        else:
            self.cb.configure(text='complete!')

    def alt_delete_goal(self):
        # Destroy TopLevel Window and Destroy self
        self.new_window.destroy()
        self.delete_goal()

    def delete_goal(self):
        # Update root goal attributes, destroy self, and update progress
        if self.completed:
            self.root.completed -= 1
        self.root.goal_count -= 1

        self.destroy()

        self.root.progupdate()


class GUI:
    def __init__(self):
        # Initialize Variables

        # Fonts
        self.mfont = 'Helvetica'
        self.font_big = 40
        self.font_bmed = 24
        self.font_med = 16
        self.font_sml = 12

        # Color
        self.blue1 = "#84CDEE"
        self.blue2 = '#B9E2F5'
        self.blue3 = '#EDF7FC'

        # Messages
        self.messages = []

        # Other
        self.goal_count = 0
        self.completed = 0
        self.percentage = 0
        self.running = True

        # Creating Main Window
        self.root = tk.Tk()

        self.root.geometry('1920x1080')
        self.root.title('blue-todo')
        self.root.config(bg=self.blue1)

        img = ImageTk.PhotoImage(Image.open("app/src/icon.png"))
        self.root.iconphoto(False, img)

        # Other
        self.root.bind('<Key>', self.keypressdet)

        self.root.bind('<Destroy>', self.runningfalse)

        self.load_messages(self)

        # Initialize Frames
        self.left_frame = tk.Frame(self.root, width=600, height=1015, bg=self.blue2)
        self.left_frame.pack(side='left', fill='both', padx=58, pady=32, expand=True)

        self.right_frame = tk.Frame(self.root, width=800, height=1015, bg=self.blue2)
        self.right_frame.pack(side='right', expand=True, fill=BOTH, padx=58, pady=32)

        # RIGHT FRAME
        self.right_canvas = tk.Canvas(self.right_frame, bg=self.blue2, width=800, height=1015,
                                      scrollregion=(0, 0, 500, 500))

        self.vbar = Scrollbar(self.right_frame, orient=VERTICAL)
        self.vbar.pack(side=RIGHT, fill=Y)
        self.vbar.config(command=self.right_canvas.yview)

        self.right_canvas.config(width=800, height=1015)
        self.right_canvas.config(yscrollcommand=self.vbar.set)
        self.right_canvas.bind('<Configure>',
                               lambda e: self.right_canvas.configure(scrollregion=self.right_canvas.bbox("all")))
        self.right_canvas.pack(expand=True, fill=BOTH)

        self.sframe = Frame(self.right_canvas, bg=self.blue2)
        self.right_canvas.create_window((0, 0), window=self.sframe, anchor='nw')

        # LEFT FRAME
        # Title
        self.left_title = tk.Label(self.left_frame, bg=self.blue3, text='My Tasks!', font=(self.mfont, self.font_big),
                                   fg='black', width=10, height=1)
        self.left_title.pack(pady=(34, 0), padx=52)

        # Progress Bar
        self.progress_frame = tk.Frame(self.left_frame, bg=self.blue2)
        self.progress_frame.pack(padx=52, pady=(60, 0))

        self.progress_label = tk.Label(self.progress_frame, bg=self.blue2, fg='black', font=(self.mfont, self.font_med),
                                       text='My Progress!')
        self.progress_label.pack()

        s = ttk.Style()
        s.theme_use('default')
        s.configure('custom.Horizontal.TProgressbar', troughcolor=self.blue2, background=self.blue1)
        self.progbar = ttk.Progressbar(self.progress_frame, orient=HORIZONTAL, length=300, mode="determinate",
                                       style='custom.Horizontal.TProgressbar')

        self.progbar.pack(ipady=10)

        self.progress_p_label = tk.Label(self.progress_frame, bg=self.blue2, fg='black',
                                         font=(self.mfont, self.font_med),
                                         text="You're 0% of the way there!")

        self.progress_p_label.pack()

        # Task Title Box
        self.task_title_frame = tk.Frame(self.left_frame, bg=self.blue2)
        self.task_title_frame.pack(padx=52, pady=(100, 0))

        self.task_title = tk.Label(self.task_title_frame, text='Enter Task Title', font=(self.mfont, self.font_med),
                                   bg=self.blue2, fg='black')
        self.task_title.pack()

        self.task_text = tk.Text(self.task_title_frame, font=(self.mfont, self.font_med), bg=self.blue3, height=1,
                                 width=30, fg='black')
        self.task_text.pack()

        # Task Title Character Checker
        self.tt_char = tk.Label(self.task_title_frame, bg=self.blue2, fg='red', text='0/35 characters',
                                font=(self.mfont, self.font_sml))
        self.tt_char.pack()

        # Desc Box
        self.desc_frame = tk.Frame(self.left_frame, bg=self.blue2)
        self.desc_frame.pack(padx=52, pady=(20, 0))

        self.desc_title = tk.Label(self.desc_frame, text='Enter Description', font=(self.mfont, self.font_med), bg=self.blue2,
                                   fg='black')
        self.desc_title.pack()

        self.desc_text = tk.Text(self.desc_frame, font=(self.mfont, self.font_med), bg=self.blue3, height=5, width=30,
                                 fg='black')
        self.desc_text.pack()

        # Desc Character Checker
        self.dt_char = tk.Label(self.desc_frame, bg=self.blue2, fg='red', text='0/175 characters',
                                font=(self.mfont, self.font_sml))
        self.dt_char.pack()

        # Create Task Button
        self.create_button = tk.Button(self.left_frame, text='Create Task!', command=self.create_goal,
                                       height=1, width=10, font=(self.mfont, self.font_big), relief='raised',
                                       highlightbackground=self.blue2)
        self.create_button.pack(pady=50)

        # Motivation Messages :)
        self.mmfont = Font(family='Helvetica', size=self.font_bmed, slant="italic", weight="bold")

        self.mm_label = tk.Label(self.left_frame, text='"Done is better than perfect."', font=self.mmfont, bg=self.blue2, fg='black')
        self.mm_label.pack()

        self.root.after(25000, self.replace_message)
        self.root.mainloop()

    def create_goal(self):
        # Check if Character Limit for Title/Desc Passed
        # Title
        title = len(" ".join(self.task_text.get('1.0', tk.END).split()))
        desc = len(" ".join(self.desc_text.get('1.0', tk.END).split()))

        if title > 35:
            err_window = tk.Toplevel(bg=self.blue1)
            err_window.geometry('400x400')
            err_window.title("Error!")

            err_frame = tk.Frame(err_window, bg=self.blue2, height=250, width=250)
            err_frame.propagate(False)
            err_frame.pack(padx=50, pady=50)

            err_text = tk.Label(err_frame, justify="center", wraplength=100, bg=self.blue2, fg='black',
                                font=(self.mfont, self.font_med), text="You've exceeded the 35 character"
                                                                       "limit for Task "
                                                                       "Titles!")
            err_text.pack(pady=70)

            if desc > 175:
                err_text.configure(text="You've exceeded the character limit for Task Titles and "
                                        "Task Notes!")
            return

        # Desc
        if desc > 175:
            err_window = tk.Toplevel(bg=self.blue1)
            err_window.geometry('400x400')
            err_window.title("Error!")

            err_frame = tk.Frame(err_window, bg=self.blue2, height=250, width=250)
            err_frame.propagate(False)
            err_frame.pack(padx=50, pady=50)

            err_text = tk.Label(err_frame, justify="center", wraplength=100, bg=self.blue2, fg='black',
                                font=(self.mfont, self.font_med), text="You've exceeded "
                                                                       "the 175 character "
                                                                       "limit for Task Notes!")
            err_text.pack(pady=70)
            return

        # Empty Title
        if title == 0:
            err_window = tk.Toplevel(bg=self.blue1)
            err_window.geometry('400x400')
            err_window.title("Error!")

            err_frame = tk.Frame(err_window, bg=self.blue2, height=250, width=250)
            err_frame.propagate(False)
            err_frame.pack(padx=50, pady=50)

            err_text = tk.Label(err_frame, justify="center", wraplength=100, bg=self.blue2, fg='black',
                                font=(self.mfont, self.font_med), text="Enter a title for your Task!")
            err_text.pack(pady=70)
            return

        # Store Variables
        title = self.task_text.get('1.0', tk.END)
        desc = self.desc_text.get('1.0', tk.END)

        # Create Goal Frame Instance
        new = Todo(self.sframe, title, desc, self)

        # Remove Content of self.task_text and self.desc_text
        self.task_text.delete('1.0', END)
        self.desc_text.delete('1.0', END)

        # Update Counters
        self.textupdate()

    def progupdate(self):
        # Change Progress Bar Value
        if self.goal_count != 0:
            self.percentage = math.floor((self.completed / self.goal_count) * 100)

        else:
            self.percentage = 0

        self.progbar['value'] = self.percentage

        # Change Progress Percentage Label
        self.progress_p_label.configure(text="You're " + str(self.percentage) + "% of the way there!")

    def keypressdet(self, event):
        # Detect Key Inputs
        if event.keysym:
            self.textupdate()

    def textupdate(self):
        # Remove extra whitespace from text
        tlength = len(" ".join(self.task_text.get('1.0', tk.END).split()))
        dlength = len(" ".join(self.desc_text.get('1.0', tk.END).split()))

        # Update Character Indicators
        self.tt_char.configure(text=str(tlength) + '/35 characters')
        self.dt_char.configure(text=str(dlength) + '/175 characters')

    def runningfalse(self, event):
        # Set Running Attribute to False
        if self.running:
            self.running = False
            print('Application Closed!')

    def replace_message(self):
        # Choose Random Message and configure mm_label
        msg = random.choice(self.messages)
        self.mm_label.configure(text='"' + msg + '"')

        print('Updated Message!')
        # Iterate Every N (25000) Seconds
        self.root.after(25000, self.replace_message)

    @staticmethod
    def load_messages(self):
        # Load messages from src folder
        with open("app/src/messages.json", 'r') as f:
            data = json.load(f)

        for msg in data['messages']:
            self.messages.append(msg)


if __name__ == '__main__':
    window = GUI()
