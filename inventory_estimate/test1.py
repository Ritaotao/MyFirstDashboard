__author__ = 'ritaotao'

#demonstrates how to use a class with Tkinter

from Tkinter import *

class Application(Frame):
    """ A GUI application with three buttons. """

    def __init__(self, master):
        """ Initialize the Frame """
        Frame.__init__(self,master)
        self.grid()
        self.button_clicks = 0 #count the number of button clicks
        self.create_widgets()

    def create_widgets(self):
        """Create button which displays number of clicks"""
        self.button = Button(self)
        self.button["text"] = "Total Clicks: 0"
        self.button["command"] = self.update_count
        self.button.grid()
        # """Create 3 buttons that do nothing."""
        # #create first button
        # self.button1 = Button(self,text="This is the first button.")
        # self.button1.grid()
        #
        # #create second button
        # self.button2 = Button(self)
        # self.button2.grid()
        # self.button2.configure(text="This will show up text")
        #
        # #create third button
        # self.button3 = Button(self)
        # self.button3.grid()
        # self.button3["text"] = "This will also show text"

    def update_count(self):
        """Increase the click count and display the new total"""
        self.button_clicks += 1
        self.button["text"] = "Total Clicks: "+str(self.button_clicks)

root = Tk()
root.title("Lazy Buttons")
root.geometry("200x85")

app=Application(root)
root.mainloop()