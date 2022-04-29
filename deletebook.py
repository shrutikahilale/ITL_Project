from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymongo



# function to delete book from databases
def delet():
    # Connect mongod to python
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    libdb = client['libDatabase']
    books = libdb['books']
    booksissued = libdb['booksissued']

    # get bid from user 
    bid = bookInfo1.get()


    # mongod code to delete a book from table books and issuedbooks from database libDatabase
    try:  
        # if book is present in the library then delete it
        if(books.find_one({"b_id": bid})): 
            books.delete_one({'b_id':bid})
            booksissued.delete_one({'b_id':bid})
            messagebox.showinfo('Success','Succesfully Deleted!')
        else:
            # else flash a prompt: Cant find book
            messagebox.showinfo('Message',"Can't find book!")
            root.destroy()
            return 
    except:
        messagebox.showinfo('Error', 'Please Check BookID')
    
    print(bid)
    bookInfo1.delete(0,END)
    root.destroy()


# function to open window for deleteing a book
def deletebook():
    global bookInfo1,Canvas1,books,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width = 400, height = 400)
    root.geometry("1900x700")

    
    # Connect mongod to python
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    libdb = client['libDatabase']

    # tables
    books = libdb['books']
    booksissued = libdb['booksissued']

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        

    # heading frame and label frame
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete a Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=delet)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
