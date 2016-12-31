__author__ = 'ritaotao'

from Tkinter import *

#create the window
root = Tk()

#modify root window
root.title("Labeler")
root.geometry("200x100")

app = Frame(root)
app.grid()
button1 = Button(app, text = "This is a button")
button1.grid()

button2 = Button(app)
button2.grid()
button2.configure(text="This will show text")

button3 = Button(app)
button3.grid()

button3["text"] = "This will show up as well."


#kick off the event loop
root.mainloop()

