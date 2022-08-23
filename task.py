import tkinter as tk
from tkinter import *
from tkinter import messagebox 

tasks =[]

def task_add():
    new_task= task_field.get()
    if len(new_task) == 0:
        messagebox.showinfo("Error", "Field is Empty.")
    else:
        tasks.append(new_task)
    
    task_update()


def task_discription():
    pass

    
def task_status():
    new_task= task_field.get()
    if len(new_task)!=0:
        task_box.insert('end',"in process")
        task_box.remove(new_task)
    else:
        task_box.insert('end',"input the task")
        
    task_add()


def task_all():
    for task in tasks:
        print(task) 

        
def task_update():
    for task in tasks:
        task_box.insert('end',task)


def task_delete():
    try:
        value = task_box.get(task_box.curselection())
        if value in tasks:
            tasks.remove(value)
    except:
        messagebox.showinfo('Error','No task selected. Cannot deleted.')


def close():
    print(tasks)
    master.destroy()


if __name__=="__main__":

    master = tk.Tk()
    master.title("Task Manager App")
    master.geometry("500x500+750+250")
    
    header = Frame(master,bg='#FAEBD7')
    functions = Frame(master,bg='#FAEBD7')
    task1_box = Frame(master,bg='#FAEBD7')
    
    header.pack(fill='both')
    functions.pack(side = "left", expand = True, fill = "both")
    task1_box.pack(side = "right", expand = True, fill = "both")  

    header_label = Label(header, text="Task Manager App", font = ("Aerial", "20"), bg='#FAEBD7')
    header_label.pack(padx=20,pady=20)
    
    task_label = Label(functions, text="Input Task",font = ("Aerial", "15"), bg='#FAEBD7')
    task_label.place(x=30,y=40)
    
    task_field = Entry(functions,width=25, bg='#FAEBD7')
    task_field.place(x=30,y=80)
    
    button_1 = Button(functions,text="Add Task", width=25, command=task_add)
    button_2 = Button(functions,text="Task Discription", width=25, command=task_discription)
    button_3 = Button(functions,text="Task Status", width=25, command=task_status)
    button_4 = Button(functions,text="All Task", width=25, command=task_all)
    button_5 = Button(functions,text="Delete Task", width=25, command=task_delete)
    button_6 = Button(functions,text="Exit", width=25, command=close)

    button_1.place(x = 30, y = 120)  
    button_2.place(x = 30, y = 160)  
    button_3.place(x = 30, y = 200)  
    button_4.place(x = 30, y = 240) 
    button_5.place(x = 30, y = 280)
    button_6.place(x = 30, y = 320)
    
    task_box = Listbox(task1_box, width = 30, height=20,bg = "#FFFFFF")
    task_box.place(x=10,y=20)


task_update()
master.mainloop()