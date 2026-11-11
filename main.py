from tkinter import *

t=Tk()
t.geometry('400x300')
t.title('main window')

def topwin():
    top = Toplevel()
    top.geometry('400x300')
    top.title('Top Window')
    
    l2=Label(top,text='This is Top Window',font=('Arial',20))
    l2.pack(pady=50)
    
    top.mainloop()
    
l = Label(t,text='This is Main Window',font=('Arial',20))
l.pack(pady=50)
btn=Button(t,text='Open Top Window',font=('Arial',15),command=topwin)
btn.pack(pady=20)

t.mainloop()
