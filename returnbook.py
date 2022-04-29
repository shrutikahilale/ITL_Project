from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymongo

# funciton to return book
def returnn():
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status
    # Connect mongod to python
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    libdb = client['libDatabase']
    books = libdb['books']
    issuedbooks = libdb['booksissued']
    
    
    bid = bookInfo1.get()
    # find book in stock
    try:
        # check if book is issued to someone 
        if(issuedbooks.find_one({"b_id": bid})):       
            # delete book from issuedbooks table
            issuedbooks.delete_one({"b_id": bid})


            # BEFORE UPDATING ISSUEDBOOKS TABLE WE HAVE TO CHECK IF THE SAME BOOK IS STILL ISSUED TO SOME OTHER STUDENT ON NOT

            if(issuedbooks.find_one({"b_id": bid})):
                # update book in books table
                bk_prev = {"b_id":bid}  # book with id 'bid'
                bk_next = {"$set": {"b_status": "issued"}}  #set book status to 'issued'
                books.update_one(bk_prev, bk_next)
            else:
                bk_prev = {"b_id":bid}  # book with id 'bid'
                bk_next = {"$set": {"b_status": "avail"}}  #set book status to 'available'
                books.update_one(bk_prev, bk_next)

                
            messagebox.showinfo('Success',"Book Returned Successfully")
        else:
            messagebox.showinfo("Message", "Can't find book!")
            root.destroy()
    except:
        messagebox.showinfo("Error","Failed to Return")
        root.destroy()
        return


    root.destroy()
    return


# function to open window
def returnbook(): 
    
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1

    # Connect mongod to python
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    libdb = client['libDatabase']
    books = libdb['books']
    issuedbooks = libdb['booksissued']
    
    root = Tk()
    root.title("Library")
    root.minsize(width = 400, height = 400)
    root.geometry("1900x700")

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()