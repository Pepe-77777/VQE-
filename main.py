import AICustom
from tkinter import *
from tkinter import filedialog as fd
from PIL import Image
root = Tk()
root.title("VQE+ - Virtual Photo Enchancer")
root.resizable(False, False)
root.geometry("700x350")

# Use AI2 = Use to make the image 2x better
# Use AI4 = Use to make the image 4x better
# Use AI8 = Use to make the image 8x better
# Use AICustom = Custom configurations

#BLINEAR
#BICUBIC
#BOX
#LANCZOS

MODE = Image.Resampling.BILINEAR
FILE = "TMP.PNG"
X = 2

title = Label(root, text="VQE+", font=('Helvetica Bold', 53))
subTitle = Label(root, text="Best Virtual Quality Enchancer Software.")
title.pack(padx=50, pady=5)
subTitle.pack(padx=50, pady=15)
empty = Label(root, text=" ")
empty.pack(padx=50, pady=10)

def blinearF():
    global MODE
    MODE = Image.Resampling.BILINEAR

def bicubicF():
    global MODE
    MODE = Image.Resampling.BICUBIC

def boxF():
    global MODE
    MODE = Image.Resampling.BOX

def lanczosF():
    global MODE
    MODE = Image.Resampling.LANCZOS

def modeClickF():
    localWindow = Toplevel()
    localWindow.title("Select Mode")
    blinear = Button(localWindow, text="BLINEAR", command=blinearF)
    bicubic = Button(localWindow, text="BICUBIC", command=bicubicF)
    box = Button(localWindow, text="BOX", command=boxF)
    lanczos = Button(localWindow, text="LANCZOS", command=lanczosF)
    
    blinear.pack()
    bicubic.pack()
    box.pack()
    lanczos.pack()

def fileClickF():
    global FILE   
    filename = fd.askopenfilename()
    FILE = filename

def twoF():
    global X
    X = 2

def fourF():
    global X
    X = 4

def eightF():
    global X
    X = 8

def sixteenF():
    global X
    x = 16

def timesClickF():
    localWindow = Toplevel()
    localWindow.title("Select Times")
    twot = Button(localWindow, text="2x", command=twoF)
    fourt = Button(localWindow, text="4x", command=fourF)
    eightt = Button(localWindow, text="8x", command=eightF)
    sixteent = Button(localWindow, text="16x", command=sixteenF)
    
    twot.pack()
    fourt.pack()
    eightt.pack()
    sixteent.pack()

def runClickF():
    AICustom.open(X, FILE, MODE)

modeButton = Button(root, text="Mode", command=modeClickF)
fileButton = Button(root, text="File", command=fileClickF)
timesButton = Button(root, text="Times", command=timesClickF)
runButton = Button(root, text="Run", command=runClickF)

modeButton.pack()
fileButton.pack()
timesButton.pack()
runButton.pack()

root.mainloop()