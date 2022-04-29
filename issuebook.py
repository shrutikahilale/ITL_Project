from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymongo


# function to issue book
def issue():
    # global variables to use in both functions
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status

        # Connect mongod to python
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    libdb = client['libDatabase']
    books = libdb['books']
    issuedbooks = libdb['booksissued']

    bid = inf1.get()
    issuedto = inf2.get()


    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()

    try:
        # Check if book is available
        if(books.find_one({"b_id": bid})):

            # check if the book is already issued to the issuer
            if(issuedbooks.find_one({"b_id": bid,"issuedto": issuedto})):
                messagebox.showinfo('Message',"Book already issued")
                root.destroy()
                return

            # else:
            # insert the record to issued books table with bid and issuer's name
            bk_details = {
                "b_id": bid,
                "issuedto": issuedto
            }
            issuedbooks.insert_one(bk_details)
            messagebox.showinfo('Message',"Book succesfully issued")

            # update the books table with status of the book to 'issued'
            bk_prev = {'b_id':bid}  # book with id 'bid'
            bk_next = {'$set': {'b_status': 'issued'}}  #set book status to 'issued'
            books.update_one(bk_prev, bk_next)

        else:
            messagebox.showinfo("Message", "Can't find book!")
            root.destroy()       
    except:
        messagebox.showinfo("Error","Failed to issue book")
        root.destroy()
        return


    print(bid)
    print(issuedto)    
    # allBid.clear()
    root.destroy()


# function to open window
def issuebook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Library")
    root.minsize(width = 400, height = 400)
    root.geometry("1900x700")   


        # Connect mongod to python
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    libdb = client['libDatabase']
    books = libdb['books']
    issuedbooks = libdb['booksissued']
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    
    #Issue Button
    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
