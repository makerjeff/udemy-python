from Tkinter import *      #python2: this imports all modules as themselves, vs 'tkinter._______'
# import tkinter    #python3

#TKinter programs are made up of a WINDOW and WIDGETS.
window = Tk()   # program code goes vv

def km_to_miles():
    print e1_value.get()    #e1_value itself is not a string; use get() to pull string value.
    miles = float(e1_value.get()) * 1.6
    t1.insert(END, miles)

b1 = Button(window, text='execute', command=km_to_miles)
#b1.pack()       #draws the button, packing everything
b1.grid(row=0, column=0, rowspan=2)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=5, width=20)
t1.grid(row=0, column=2)






window.mainloop()   # program code goes ^^

