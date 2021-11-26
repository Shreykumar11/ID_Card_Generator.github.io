from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import random
import os
import datetime
import pyqrcode
import png
import PIL
import libjpeg

from PIL import Image, ImageDraw, ImageFont, ImageTk
from pyqrcode import QRCode


def ans():
    image = Image.new('RGB', (1200, 900), (153, 153, 255))
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('arial.ttf', size=45)

    os.system("Title: ID CARD Generator by Grasp Coding")

    d_date = datetime.datetime.now()
    reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t ID CARD Generator\t\t\t\t  %I:%M:%S %p")
    
    print(reg_format_date)
    

# starting position of the message
    (x, y) = (50, 50)
    company = s1.get()
    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('arial.ttf', size=80)
    draw.text((x, y), s1.get(), fill=color, font=font)
    s1.set(company)

# adding an unique id number. You can manually take it from user
    (x, y) = (750, 180)
    idno = random.randint(10000000, 90000000)
    message = str('ID: ' + str(idno))
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial.ttf', size=60)
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (50, 250)
    
    name = s2.get()
    message = str('Name: ' + str(name))
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial.ttf', size=45)
    draw.text((x, y), message, fill=color, font=font)
    s2.set(name)

    (x, y) = (50, 350)
    k1 = s8.get()
    message = str('Gender: ' + str(k1))
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)
    s8.set(k1)

    (x, y) = (400, 350)
    k2 = s5.get()
    message = str('Age: ' + str(k2))
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)
    s5.set(k2)

    (x, y) = (50, 450)
    k3 = s4.get()
    message = str('Date of Birth: ' + str(k3))
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)
    s4.set(k3)

    (x, y) = (50, 550)
    k4 = s3.get()
    message = str('Blood Group: ' + str(k4))
    color = 'rgb(255, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)
    s3.set(k4)

    (x, y) = (50, 650)
    temp = s6.get()
    message = str('Mobile Number: ' + str(temp))
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)
    s6.set(temp)

    (x, y) = (50, 750)
    k5 = s7.get()
    message = str('Address: ' + str(k5))
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message, fill=color, font=font)
    s7.set(k5)

# save the edited image

    image.save((str(idno)+name) + '.png')

    img = pyqrcode.create(str(company) + str(idno))  # this info. is added in QR code, also add other things
    img.svg(str(idno)+'.svg', scale = 8)
    img.png(str(idno)+'.png', scale = 6)

    kkk = upload_file()
    st = Image.open(kkk)
    st = st.resize((250,250))
    til = Image.open(str(idno) + '.png')
    image.paste(st, (800, 280))
    image.paste(til, (800, 600)) # 25x25
    image.save((str(idno)+name) + '.png')

    do="Your ID Card Successfully created in a PNG file " + name + '.png'
    messagebox.showinfo("Message",do)

def upload_file():
    f_types = [('Jpg Files', '*.jpg'), ('PNG Files','*.png')]   # type of files to select 
    filename = filedialog.askopenfilename(multiple=True,filetypes=f_types)
    
    for f in filename:
        img=Image.open(f) # read the image file
        #img.svg(name+'.svg', scale = 8)
        img=img.resize((100,100)) # new width & height
        img=ImageTk.PhotoImage(img)
        e0 =Label(root)
        e0.place(x=570, y=180)
        e0.image = img
        e0['image']=img # garbage collection
        return f

def clear():
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    s5.set(0)
    s6.set(0)
    s7.set("")
    s8.set("")

root=Tk()
root.title("Window")
root.geometry("800x650")
root.configure( bg="pink")

s1=StringVar()
s1.set("")
s2=StringVar()
s2.set("")
s3=StringVar()
s3.set("")
s4=StringVar()
s4.set("")
s5=IntVar()
s6=IntVar()
s7=StringVar()
s7.set("")
s8=StringVar()
s8.set("")


l0=Label(root,text="Enter your details",fg="white",bg="green",font="Cambria 24 bold")
l0.place(x=270,y=50)

l1=Label(root,text="Company",fg="black",bg="pink",font="Cambria 16 bold")
l1.place(x=100,y=120)
e1=Entry(root,textvariable=s1,width=30)
e1.place(x=250,y=130)

l2=Label(root,text="Full Name",fg="black",bg="pink",font="Cambria 16 bold")
l2.place(x=100,y=170)
e2=Entry(root,textvariable=s2,width=30)
e2.place(x=250,y=180)

l3=Label(root,text="Age",fg="black",bg="pink",font="Cambria 16 bold")
l3.place(x=100,y=220)
e3=Entry(root,textvariable=s5,width=30)
e3.place(x=250,y=230)

l4=Label(root,text="Blood Group",fg="black",bg="pink",font="Cambria 16 bold")
l4.place(x=100,y=270)
e4=Entry(root,textvariable=s3,width=30)
e4.place(x=250,y=280)

l5=Label(root,text="D.O.B",fg="black",bg="pink",font="Cambria 16 bold")
l5.place(x=100,y=320)
e5=Entry(root,textvariable=s4,width=30)
e5.place(x=250,y=330)

l6=Label(root,text="Address",fg="black",bg="pink",font="Cambria 16 bold")
l6.place(x=100,y=370)
e6=Entry(root,textvariable=s7,width=30)
e6.place(x=250,y=380)

l7=Label(root,text="Mobile No.",fg="black",bg="pink",font="Cambria 16 bold")
l7.place(x=100,y=420)
e7=Entry(root,textvariable=s6,width=30)
e7.place(x=250,y=430)

l8=Label(root,text="Gender",fg="black",bg="pink",font="Cambria 16 bold")
l8.place(x=100,y=470)
e8=Entry(root,textvariable=s8,width=30)
e8.place(x=250,y=480)

b = Button(root, text='Upload Files', width=20,command = lambda:upload_file())
b.place(x=550,y=120)

b1=Button(root,text="Execute",fg="white",bg="green",width=10,height=3,command=ans)
b1.place(x=200,y=550)


b2=Button(root,text="Clear",fg="white",bg="blue",width=10,height=3,command=clear)
b2.place(x=350,y=550)


b3=Button(root,text="Exit",fg="white",bg="red",width=10,height=3,command=root.destroy)
b3.place(x=500,y=550)

mainloop()
