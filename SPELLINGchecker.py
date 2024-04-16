from  tkinter import *
from textblob import TextBlob
root=Tk()
root.title("spelling checker")
root.geometry("700x400")
root.config(bg="light blue")

def check():
    word=enter_text.get()
    a=TextBlob(word)
    right=str(a.correct())

    cs=Label(root,text="correct text is :",font="poppins 20",bg="light blue",fg="blue")
    cs.place(x=100,y=250)
    spell.config(text=right)

heading=Label(root,text="spelling checker",font=("Trebuchet MS",30,"bold"),bg="light blue",fg="blue")
heading.pack(pady=50)

enter_text=Entry(root,justify="center",width=30,font="poppins,25",bg="white",border=2)
enter_text.pack(pady=10)
enter_text.focus()

button=Button(root,text="check",font="arial 20 bold",fg="white",bg="red",command=check)
button.pack()

spell=Label(root,font="poppins  20",bg="light blue",fg="blue")
spell.place(x=350,y=250)
root.mainloop()