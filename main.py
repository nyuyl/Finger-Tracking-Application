from tkinter import *
from PIL import Image, ImageTk
from hand2 import main


root = Tk()
root.wm_title("Figer Tracking")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("1366x768")
root.configure(background='white')
root.resizable(width=False, height=False)


titlephoto = Image.open("images/logo.png")
titlephoto = titlephoto.convert("RGB")
titlephoto.mode = "RGB"
titleimg = ImageTk.PhotoImage(titlephoto)
titlelabel = Label(root, image = titleimg, borderwidth = 0, highlightthickness = 0)
titlelabel.image = titleimg
titlelabel.place(x = 298, y = 20)

titlephoto1 = Image.open("images/logo.png")
titlephoto1 = titlephoto.convert("RGB")
titlephoto1.mode = "RGB"
titleimg1 = ImageTk.PhotoImage(titlephoto)
titlelabel1 = Label(root, image = titleimg, borderwidth = 0, highlightthickness = 0)
titlelabel1.image = titleimg
titlelabel1.place(x = 498, y = 20)

titlephoto1 = Image.open("images/logo.png")
titlephoto1 = titlephoto.convert("RGB")
titlephoto1.mode = "RGB"
titleimg1 = ImageTk.PhotoImage(titlephoto)
titlelabel1 = Label(root, image = titleimg, borderwidth = 0, highlightthickness = 0)
titlelabel1.image = titleimg
titlelabel1.place(x = 698, y = 20)

titlephoto1 = Image.open("images/logo.png")
titlephoto1 = titlephoto.convert("RGB")
titlephoto1.mode = "RGB"
titleimg1 = ImageTk.PhotoImage(titlephoto)
titlelabel1 = Label(root, image = titleimg, borderwidth = 0, highlightthickness = 0)
titlelabel1.image = titleimg
titlelabel1.place(x = 898, y = 20)


button2photo = Image.open("images/button.png")
button2photo = button2photo.convert("RGB")
button2photo.mode = "RGB"
button2img = ImageTk.PhotoImage(button2photo)
button2 = Button(root, image = button2img, highlightbackground ='#000000', highlightcolor = "#000000", foreground = "#000000", background = "#000000", borderwidth = 4, highlightthickness = 4, command = lambda: main())
button2.place(x = 300, y = 280)

creditphoto = Image.open("images/f8.png")
creditphoto = creditphoto.convert("RGB")
creditphoto.mode = "RGB"
creditimg = ImageTk.PhotoImage(creditphoto)
creditlabel = Label(root, image = creditimg, borderwidth = 0, highlightthickness = 0)
creditlabel.image = creditimg
creditlabel.place(x = 600, y = 520)



