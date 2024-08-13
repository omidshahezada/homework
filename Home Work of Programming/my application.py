from tkinter import *
from tkinter import filedialog
root = Tk()
root.title("Under Ground")
root.iconbitmap("./development_ZqG_icon.ico")
root.geometry("400x430")
lable1 = Label(root, text= "Welcome to Programming\r Home Work Program!", font=("Andalus", 18), fg= "green")
lable1.pack(pady= 5)
root.resizable(width= False, height= False)


def win():
    if e1.get() == "1":
        window = Tk()
        window.title("Programming Home Work")
        # window.iconbitmap("E:\\1.ico")
        window.geometry("790x500")
        window.resizable(width= False, height= False)
        scrollbar = Scrollbar(window)
        scrollbar.pack(side= RIGHT, fill= BOTH)
        l = Label(window,text= "Welcome Mr/Ms {}!".format(e.get()),font=("Andalus", 16), fg= "red")
        l.pack()
        root.destroy()
        def text_1():
            text.delete(1.0,END)
            with open("H-1.txt") as f:
                data = f.read()
            text.insert(INSERT, data)
        def text_2():
            text.delete(1.0,END)
            with open("H-2.txt") as f:
                data = f.read()
            text.insert(INSERT, data)
        def text_3():
            text.delete(1.0,END)
            with open("H-3.txt") as f:
                data = f.read()
            text.insert(INSERT, data)
        def text_4():
            text.delete(1.0,END)
            with open("H-4.txt") as f:
                data = f.read()
            text.insert(INSERT, data)
        def text_5():
            text.delete(1.0,END)
            with open("H-5.txt") as f:
                data = f.read()
            text.insert(INSERT, data)
        btn = Button(window, text= "Built-in Functions",font=("Andalus", 14),width= 14, fg= "blue", command= text_1)
        btn.pack()
        btn.place(x= 6,y=30)
        btn1 = Button(window, text= "Factorial",font=("Andalus", 14), fg= "blue",width= 14, command= text_2)
        btn1.pack()
        btn1.place(x=6,y=90)
        btn2 = Button(window, text= "Fibonachi Seqence",font=("Andalus", 14), fg= "blue",width= 14, command= text_3)
        btn2.pack()
        btn2.place(x= 6,y=150)
        btn3 = Button(window, text= "Recusive",font=("Andalus", 14), fg= "blue",width= 14, command= text_4)
        btn3.pack()
        btn3.place(x= 6,y=210)


        text = Text(window,yscrollcommand=scrollbar.set, width= 76)
        text.pack()
        text.place(x= 160, y= 32)

        def close():
            window.destroy()

        btn4 = Button(window, text= "OOP Exercies", font= ("Andalus", 14),width= 14,fg= "blue", command= text_5)
        btn4.pack()
        btn4.place(x=6,y=270)
        exit1 = Button(window, text= "Exit", font= ("Andalus", 14),width= 14,fg= "blue", command= close)
        exit1.pack()
        exit1.place(x= 6,y=330)
        l1 =Label(window, text="Designed By Omid Shahezada", font= ("Andalus",12))
        l1.pack()
        l1.place(x= 10, y =430)
        l2 =Label(window, text="Instructor: Abdul Waheed Khaliqyar", font= ("Andalus", 12))
        l2.pack()
        l2.place(x= 10, y =460)

        def text_scroll(*args):
            text.yview(*args)
        scrollbar.config(command= text_scroll)

        menubar = Menu(window, tearoff= 0)
        menubar1 = Menu(menubar, tearoff= 0)
        def open_1():
            a = filedialog.askopenfilename(initialdir= "/", title= "Open file", filetypes= (("txt files", "*.txt"), ("all file", "*.*")))
            text.delete(1.0, END)
            file_10 = open(a, "r")
            text.insert(INSERT, file_10.read())
        def help1():
            help2 = Tk()
            help2.geometry("600x500")
            help2.resizable(width= False, height= False)
            help2.title("HELP")
            help2.iconbitmap("C:\\Users\\Omid Shahizada\\OneDrive\\Desktop\\development_ZqG_icon.ico")
            Label(help2, text='''Kabul University
Computer Science Faculty
Depatement Of Software Engineering''', font=("Andalus", 24), justify= CENTER, pady=20, fg= "red").pack()
            Label(help2, text='''Hi, This is a simple python GUI program.
I hope it will be enjoyable for you!
Designed by: Omid Shahezada
Instructor: Abdul Roheed Khaliqyar''', font=("Andalus", 24), justify= CENTER).pack()
            
            # with open("help.txt") as f:
            #     data = f.read()
            # text.insert(INSERT, data)

        menubar1.add_command(label= "Open", command= open_1)
        menubar4 = Menu(menubar1, tearoff= 0)
        menubar.add_cascade(label= "File", menu= menubar1)
        menubar.add_command(label= "Help", command= help1)
        menubar2 = Menu(menubar1, tearoff= 0)
        menubar2.add_command(label= "Built in Function", command= text_1)
        menubar2.add_command(label= "Factorial", command= text_2)
        menubar2.add_command(label= "Fibonachi Seqence", command= text_3)
        menubar2.add_command(label= "Home work 4", command= text_4)
        menubar2.add_command(label= "OOP Exercies", command= text_5)
        menubar3 = Menu(menubar1, tearoff= 0)
        menubar1.add_cascade(label="Open Home works", menu= menubar2)
        menubar1.add_cascade(label="Save", menu= menubar3)
            
        menubar3.add_command(label= "Save")
        def saveas():
            data1 = text.get(1.0, END)
            f = filedialog.asksaveasfilename(initialdir= "/", title= "Save As", filetypes= (("txt", "*.txt"), ("all", "*.*")))
            if f != None:
                f1 = open(f, "w")
                f1.write(data1)
                f1.close()

        menubar3.add_command(label= "Save As", command= saveas)
        menubar1.add_command(label= "Exit", command= window.quit)
        window.config(menu= menubar)


        window.mainloop()
    else:
        lable2.config(text= "Password is wrong!", font= ("Andalus", 18), fg= "red")

Label(root, text= " Full name ", font= "Andalus").pack(pady= 5)
e = Entry(root, font= "Andalus", justify= "center")
e.pack()
Label(root, text= "Password", font= "Andalus").pack(pady= 5)
e1 = Entry(root, font= "Andalus", justify= "center")
e1.pack()

def exit1():
    root.destroy()

Button(root, text= "Log in", font="Andalus", command= win, width= 10).pack(pady= 5)
Button(root, text= "Exit", font= "Andalus", command= exit1, width= 10).pack(pady= 5)

lable2 = Label(root)
lable2.pack(pady= 5)

root.mainloop()