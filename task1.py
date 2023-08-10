from tkinter import *
from tkinter import ttk

class TODOLIST:
    def __init__(self,root):
        self.root=root
        self.root.title("To-do List")
        self.root.geometry('550x550+150+150')
        self.label=Label(self.root,text='TO-DO-LIST',
                         font="ARIAL, 30 bold",width=10,bd=15,bg='LIGHT BLUE',fg='black')
        self.label.pack(side='top',fill=BOTH)


        self.label2=Label(self.root,text='ADD',
                         font='ARIAL,20',width=10,bd=10,bg='black',fg='LIGHT BLUE')
        self.label2.place(x=40,y=90)


        self.label3=Label(self.root,text='TASKS FOR THE DAY',
                         font='ARIAL,20',width=15,bd=15,bg='black',fg='LIGHT BLUE')
        self.label3.place(x=320,y=90)


        self.main_text=Listbox(self.root,height=15,bd=5,width=26,font="ARIAL,20")
        self.main_text.place(x=240,y=170)


        self.text=Text(self.root,bd=5,height=2,width=13,font="arial, 22 bold")
        self.text.place(x=10,y=170)



        def add():
            content=self.text.get(1.0,END)
            self.main_text.insert(END,content)
            result = open("tasks.txt","a")
            print(result.read())
            #with open('tasks.txt','a') as file:
            result.write(content)
            result.seek(0)
            result.close()
            self.text.delete(1.0,END)

        def delete():
            delete_= self.main_text.curselection()
            look=self.main_text.get(delete_)
            with open('tasks.txt','r+') as f:
                new_f=f.readlines()
                f.seek(0)
                for line in new_f:
                    item=str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)


            result = open("tasks.txt","r")
            print(result.read())
        # with open("tasks.txt","r") as file:
            read=result.readlines()
            for i in read():
                ready=i.split()
                self.main_text.insert(END,ready)
            result.close()


        self.button=Button(self.root,text="Insert",font="ARIAL, 20 bold",
                           width=6,bd=5,bg='black',fg='LIGHT BLUE',command=add)
        self.button.place(x=50,y=280)

        self.button1=Button(self.root,text="Remove",font="ARIAL, 20 bold",
                           width=6,bd=5,bg='black',fg='LIGHT BLUE',command=delete)
        self.button1.place(x=50,y=360)


def main():
    root=Tk()
    ui=TODOLIST(root)
    root.mainloop()

if __name__ == "__main__":
    main()