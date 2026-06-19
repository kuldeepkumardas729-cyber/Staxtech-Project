import tkinter as tr
from tkinter import messagebox
select = None
#create a empty list 
task=[]
# create add function 
def add():
    global task
    title = entry.get()  # get input
	# use strip to avoid empty task
    if title.strip():
        task.append({"title": title.strip(), "completed": False})
        entry.delete(0, tr.END)
        update()
    else:
        messagebox.showwarning("task is empty", " write a valid task")

#create complete function
def comtask():
    global task, select
    if select is not None and 0 <= select < len(task):
        task[select]["completed"] = True
        update()
    else:
        messagebox.showerror("Selected is error ", "Please select a task properly")
        
#create delete function 
def dele() :
    global task, select
    if select is not None and 0 <= select < len(task):
        removed = task.pop(select)
        update()
        messagebox.showinfo("Deleted", f"Removed: {removed['title']}")
    else:
        messagebox.showerror("selected is Error", "Please select a task properly")
	
# update display 
def update() :
				global task
				LB.delete(0,tr.END)
				for idx, t in enumerate(task,1):
					prog = "✓" if t["completed"] else "×"
					LB.insert(tr.END,f"{idx}.[{prog}] {t['title']}")
					
#main program 
root=tr.Tk()
root.title("Nikki's TO-DO list✓")
root.geometry("360x640")
root.resizable(True,True)
root.config(bg="#87CEFA")#sky blue background

#heading 
tr.Label(
          root ,
          text= "what to do today!! ",
          font =("Helvetica",18,"bold"),
          bg="#87CEFA",
          fg="white"
). pack(pady=10)

#select index
def on_select(event=None):
    global select
    try:
        selected = LB.curselection()
        if selected:
            select= selected[0]
    except:
        select = None
        
        
#list display
LB = tr.Listbox(
              root,
              width =50,
              height=15,
              font=("courier",10),
              bg="white",
              fg="#D81B60",            #deep pink font
              highlightthickness=2,
              highlightbackground="white"
)
LB.pack(pady=10)
LB.bind('<<ListboxSelect>>', lambda event: on_select())


#enter data box
entry=tr.Entry(root,width=28,font=("Helvetica",12))
entry.pack(pady=5)

#for error of not getting keyboard
entry.bind("<Button-1>", lambda e: entry.focus_set())

#buttons
fr=tr.Frame(root,bg="#87CEFA")
fr.pack(pady=10)

sty={
         "width":12, 
         "bg":"#FF69B4" ,    #pink background
         "fg":"white",      #white text
         "font":("Arial",10,"bold")
}
tr.Button(fr, text="Add Task", command=add, **sty).pack(pady=5)
tr.Button(fr, text="Delete Task", command=dele, **sty).pack(pady=5)
tr.Button(fr, text="Task Done", command=comtask, **sty).pack(pady=5)

#end

tr.Label(
         root,
         text="A TO-DO LIST BY NY<3",
         font=("Arial",10),
         bg="#87CEFA",
         fg="white"
).pack(pady=10)

#start program 
root.mainloop()
	