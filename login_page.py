from tkinter import *
from tkinter import ttk  # provide combo box
from PIL import ImageTk
import pymysql
from tkinter import messagebox



class Login_page:

    def __init__(self,window):
        self.window = window
        self.window.title("Login Page")
        self.window.geometry("1350x700")

        # BACKGROUND IMAGE
        self.bg_icon = ImageTk.PhotoImage(file="Images/bg_image.jpg")
        bg_lbl = Label(self.window, image=self.bg_icon).pack()

        # ========= Setting all Variables ====================
        self.password_var = StringVar()
        self.son_var = StringVar()
        self.name_var = StringVar()
        self.roll_no_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.address_var = StringVar()
        self.dob_var = StringVar()
        self.authorization_var=StringVar


        # -----------------------------------------------------------------
        # Lables
        title = Label(self.window, text="Login And Register New Account", font=("times new roman", 40, "bold"),
                      bg="yellow", fg="red", bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)  # relwidth =1 --> set relative width according to window

        # Crimson box Left Side
        Manage_Frame = Frame(self.window, bd=4, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=450, height=570)

        # Title Bar
        m_title = Label(Manage_Frame, text="Login", bg="crimson", fg="white",
                        font=("times new roman", 40, "bold"))
        m_title.grid(row=0, columnspan=2, pady=10,sticky=NSEW)

        # --------------------------------------------------------
        # Roll_no.
        lbl_roll_no = Label(Manage_Frame, text="Roll NO.", bg="crimson", fg="white",
                         font=("times new roman", 20, "bold"))
        lbl_roll_no.grid(row=1, column=0, pady=30, padx=20, sticky="w")

        txt_roll_no = Entry(Manage_Frame, textvariable=self.roll_no_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_roll_no.grid(row=1, column=1, pady=30, padx=20, sticky="w")

        # Password
        lbl_Password = Label(Manage_Frame, text="Password.", bg="crimson", fg="white",
                         font=("times new roman", 20, "bold"))
        lbl_Password.grid(row=2, column=0, pady=30, padx=20, sticky="w")

        txt_Password = Entry(Manage_Frame, textvariable=self.password_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_Password.grid(row=2, column=1, pady=30, padx=20, sticky="w")

        # ------------- Button Frame ---------------
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=80, y=300, width=300, height=100)

        login_btn = Button(btn_Frame,command=self.login_process, text="Login", width=10).grid(row=0, column=0, padx=30,
                                                                                        pady=30)

        registration_btn = Button(btn_Frame,command=self.registration_pressed,  text="Registration", width=10).grid(row=0, column=1, padx=30,
                                                                                             pady=30)


        # ------Details Frame---------------------------------------------------
        # Crimson box Right Side
        self.Detail_Frame = Frame(self.window, bd=4, relief=RIDGE, bg="crimson")
        self.Detail_Frame.place(x=490, y=100, width=830, height=570)

    #-------------------------------------------
    def login_pressed(self):
        connection = pymysql.connect(host="localhost", user="root", password="", database="gu_student_managment_system")
        cursor = connection.cursor()
        cursor.execute("select * from students where roll_no = %s",(self.roll_no_var.get()))

        rows = cursor.fetchall()
        connection.close()
        print(rows)

        # ----Warning if no data (Wrong roll no.)
        if len(rows) ==0:
            messagebox.showwarning("Warning","Write Right Roll no.")
        else:
            # Setting all variable
            self.name_var.set(rows[0][0])
            self.roll_no_var.set(rows[0][1])
            self.gender_var.set(rows[0][2])
            self.contact_var.set(rows[0][3])
            self.dob_var.set(rows[0][4])
            self.email_var.set(rows[0][5])
            self.address_var.set(rows[0][6])

            self.address_var.set("")
            self.address_var.set(rows[0][6])


            self.Show_Data()

    def login_process(self):
        connection = pymysql.connect(host="localhost", user="root", password="", database="gu_student_managment_system")
        cursor = connection.cursor()
        cursor.execute("select * from login_process where roll_no = %s", (self.roll_no_var.get()))

        rows = cursor.fetchall()
        connection.close()
        if len(rows) ==0:
            messagebox.showwarning("Login","Enter correct Roll Number")
        else:
            if self.password_var.get() == rows[0][1]:
                if rows[0][2]=="Admin":
                    self.window.destroy()
                    import Adim_resources
                else:
                    self.login_pressed()
            else:
                messagebox.showwarning("Login","Wrong Password")

    def Show_Data(self):
        # Title Bar
        m_title = Label(self.Detail_Frame, text="Details Of Student", bg="crimson", fg="white",
                        font=("times new roman", 40, "bold"))
        m_title.grid(row=0, columnspan=2, pady=10)
        # Name
        lbl_Name = Label(self.Detail_Frame, text="Name.", bg="crimson", fg="white",
                         font=("times new roman", 20, "bold"))
        lbl_Name.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Name = Entry(self.Detail_Frame,state='disabled', textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_Name.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        # Roll number
        lbl_roll = Label(self.Detail_Frame, text="Roll No.", bg="crimson", fg="white",
                         font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Roll = Entry(self.Detail_Frame,state='disabled', textvariable=self.roll_no_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_Roll.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        # Email
        lbl_Email = Label(self.Detail_Frame, text="Email ID.", bg="crimson", fg="white",
                          font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(self.Detail_Frame,state='disabled', textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        # Gender
        lbl_Gender = Label(self.Detail_Frame, text="Gender.", bg="crimson", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(self.Detail_Frame, textvariable=self.gender_var, font=("times new roman", 13, "bold"),
                                    state="disabled")
        combo_gender["values"] = ("Male", "Female", "Other")
        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        # Contact Number
        lbl_phone = Label(self.Detail_Frame, text="Contact No.", bg="crimson", fg="white",
                          font=("times new roman", 20, "bold"))
        lbl_phone.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_phone = Entry(self.Detail_Frame,state='disabled', textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_phone.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        # Date of Birth
        lbl_dof = Label(self.Detail_Frame, text="DOF(dd/mm/yyyy)", bg="crimson", fg="white",
                        font=("times new roman", 15, "bold"))
        lbl_dof.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_dof = Entry(self.Detail_Frame,state='disabled', textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_dof.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        # Address
        lbl_address = Label(self.Detail_Frame, text="Address", bg="crimson", fg="white",
                            font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_address = Entry(self.Detail_Frame,state='disabled', textvariable=self.address_var, font=("times new roman", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

    def apply_registration(self):
        # Apply for registration
        connection = pymysql.connect(host="localhost", user="root", password="", database="gu_student_managment_system")
        cursor = connection.cursor()
        max_roll_no = cursor.execute("select max(roll_no) from login_process")
        print("max roll_no",max_roll_no)
        cursor.execute("insert into registration_process values(%s,%s,%s,%s,%s,%s,%s,%s)", (self.name_var.get(),
                                                                                         max_roll_no,
                                                                                        self.password_var.get(),
                                                                                         self.gender_var.get(),
                                                                                         self.contact_var.get(),
                                                                                         self.dob_var.get(),
                                                                                         self.email_var.get(),
                                                                                         self.address_var.get()))
        messagebox._show("Registration","Your Roll Number Is : ",max_roll_no," : Always Remember It")
        connection.commit()
        self.fetchData()
        self.clear()
        connection.close()

    def registration_pressed(self):
        print("registration")
        # Title Bar
        m_title = Label(self.Detail_Frame, text="Fill Details Of Student", bg="crimson", fg="white",
                        font=("times new roman", 40, "bold"))
        m_title.grid(row=0, columnspan=2, pady=10)
        # Name
        lbl_Name = Label(self.Detail_Frame, text="Name.", bg="crimson", fg="white",
                         font=("times new roman", 20, "bold"))
        lbl_Name.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Name = Entry(self.Detail_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_Name.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        # Password
        lbl_password = Label(self.Detail_Frame, text="Password", bg="crimson", fg="white",
                         font=("times new roman", 20, "bold"))
        lbl_password.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_password = Entry(self.Detail_Frame, textvariable=self.password_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_password.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        # Email
        lbl_Email = Label(self.Detail_Frame, text="Email ID.", bg="crimson", fg="white",
                          font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(self.Detail_Frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        # Gender
        lbl_Gender = Label(self.Detail_Frame, text="Gender.", bg="crimson", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(self.Detail_Frame, textvariable=self.gender_var, font=("times new roman", 13, "bold"),
                                    state="readonly")
        combo_gender["values"] = ("Male", "Female", "Other")
        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        # Contact Number
        lbl_phone = Label(self.Detail_Frame, text="Contact No.", bg="crimson", fg="white",
                          font=("times new roman", 20, "bold"))
        lbl_phone.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_phone = Entry(self.Detail_Frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_phone.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        # Date of Birth
        lbl_dof = Label(self.Detail_Frame, text="DOF(dd/mm/yyyy)", bg="crimson", fg="white",
                        font=("times new roman", 15, "bold"))
        lbl_dof.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_dof = Entry(self.Detail_Frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_dof.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        # Address
        lbl_address = Label(self.Detail_Frame,text="Address", bg="crimson", fg="white",
                            font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_address = Entry(self.Detail_Frame, textvariable=self.address_var, font=("times new roman", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # Gender
        lbl_authorization = Label(self.Detail_Frame, text="Authorization", bg="crimson", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_authorization.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        combo_authorization = ttk.Combobox(self.Detail_Frame, textvariable=self.authorization_var,
                                    font=("times new roman", 13, "bold"),
                                    state="readonly")
        combo_authorization["values"] = ("Admin", "Student")
        combo_authorization.grid(row=8, column=1, pady=10, padx=20, sticky="w")

        # ------------- Button Frame ---------------

        btn_Frame2 = Frame(self.Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame2.place(x=600, y=10, width=95, height=58)

        registration_applied_btn = Button(btn_Frame2, command=self.apply_registration, text="Apply For \n Registration", width=10)
        registration_applied_btn.grid(row=0, column=0, padx=3,pady=3)







window = Tk()
screen = Login_page(window)

window.mainloop()

