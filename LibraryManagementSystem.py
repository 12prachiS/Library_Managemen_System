from tkinter import*
from tkinter import ttk
import mysql.connector 
from tkinter import messagebox
import tkinter
import datetime

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1363x763+0+0")

        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.Firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()


        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="lavender", fg="black", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=5)
        lbltitle.pack(side=TOP, fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=7,bg="lavender")
        frame.place(x=0,y=110,width=1280,height=350)

        DataFrameLeft=LabelFrame(frame,text="Library Membership Information", bg="lavender", fg="black", bd=10, relief=RIDGE, font=("times new roman", 20, "bold"))
        DataFrameLeft.place(x=0,y=5,width=760,height=320)

        lblMember=Label(DataFrameLeft,bg="lavender",text="Member Type",font=("times new roman", 12, "bold"),padx=2,pady=4)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman", 12, "bold"),textvariable=self.member_var,width=24,state="readonly")
        comMember["value"]=("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(DataFrameLeft,bg="lavender",text="PRN NO",font=("arial", 11, "bold"),padx=2,pady=4)
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_No=Entry(DataFrameLeft,font=("arial", 11, "bold"),textvariable=self.prn_var,width=26 )
        txtPRN_No.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,bg="lavender",text="ID No",font=("arial", 11, "bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial", 11, "bold"),textvariable=self.id_var,width=26 )
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="lavender",text="First Name",font=("arial", 12, "bold"),padx=2,pady=4)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial", 11, "bold"),textvariable=self.Firstname_var,width=26 )
        txtFirstName.grid(row=3,column=1)

        
        lblLastName=Label(DataFrameLeft,bg="lavender",text="Last Name",font=("arial", 11, "bold"),padx=2,pady=4)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial", 11, "bold"),textvariable=self.lastname_var,width=26 )
        txtLastName.grid(row=4,column=1)

        
        lblAddress1=Label(DataFrameLeft,bg="lavender",text="Address1",font=("arial", 11, "bold"),padx=2,pady=4)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial", 11, "bold"),textvariable=self.address1_var,width=26 )
        txtAddress1.grid(row=5,column=1)

        
        lblAddress2=Label(DataFrameLeft,bg="lavender",text="Address2",font=("arial", 11, "bold"),padx=2,pady=4)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial", 11, "bold"),textvariable=self.address2_var,width=26 )
        txtAddress2.grid(row=6,column=1)

        
        lblPostCode=Label(DataFrameLeft,bg="lavender",text="Post Code",font=("arial", 11, "bold"),padx=2,pady=4)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial", 11, "bold"),textvariable=self.postcode_var,width=26 )
        txtPostCode.grid(row=7,column=1)

        
        lblMobile=Label(DataFrameLeft,bg="lavender",text="Mobile No.",font=("arial", 11, "bold"),padx=2,pady=4)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial", 11, "bold"),textvariable=self.mobile_var,width=27 )
        txtMobile.grid(row=8,column=1)  

        
        lblBookID=Label(DataFrameLeft,bg="lavender",text="Book Id",font=("arial", 11, "bold"),padx=4,pady=4)
        lblBookID.grid(row=0,column=5,sticky=W)
        txtBookID=Entry(DataFrameLeft,font=("arial", 11, "bold"),textvariable=self.bookid_var,width=27 )
        txtBookID.grid(row=0,column=6)

        
        lblBookTitle=Label(DataFrameLeft,bg="lavender",text="Book Title",font=("arial", 11, "bold"),padx=4,pady=4)
        lblBookTitle.grid(row=1,column=5,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial", 11, "bold"),textvariable=self.booktitle_var,width=27 )
        txtBookTitle.grid(row=1,column=6)

        
        lblAuthor=Label(DataFrameLeft,bg="lavender",text="Author",font=("arial", 11, "bold"),padx=4,pady=4)
        lblAuthor.grid(row=2,column=5,sticky=W)
        txtAuthor=Entry(DataFrameLeft,font=("arial", 11, "bold"),textvariable=self.author_var,width=27 )
        txtAuthor.grid(row=2,column=6)

        
        lblDateBorrowed=Label(DataFrameLeft,bg="lavender",text="Issued Date",font=("arial", 11, "bold"),padx=4,pady=4)
        lblDateBorrowed.grid(row=3,column=5,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial", 11, "bold"),textvariable=self.dateborrowed_var,width=27 )
        txtDateBorrowed.grid(row=3,column=6)

        
        lblDateDue=Label(DataFrameLeft,bg="lavender",text="Due Date",font=("arial", 11, "bold"),padx=4,pady=4)
        lblDateDue.grid(row=4,column=5,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial", 11, "bold"),textvariable=self.datedue_var,width=27 )
        txtDateDue.grid(row=4,column=6)

        
        lblDaysOnBook=Label(DataFrameLeft,bg="lavender",text="Days on Book",font=("arial", 11, "bold"),padx=4,pady=4)
        lblDaysOnBook.grid(row=5,column=5,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial", 11, "bold"),textvariable=self.daysonbook_var,width=27 )
        txtDaysOnBook.grid(row=5,column=6)

        
        lblLateReturnFine=Label(DataFrameLeft,bg="lavender",text="Late Return Fine",font=("arial", 11, "bold"),padx=4,pady=4)
        lblLateReturnFine.grid(row=6,column=5,sticky=W)
        txtLatereturnFine=Entry(DataFrameLeft,font=("arial", 11, "bold"),textvariable=self.lateratefine_var,width=27 )
        txtLatereturnFine.grid(row=6,column=6)

        
        lblDateOverDate=Label(DataFrameLeft,bg="lavender",text="Date Over Due",font=("arial", 11, "bold"),padx=4,pady=4)
        lblDateOverDate.grid(row=7,column=5,sticky=W)
        txtDateOverDate=Entry(DataFrameLeft,font=("arial", 11, "bold"),textvariable=self.dateoverdue_var,width=27 )
        txtDateOverDate.grid(row=7,column=6)

        
        lblActualPrice=Label(DataFrameLeft,bg="lavender",text="Actual Price",font=("arial", 11, "bold"),padx=4,pady=4)
        lblActualPrice.grid(row=8,column=5,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial", 11, "bold"),textvariable=self.finalprice_var,width=27 )
        txtActualPrice.grid(row=8,column=6)


        DataFrameRight=LabelFrame(frame,text="Book Details", bg="lavender", fg="black", bd=10, relief=RIDGE, font=("times new roman", 20, "bold"))
        DataFrameRight.place(x=780,y=5,width=440,height=320)

        self.txtBox=Text(DataFrameRight,font=("arial", 11, "bold"),width=24, height=14, padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Head First Python','Learn Python: The Hard Way','Deep Learning With Python','Advance Python','Introduction to Algorithms','Design Patterns','Machine learning in Action',
                   'Effective C++','Clean Code','code Simplicity','Softwaare Craftmanship','Think Like A Programmer','Programming Pearls',
                   'Refactoring Databases','Oops','networking with linux','Inside the machine','code complete','Data structures','DevOps','Agile testing','Thinking in C++','SQL CookBook']
        
        def SelectBook(event=""):
            value=str(listbox.get(listbox.curselection()))
            x=value
            if (x=="Head First Python"):
                self.bookid_var.set("BkID4355")
                self.booktitle_var.set("python Manual")
                self.author_var.set("paul berry")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.770")

            elif (x=="Learn Python: The Hard Way"):
                self.bookid_var.set("BkID5655")
                self.booktitle_var.set("basics of python")
                self.author_var.set("john lauren")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.800")

            elif (x=="'Deep Learning With Python"):
                self.bookid_var.set("BkID5005")
                self.booktitle_var.set("joy of learning with python")
                self.author_var.set("meck lauren")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.700")


            elif (x=="Advance Python"):
                self.bookid_var.set("BkID1235")
                self.booktitle_var.set("Python Unleashed")
                self.author_var.set("John Smith")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.600")

            elif (x=="Introduction to Algorithms"):
                self.bookid_var.set("BkID5615")
                self.booktitle_var.set("Mastering Algorithms")
                self.author_var.set("Sarah Johnson")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.899")

            
            elif (x=="Design Patterns"):
                self.bookid_var.set("BkID2235")
                self.booktitle_var.set("Designing Software Patterns")
                self.author_var.set("Michael Brown")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.820")

            elif (x=="SQL CookBook"):
                self.bookid_var.set("BkI0985")
                self.booktitle_var.set("SQL Cookbook Delights")
                self.author_var.set("Elizabeth Allen")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.850")

                
            elif (x=="Thinking in C++"):
                self.bookid_var.set("BkID9087")
                self.booktitle_var.set("Thinking in C++ Concepts")
                self.author_var.set("Benjamin Scott")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.600")


            elif (x=="Agile Testing"):
                self.bookid_var.set("BkID5665")
                self.booktitle_var.set("Agile Testing Strategies")
                self.author_var.set("Sophia Brown")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.620")

                
            elif (x=="Effective C++"):
                self.bookid_var.set("BkID5115")
                self.booktitle_var.set("Effective C++ Techniques")
                self.author_var.set("David Wilson")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.670")

                

            elif (x=="DevOps"):
                self.bookid_var.set("BkID9500")
                self.booktitle_var.set("DevOps Revolution")
                self.author_var.set("Matthew Hall")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.950")

            elif (x=="Data Structures"):
                self.bookid_var.set("BkID5405")
                self.booktitle_var.set("Mastering Data Structures")
                self.author_var.set("Olivia White")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.540")
              
            elif (x=="Clean Code"):
                self.bookid_var.set("BkID5620")
                self.booktitle_var.set("The Art of Clean Code")
                self.author_var.set("Jennifer Lee")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.620")


            elif (x=="Code Complete"):
                self.bookid_var.set("BkID7205")
                self.booktitle_var.set("Code Complete Essentials")
                self.author_var.set(" Daniel Johnson")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.720")

            elif (x=="Inside the Machine"):
                self.bookid_var.set("BkID6400")
                self.booktitle_var.set("Inside the Machine Code")
                self.author_var.set("Lisa Miller")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.640")

            elif (x=="Networking with Linux"):
                self.bookid_var.set("BkID5930")
                self.booktitle_var.set("Networking with Linux Pros")
                self.author_var.set("Brian Adams")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.930")

            elif (x=="Oops"):
                self.bookid_var.set("BkID9305")
                self.booktitle_var.set("Oops! Coding Mistakes")
                self.author_var.set("Jessica Turner")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.930")

            elif (x=="Refactoring Databases"):
                self.bookid_var.set("BkID5800")
                self.booktitle_var.set("Database Refactoring Guide")
                self.author_var.set("Kevin Harris")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.800")

            elif (x=="Programming Pearls"):
                self.bookid_var.set("BkID5599")
                self.booktitle_var.set("Programming Pearls of Wisdom")
                self.author_var.set("Laura Anderson")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.599")

                
            elif (x=="Think Like A Programmer"):
                self.bookid_var.set("BkID5679")
                self.booktitle_var.set("Thinking Like a Pro Coder")
                self.author_var.set("William Taylor")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.679")

                
            elif (x=="Software Craftsmanship"):
                self.bookid_var.set("BkID8499")
                self.booktitle_var.set("Craftsmanship in Software")
                self.author_var.set("Robert Clark")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.849")

            elif (x=="Machine Learning in Action"):
                self.bookid_var.set("BkID1100")
                self.booktitle_var.set("Machine Learning Mastery")
                self.author_var.set("Emily Davis")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.590")



            elif (x=="Code Simplicity"):
                self.bookid_var.set("BkID4995")
                self.booktitle_var.set(" Code Simplicity Secrets")
                self.author_var.set("john lauren")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.499")
                
        listbox = Listbox(DataFrameRight, font=("arial", 12, "bold"), width=20, height=13)
        listbox.bind("<<ListboxSelect>>",SelectBook)
        listbox.grid(row=0, column=0, padx=3)
        listScrollbar.config(command=listbox.yview)

        
        for item in listBooks:
            listbox.insert(END,item)


         #................Button frame................#

        framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=11,bg="lavender")
        framebutton.place(x=0,y=460,width=1280,height=60)

        btnAddData=Button(framebutton,command=self.adda_data, text="Add Data",font=("arial",12,"bold"),width=19,bg="purple",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=19,bg="purple",fg="white")
        btnAddData.grid(row=0,column=1)

        
        btnAddData=Button(framebutton, command=self.update, text="Update", font=("arial", 12, "bold"), width=19, bg="purple", fg="white")
        btnAddData.grid(row=0, column=2)

        
        btnAddData=Button(framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=19,bg="purple",fg="white")
        btnAddData.grid(row=0,column=3)

        
        btnAddData=Button(framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=19,bg="purple",fg="white")
        btnAddData.grid(row=0,column=4)

        
        btnAddData=Button(framebutton,command=self.iExit,text=" Exit",font=("arial",12,"bold"),width=19,bg="purple",fg="white")
        btnAddData.grid(row=0,column=5)


        frameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=2,bg="lavender")
        frameDetails.place(x=0,y=510,width=1280,height=143)

        Table_frame=Frame(frameDetails,bd=6,relief=RIDGE,bg="lavender")
        Table_frame.place(x=0,y=2,width=1260,height=119)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)


        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname",
                                                            "address1","address2","postid","mobile","bookid",
                                                            "booktitle","author","dateborrowed","datedue","days",
                                                            "latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
         
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview) 


        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text=" Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile No.")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text=" Author")
        self.library_table.heading("dateborrowed",text="Issued Date")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days as of Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over due")
        self.library_table.heading("finalprice",text="Final Price")
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=96)
        self.library_table.column("prnno",width=96)
        self.library_table.column("title",width=96)
        self.library_table.column("firstname",width=96)
        self.library_table.column("lastname",width=96)
        self.library_table.column("address1",width=96)
        self.library_table.column("address2",width=96)
        self.library_table.column("postid",width=96)
        self.library_table.column("mobile",width=96)
        self.library_table.column("bookid",width=96)
        self.library_table.column("booktitle",width=96)
        self.library_table.column("author",width=96)
        self.library_table.column("dateborrowed",width=96)
        self.library_table.column("datedue",width=96)
        self.library_table.column("days",width=96)
        self.library_table.column("latereturnfine",width=96)
        self.library_table.column("dateoverdue",width=96)
        self.library_table.column("finalprice",width=96)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Prachi@12",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("Insert into library values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.Firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.lateratefine_var.get(),
            self.dateoverdue_var.get(),  
            self.finalprice_var.get()  
        ))
        conn.commit()
        self.fatch_data()
        conn.close()


        messagebox.showinfo("Success", "Member has been inserted successfully")

    def update(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Prachi@12", database="project")
        my_cursor = conn.cursor()
        query = (
        "UPDATE library SET Member=%s, ID=%s, `First Name`=%s, `Last Name`=%s, Address1=%s, Address2=%s, PostID=%s, "
        "Mobile=%s, BookId=%s, BookTitle=%s, author=%s, DateBorrowed=%s, DateDue=%s, DayonBook=%s, LateReturnFine=%s, "
        "finalprice=%s WHERE PRN_NO=%s"
         )
        my_cursor.execute(query, (
        self.member_var.get(),
        self.id_var.get(),
        self.Firstname_var.get(),
        self.lastname_var.get(),
        self.address1_var.get(),
        self.address2_var.get(),
        self.postcode_var.get(),
        self.mobile_var.get(),
        self.bookid_var.get(),
        self.booktitle_var.get(),
        self.author_var.get(),
        self.dateborrowed_var.get(),
        self.datedue_var.get(),
        self.daysonbook_var.get(),
        self.lateratefine_var.get(),
        self.finalprice_var.get(),
        self.prn_var.get()
    ))
        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success", "Member has been updated")



    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Prachi@12",database="project")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM library")
        rows= my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for row in rows:
                self.library_table.insert("",END,values=row)
            conn.commit()
            conn.close()

    def get_cursor(self,event=""):
            cursor_row=self.library_table.focus()
            content=self.library_table.item(cursor_row)
            row=content['values']

            self.member_var.set(row[0]),
            self.prn_var.set(row[1]),
            self.id_var.set(row[2]),
            self.Firstname_var.set(row[3]),
            self.lastname_var.set(row[4]),
            self.address1_var.set(row[5]),
            self.address2_var.set(row[6]),
            self.postcode_var.set(row[7]),
            self.mobile_var.set(row[8]),
            self.bookid_var.set(row[9]),
            self.booktitle_var.set(row[10]),
            self.author_var.set(row[11]),
            self.dateborrowed_var.set(row[12]),
            self.datedue_var.set(row[13]),
            self.daysonbook_var.set(row[14]),
            self.lateratefine_var.set(row[15]),
            self.dateoverdue_var.set(row[16]),
            self.finalprice_var.set(row[17])


    def showData(self):
        self.txtBox.insert(END,"Member Type:\t" + self.member_var.get()+ "\n")
        self.txtBox.insert(END, "PRN No:\t" + self.prn_var.get() + "\n")
        self.txtBox.insert(END, "Id No:\t" + self.id_var.get() + "\n")
        self.txtBox.insert(END, "First name:\t" + self.Firstname_var.get() + "\n")
        self.txtBox.insert(END, "Last name:\t" + self.lastname_var.get() + "\n")  
        self.txtBox.insert(END, "Address1:\t" + self.address1_var.get() + "\n")
        self.txtBox.insert(END, "Address2:\t" + self.address2_var.get() + "\n")
        self.txtBox.insert(END, "Postcode:\t" + self.postcode_var.get() + "\n")
        self.txtBox.insert(END, "Mobile:\t" + self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "Book id:\t" + self.bookid_var.get()  + "\n")
        self.txtBox.insert(END, "Book title:\t" +self.booktitle_var.get() + "\n")
        self.txtBox.insert(END, "Author:\t" +self.author_var.get()  + "\n")
        self.txtBox.insert(END, "Date borrowed:\t" + self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END, "Date due:\t" + self.datedue_var.get() + "\n")
        self.txtBox.insert(END, "Days on book:\t" + self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END, "Late return fine:\t" + self.lateratefine_var.get()+ "\n")
        self.txtBox.insert(END, "Date over due:\t" + self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END, "Actual price:\t" + self.finalprice_var.get()  + "\n")

    def reset(self):
        self.member_var.set(" "),
        self.prn_var.set(" "),
        self.id_var.set(" "),
        self.Firstname_var.set(" "),
        self.lastname_var.set(""),
        self.address1_var.set(" "),
        self.address2_var.set(" "),
        self.postcode_var.set(" "),
        self.mobile_var.set(" "),
        self.bookid_var.set(" "),
        self.booktitle_var.set(" "),
        self.author_var.set(" "),
        self.dateborrowed_var.set(" "),
        self.datedue_var.set(" "),
        self.daysonbook_var.set(" "),
        self.lateratefine_var.set(" "),
        self.dateoverdue_var.set(" "),
        self.finalprice_var.set(" ")
        self.txtBox.delete("1.0",END)
        
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit?")
        if iExit>0:
            self.root.destroy()
            return
        
    def delete(self):
        if self.prn_var.get() == " " or self.id_var.get() == " ":
         messagebox.showerror("Error", "First Select The Member")
        else:
         conn = mysql.connector.connect(host="localhost", username="root", password="Prachi@12", database="project")
        my_cursor = conn.cursor()
        query = "DELETE FROM library WHERE PRN_NO=%s"
        value = (self.prn_var.get(),) 
        my_cursor.execute(query, value)

        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success", "Member has been Deleted")



if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()