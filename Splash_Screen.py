from tkinter import *
from PIL import ImageTk


class Splash_screen:

    def __init__(self,window):
        self.window = window
        self.window.title("Galgotias University")
        self.window.geometry("1350x700")

        self.gu_image = ImageTk.PhotoImage(file = "Images/logo.jpg")

        self.gu_image_lable = Label(window,image=self.gu_image)
        self.gu_image_lable.place(anchor=CENTER,relx=0.5, rely=0.5)

        self.window.after(3000,lambda : self.window.destroy())

    def callingLoginPage(self):
        import login_page


window = Tk()
screen = Splash_screen(window)
window.mainloop()
screen.callingLoginPage()
