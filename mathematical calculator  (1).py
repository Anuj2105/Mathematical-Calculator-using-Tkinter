#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk



window = tk.Tk() #main application window use graphical user interface



e1= tk.Entry(window, width=20, borderwidth=5) #borderwidth use to the border will be  pixels wide.and width is use to charcter wide
e1.grid(row=0, column=0, columnspan=6) # in this case columnspan is use to flexible and responsive layout

def from_button(number):
    current = e1.get()
    e1.delete(0, tk.END)
    e1.insert(0, str(current) + str(number))


def from_delete():
    e1.delete(0, tk.END)


def from_equal():
    
    result = eval(e1.get()) #eval use to mathematical expression enter by the user.string"add,subtract etc"
    e1.delete(0, tk.END)
    e1.insert(0, result)



d_7 = tk.Button(window, text="7",  command=lambda: from_button(7)) #argument pass to function when click button
d_8 = tk.Button(window, text="8",  command=lambda: from_button(8))
d_9 = tk.Button(window, text="9",  command=lambda: from_button(9))
d_4 = tk.Button(window, text="4",  command=lambda: from_button(4))
d_5 = tk.Button(window, text="5",  command=lambda: from_button(5))
d_6 = tk.Button(window, text="6",  command=lambda: from_button(6))
d_1 = tk.Button(window, text="1",  command=lambda: from_button(1))
d_2 = tk.Button(window, text="2",  command=lambda: from_button(2))
d_3 = tk.Button(window, text="3",  command=lambda: from_button(3))
d_0 = tk.Button(window, text="0",  command=lambda: from_button(0))


add = tk.Button(window, text="+",  command=lambda: from_button("+"))#argument pass to function when click button +
subtract = tk.Button(window, text="-",command=lambda: from_button("-"))
multiply = tk.Button(window, text="*",command=lambda: from_button("*"))
divide = tk.Button(window, text="/", command=lambda: from_button("/"))


clear = tk.Button(window, text="Clear",  command=from_delete)
equal = tk.Button(window, text="=",  command=from_equal)

d_7.grid(row=1, column=0)
d_8.grid(row=1, column=1)
d_9.grid(row=1, column=2)
add.grid(row=1, column=3)

d_4.grid(row=2, column=0)
d_5.grid(row=2, column=1)
d_6.grid(row=2, column=2)
subtract.grid(row=2, column=3)

d_1.grid(row=3, column=0)
d_2.grid(row=3, column=1)
d_3.grid(row=3, column=2)
multiply.grid(row=3, column=3)

d_0.grid(row=4, column=0)
clear.grid(row=4, column=1)
equal.grid(row=4, column=2)
divide.grid(row=4, column=3)


window.mainloop()


# In[ ]:




