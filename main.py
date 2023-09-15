from tkinter import *
from tkinter import messagebox


def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")


def deleteTask():
    lb.delete(ANCHOR)

root = Tk()

root.geometry('500x400+500+150')
root.title('TODO App')
root.config(bg='#242424')
root.resizable(width=False, height=False)


my_entry = Entry(
    root,
    font=('times', 24)
)

my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='light blue',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

frame = Frame(root)

frame.pack(pady=10)

lb = Listbox(
    frame,
    width=20,
    height=5,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",

)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'drink water',

]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)


root.mainloop()
