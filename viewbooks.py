from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymongo


# funtion to view book and open a window for the same
def viewbook():
    root = Tk()
    root.title("Library")
    root.minsize(width = 400, height = 400)
    root.geometry("1900x700")


    # Connect mongod to python
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    libdb = client['libDatabase']
    books = libdb['books']

    canvas1 = Canvas(root)
    canvas1.config(bg="blue")
    canvas1.pack(expand=True, fill = BOTH)


    # heading and label frame

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font = ('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    

    Label(labelFrame, text="%-20s%-70s%-70s%-50s"%('BookID','Title', 'Author', 'Status'), bg='black', fg='white').place(relx=0.07, rely=0.1)

    Label(labelFrame, text = '------------------------------------------------------------------------------------------------------------------------------------------------------', bg='black', fg='white').place(relx=0.05, rely=0.2)


    # excluding _id to be shown
    allBooks = books.find()

    try:
        for bk in allBooks:
            Label(labelFrame, text="%-20s%-70s%-70s%-50s"%(bk.get('b_id'), bk.get('b_title'), bk.get('b_author'), bk.get('b_status')), bg='black', fg='white').place(relx = 0.07, rely=y)
            y+=0.1
    except:
        messagebox.showinfo("Error","Failed to fetch files from database")



    # quit from that window
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    root.mainloop()

