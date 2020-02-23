from tkinter import *
from tkinter import ttk  # provide combo box
from PIL import ImageTk
import pymysql


class Admin_resources:
    def __init__(self, window):
        self.window = window
        self.window.title("GU  Student Management System")
        self.window.geometry("1350x700+0+0")  # xAxis_x_yAxis_+_xStartFrom_+_yStartFrom

        # Setting up images
        self.bg_icon = ImageTk.PhotoImage(file="Images/bg_image.jpg")
        self.user_icon = ImageTk.PhotoImage(file="Images/user_icon.png")
        self.pass_icon = ImageTk.PhotoImage(file="Images/pass_icon.jpg")
        self.logo_icon = ImageTk.PhotoImage(file="Images/logo.jpg")

        # ========= Setting all Variables ====================
        self.son_var = StringVar()
        self.name_var = StringVar()
        self.roll_no_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.address_var = StringVar()
        self.dob_var = StringVar()

        # BACKGROUND IMAGE
        bg_lbl = Label(self.window, image=self.bg_icon).pack()

        # Lables
        title = Label(self.window, text="GU  Student Management System", font=("times new roman", 40, "bold"),
                      bg="yellow", fg="red", bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)  # relwidth =1 --> set relative width according to window

        # --------Manage frame--------------------------------------------------

        # Crimson box Left Side
        Manage_Frame = Frame(self.window, bd=4, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=450, height=570)

        # Title Bar
        m_title = Label(Manage_Frame, text="Manage Student", bg="crimson", fg="white",
                        font=("times new roman", 40, "bold"))
        m_title.grid(row=0, columnspan=2, pady=10)

        # Name
        lbl_Name = Label(Manage_Frame, text="Name.", bg="crimson", fg="white",
                         font=("times new roman", 20, "bold"))
        lbl_Name.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Name = Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_Name.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        # Roll number
        lbl_roll = Label(Manage_Frame, text="Roll No.", bg="crimson", fg="white",
                         font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Roll = Entry(Manage_Frame, textvariable=self.roll_no_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        txt_Roll.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        # Email
        lbl_Email = Label(Manage_Frame, text="Email ID.", bg="crimson", fg="white",
                          font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(Manage_Frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        # Gender
        lbl_Gender = Label(Manage_Frame, text="Gender.", bg="crimson", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman", 13, "bold"),
                                    state="readonly")
        combo_gender["values"] = ("Male", "Female", "Other")
        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        # Contact Number
        lbl_phone = Label(Manage_Frame, text="Contact No.", bg="crimson", fg="white",
                          font=("times new roman", 20, "bold"))
        lbl_phone.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_phone = Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        txt_phone.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        # Date of Birth
        lbl_dof = Label(Manage_Frame, text="DOF(dd/mm/yyyy)", bg="crimson", fg="white",
                        font=("times new roman", 15, "bold"))
        lbl_dof.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_dof = Entry(Manage_Frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5,
                        relief=GROOVE)
        txt_dof.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        # Address
        lbl_address = Label(Manage_Frame, text="Address", bg="crimson", fg="white",
                            font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_address = Entry(Manage_Frame, textvariable=self.address_var, font=("times new roman", 15, "bold"), bd=5,
                            relief=GROOVE)
        txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # ------------- Button Frame ---------------
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=2, y=500, width=438)

        add_btn = Button(btn_Frame, command=self.addStudent, text="Add", width=10).grid(row=0, column=0, padx=3,
                                                                                        pady=10)
        update_btn = Button(btn_Frame, command=self.update_data, text="Update", width=10).grid(row=0, column=1, padx=3,
                                                                                               pady=10)
        # insert_btn = Button(btn_Frame, text="Insert", width=10).grid(row=0, column=2, padx=3, pady=10)
        delete_btn = Button(btn_Frame, command=self.deleteData(), text="Delete", width=10).grid(row=0, column=3, padx=3,
                                                                                                pady=10)
        clear_btn = Button(btn_Frame, command=self.clear, text="Clear", width=10).grid(row=0, column=4, padx=3, pady=10)

        # ------Details Frame---------------------------------------------------
        # Crimson box Right Side
        Detail_Frame = Frame(self.window, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=490, y=100, width=830, height=570)


        container = ttk.Frame(root)
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        # Search Frame---------
        search_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        search_Frame.place(x=5, y=5, width=810)

        lbl_search = Label(search_Frame, text="Search By", bg="crimson", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=3, padx=3, sticky="w")

        combo_search = ttk.Combobox(search_Frame, font=("times new roman", 13, "bold"), state="readonly")
        combo_search["values"] = ("ID", "Name", "Contact")
        combo_search.grid(row=0, column=1, pady=3, padx=3, sticky="w")

        txt_search = Entry(search_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=3, padx=3, sticky="w")

        search_btn = Button(search_Frame, text="Search", width=10).grid(row=0, column=3, padx=3, pady=3)
        showAll_btn = Button(search_Frame, text="Show All", width=10).grid(row=0, column=4, padx=3, pady=3)

        # Table Frame ------------------------------------
        table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        table_Frame.place(x=5, y=60, width=810, height=500)

        scroll_x = Scrollbar(table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_Frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_Frame,
                                          columns=("name", "roll", "gender", "contact", "dob", "email", "address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll No.")
        self.student_table.heading("email", text="Email ID")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("contact", text="Contact No.")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("address", text="Address")

        self.student_table["show"] = "headings"

        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("email", width=150)
        self.student_table.column("gender", width=100)
        self.student_table.column("contact", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("address", width=200)
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.update_data()
        self.fetchData()

    def addStudent(self):
        connection = pymysql.connect(host="localhost", user="root", password="", database="gu_student_managment_system")
        cursor = connection.cursor()
        cursor.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (self.name_var.get(),
                                                                             self.roll_no_var.get(),
                                                                             self.gender_var.get(),
                                                                             self.contact_var.get(),
                                                                             self.dob_var.get(),
                                                                             self.email_var.get(),
                                                                             self.address_var.get()))
        connection.commit()
        self.fetchData()
        self.clear()
        connection.close()

    def fetchData(self):
        connection = pymysql.connect(host="localhost", user="root", password="", database="gu_student_managment_system")
        cursor = connection.cursor()
        cursor.execute("select * from students")

        rows = cursor.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
            connection.commit()
        connection.close()

    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.contact_var.set("")
        self.gender_var.set("")
        self.dob_var.set("")
        self.address_var.set("")

    def get_cursor(self, even):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents["values"]

        self.name_var.set(row[0])
        self.roll_no_var.set(row[1])
        self.gender_var.set(row[2])
        self.contact_var.set(row[3])
        self.dob_var.set(row[4])
        self.email_var.set(row[5])
        self.address_var.set(row[6])

        self.address_var.set("")
        self.address_var.set(row[6])

    def update_data(self):
        connection = pymysql.connect(host="localhost", user="root", password="", database="gu_student_managment_system")
        cursor = connection.cursor()
        cursor.execute("update students set name=%s,gender=%s,email=%s,contact=%s,dob=%s,address=%s where roll_no=%s",
                       (self.name_var.get(),
                        self.gender_var.get(),
                        self.email_var.get(),
                        self.contact_var.get(),
                        self.dob_var.get(),
                        self.address_var.get(),
                        self.roll_no_var.get()))

        connection.commit()
        #self.fetchData()
        connection.close()
        self.clear()

    def deleteData(self):
        connection = pymysql.connect(host="localhost", user="root", password="", database="gu_student_managment_system")
        cursor = connection.cursor()
        cursor.execute("delete from students where roll_no=%s", self.roll_no_var.get())

        #self.fetchData()
        self.clear()

        rows = cursor.fetchall()

        connection.commit()
        connection.close()


window = Tk()
obj = Admin_resources(window)
window.mainloop()
