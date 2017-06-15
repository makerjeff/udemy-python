from Tkinter import *

window = Tk()

def from_kg():
    print 'from KG'
    gram = float(e2_value.get())*1000
    pound = float(e2_value.get())*2.20462
    ounce = float(e2_value.get())*35.274
    t1.insert(END, gram)
    t2.insert(END, pound)
    t3.insert(END, ounce)

def Main():
    e1 = Label(window, text='KG')
    e1.grid(row=0, column=0)

    global e2_value
    e2_value = StringVar()
    e2 = Entry(window, textvariable=e2_value)
    e2.grid(row=0, column=0)

    b1 = Button(window, text="Convert", command=from_kg)
    b1.grid(row=0, column=2)

    global t1
    t1 = Text(window, height=1, width=20)
    t1.grid(row=1, column=0)

    global t2
    t2 = Text(window, height=1, width=20)
    t2.grid(row=1, column=1)

    global t3
    t3 = Text(window, height=1, width=20)
    t3.grid(row=1, column=2)
    window.mainloop()

if __name__ == '__main__':
    Main()