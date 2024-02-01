from tkinter import *
from tkinter import ttk,messagebox
from Classes import *
from Functions import *
from datetime import *
from InterfaceFuncs import *
from PIL import Image, ImageTk


fen = Tk()
fen.title("Gestion De Scolarité")
fen.iconbitmap("img\centrale1.ico")
x = (fen.winfo_screenwidth() - 800) / 2
y = (fen.winfo_screenheight() - 600) / 2
fen.geometry('%dx%d+%d+%d' % (800, 600, x, y))


# from PIL import Image, ImageTk

image = Image.open("img/JJ.png")
image = image.resize((100, 100), Image.ADAPTIVE)  # Reize to the desired size
logo_image = ImageTk.PhotoImage(image)




# Create a Label to hold the background image
bg_image = Image.open("img/jjjj.jpg")  # Replace with your image file path
bg_image = bg_image.resize((1400, 900), Image.ADAPTIVE)  # Resize to window size
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(fen, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1) 
# Logo Label
logo_label = Label(fen, image=logo_image , bg="#FCFCFC")
logo_label.pack(padx=10, pady=10)  # Adjust the padding as needed"""


# Call the main menu function or any initial function you need
MenuPrincipale(fen)

fen.mainloop()

