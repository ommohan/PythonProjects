
#Using grid() #geometry manager that oraganizes in table-like strucutre in parent widget
from tkinter import *
window = Tk()

titleLabel = Label(window,text="Enter your information",font=("Verdona",25)).grid(row=0,column=0,columnspan=2)



firstNameLabel = Label(window,text="First name:",width=20,bg="red").grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)

lastNameLabel = Label(window,text="Last name:",width=10,bg="Green",).grid(row=2,column=0)
lastNameEntry = Entry(window).grid(row=2, column= 1)

emailNameLabel = Label(window,text="email:",bg="orange",fg="blue").grid(row=3,column=0)
emailNameEntry = Entry(window).grid(row=3, column= 1)

submit_button = Button(window,text="submit").grid(row=4,column=0,columnspan=2)
window.mainloop()