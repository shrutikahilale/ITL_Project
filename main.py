from tkinter import *
from addbook import *
from deletebook import *
from viewbooks import *
from issuebook import *
from returnbook import *
from PIL import ImageTk, Image
import pymongo

#------------------------ Connecting database to Python
client = pymongo.MongoClient("mongodb://localhost:27017/")
libdb = client['libDatabase']
books = libdb['books']


#------------------------set up window

root = Tk()
root.title("Library")
root.minsize(width = 400, height = 400)
root.geometry("1900x700")



same = True
n = 0.25 # not less than 0.25 not more than 5

#------------------------Add bg image

bg_img = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = bg_img.size 


# adjust window according to size to bg image dimensions
newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else:
    newImageSizeHeight = int(imageSizeHeight/n)


# resize the window using new dimensions
bg_img = bg_img.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)

# display bg img
img = ImageTk.PhotoImage(bg_img)

#creating an image using createImage method
canvas1 = Canvas(root)
canvas1.create_image(680,340, image = img)
canvas1.config(bg="white", width= newImageSizeWidth, height= newImageSizeHeight)
#placing the widgets in blocks before placing them in the parent widget
canvas1.pack(expand=True, fill = BOTH)

#------------------------ setting up heading frame with label

head_frame = Frame(root, bg="#fb0", bd=5)
head_frame.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

# we created a frame that will hold the heading label
head_label = Label(head_frame, text = "Welcome to the Library", bg = "black", fg="white", font = ('Calibri', 15))
head_label.place(relx=0, rely=0, relwidth=1, relheight=1)


#------------------------ adding buttons to window frame

# BUTTON to ADD book
# button details
btn1 = Button(root, text="Add a Book", bg="black", fg="white", command=addbook)
# positioning of btn 
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

# BUTTON to DELETE book
btn2 = Button(root, text="Delete a Book", bg="black", fg="white", command=deletebook)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

# BUTTON to VIEW book
btn3 = Button(root, text="View Book List", bg="black", fg="white", command=viewbook)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

# BUTTON to ISSUE book
btn4 = Button(root, text="Issue Book to Student", bg="black", fg="white", command=issuebook)
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

# BUTTON to RETURN book
btn5 = Button(root, text="Return Book", bg="black", fg="white", command=returnbook)
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)


root.mainloop()
