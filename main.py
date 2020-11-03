from tkinter import *

def build_gui():
    root = Tk()
    root.title("Temperature Converter")
    root.geometry("700x400")

    celcius = IntVar()
    fahrenheit = IntVar()

    labelframe1=LabelFrame(root, text="Degrees Celcius",padx="40", pady="40")
    labelframe1.pack(fill="both")
    labelframe1.place(x = 100, y = 10)
    C_entry=Entry(labelframe1)
    C_entry.configure(state="disable")
    C_entry.pack()

    labelframe2=LabelFrame(root, text="Degrees Fahrenheit", padx="40",pady="40")
    labelframe2.pack(fill="both")
    labelframe2.place(x = 350, y = 10)
    F_entry=Entry(labelframe2)
    F_entry.configure(state="disable")
    F_entry.pack()

    def activate_Cel():
        C_entry.configure(state="normal")


    cel_convert_btn=Button(text="Activate-Celcius to Fahrenheit", command=activate_Cel)
    cel_convert_btn.pack()
    cel_convert_btn.place( x = 120,y = 150)


    def activate_far():
        F_entry.configure(state="normal")


    f_convert_btn=Button(text="Activate-Fahrenheit to Celcius", command=activate_far)
    f_convert_btn.pack(side=RIGHT)
    f_convert_btn.place(x = 380, y = 150)

    def convert():
        if C_entry:
            celcius = float(C_entry.get())
            fahrenheit = (celcius *9/5) + 32
            answer.insert(0, float(fahrenheit))

    def convert1():
        if F_entry:
            fahrenheit = float(F_entry.get())
            celcius = (fahrenheit -32) *5/9
            answer.insert(0, float(celcius))

    cal_btn=Button(text="Celcius-Fahrenheit", command=convert)
    cal_btn.pack(side=LEFT)
    cal_btn.place(x = 50, y = 230)

    cal_btn1=Button(text="Fahrenheit-Celcius", command=convert1)
    cal_btn1.pack(side=LEFT)
    cal_btn1.place(x = 50, y = 290)

    answer=Entry(text="", background="lime")
    answer.pack()
    answer.place(x = 280 ,y = 230)

    def clear_all():
        C_entry.delete(0, END)
        F_entry.delete(0, END)
        answer.delete(0, END)

    clear_btn=Button(text="Clear", command=clear_all)
    clear_btn.pack(side=RIGHT)
    clear_btn.place(x = 500, y = 230)

    def exit_prog():
        root.destroy()

    exit_btn=Button(text="Exit Program", command=exit_prog)
    exit_btn.pack(side=RIGHT)
    exit_btn.place(x = 500, y = 270)

    root.mainloop()


build_gui()
