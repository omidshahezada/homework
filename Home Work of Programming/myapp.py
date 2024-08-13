from tkinter import *
window = Tk()

window.title("Home Work")
window.geometry("790x500")

scrollbar = Scrollbar(window)
scrollbar.pack(side= RIGHT, fill= BOTH)
l = Label(window, text= "Welcome",font=("Andalus", 16), fg= "red")
l.pack()
def text_1():
    text.delete(1.0,END)
    with open("C:\\Users\\Omid Shahizada\\OneDrive\\Desktop\\homework notepad\\H-1.txt") as f:
        data = f.read()
    text.insert(INSERT, data)
def text_2():
    text.delete(1.0,END)
    with open("C:\\Users\\Omid Shahizada\\OneDrive\\Desktop\\homework notepad\\H-2.txt") as f:
        data = f.read()
    text.insert(INSERT, data)
def text_3():
    text.delete(1.0,END)
    with open("C:\\Users\\Omid Shahizada\\OneDrive\\Desktop\\homework notepad\\H-3.txt") as f:
        data = f.read()
    text.insert(INSERT, data)
def text_4():
    text.delete(1.0,END)
    with open("C:\\Users\\Omid Shahizada\\OneDrive\\Desktop\\homework notepad\\H-5.txt") as f:
        data = f.read()
    text.insert(INSERT, data)
btn = Button(window, text= "Home Work 1",font="Andalus", fg= "blue", command= text_1)
btn.pack()
btn.place(x=10,y=30)
btn1 = Button(window, text= "Home Work 2",font="Andalus", fg= "blue", command= text_2)
btn1.pack()
btn1.place(x=10,y=90)
btn2 = Button(window, text= "Home Work 3",font="Andalus", fg= "blue", command= text_3)
btn2.pack()
btn2.place(x=10,y=150)
btn3 = Button(window, text= "Home Work 4",font="Andalus", fg= "blue", command= text_4)
btn3.pack()
btn3.place(x=10,y=210)


text = Text(window,yscrollcommand=scrollbar.set, width= 76)
text.pack()
text.place(x= 160, y= 32)

def close():
    window.destroy()

exit1 = Button(window, text= "       Exit       ", font= ("Andalus", 16), fg= "blue", command= close)
exit1.pack()
exit1.place(x=10,y=270)
l1 =Label(window, text="Designed By Omid Shahezada", font= ("Andalus",12))
l1.pack()
l1.place(x= 10, y =430)
l2 =Label(window, text="Instructor: Abdul Waheed Khaliqyar", font= ("Andalus", 12))
l2.pack()
l2.place(x= 10, y =460)

def text_scroll(*args):
    text.yview(*args)
scrollbar.config(command= text_scroll)







window.mainloop()