import mysql.connector
from tkinter import *
db = mysql.connector.connect(user='root', password='rootmysql',
                              host='127.0.0.1', database='blood_group_db',
                              auth_plugin='caching_sha2_password')


cursor = db.cursor()

root = Tk()
image1 = PhotoImage(file="/Users/jeetu/Desktop/blood.png")
panel = Label(root, image=image1, bg="black").place(x=0, y=0, relwidth=1, relheight=1)
root.title("BLOOD TYPING TEST")
root.geometry("1920x1080")
root.configure(background='white')

l1 = Label(root, text="Enter New Report", bg='green2', font="Helvetica 12").place(x=80, y=100,w=300, h=40)
b1 = Button(root, text="Click To Enter", command=lambda: donordetails()).place(x=80, y=150)

l2 = Label(root, text="View All Reports", bg='green2', font="Helvetica 12").place(x=80, y=200,w=300, h=40)
b2 = Button(root, text="Click To View", command=lambda: requestall()).place(x=80, y=250)


l3 = Label(root, text="View By Blood Group", bg='green2', font="Helvetica 12").place(x=80, y=300, w=300,h=40)
b3 = Button(root, text="Click To View", command=lambda: requestblood()).place(x=80, y=350)

l4 = Label(root, text="View By Phone Number", bg='green2', font="Helvetica 12").place(x=80, y=400, w=300,h=40)
b4 = Button(root, text="Click To View", command=lambda: requestphone()).place(x=80, y=450)

b2 = Button(root, text="Exit", command=lambda: stop(root)).place(x=80, y=500)
v = StringVar()

def sel():
   selection = "You selected the option " + v.get()



def insertDonor(name,age,sex,phone,Blood_group, rh_val,root):

    insert = "INSERT INTO report(Name,Age,Sex,Phone,Blood_group, Rh_val) VALUES('" + name + "','" + age + "','" + sex + "','" + phone + "','" + Blood_group + "','" + rh_val + "')"

    try:
        cursor.execute(insert)
        db.commit()
        l6 = Label(root, text="Report Entered To Database successfully!", bg='lawn green', font="Helvetica 12").place(x=40, y=380)

    except:
        db.rollback()
        l6 = Label(root, text="Failed ! Please Enter The Correct Details", bg='lavender', font="Helvetica 12").place(x=40, y=380)



def retrieve_all():
    request = "select * from report"

    try:
        cursor.execute(request)
        rows = cursor.fetchall()
        db.commit()
        return rows
    except Exception as e:
        db.rollback()


def retrieve_Blood(bg):
    request = "select * from report where Blood_group='" + bg + "'"

    try:
        cursor.execute(request)
        rows = cursor.fetchall()
        db.commit()

        return rows
    except:
        db.rollback()

def retrieve_phone(phn):
    request = "select * from report where Phone='" + phn + "'"

    try:
        cursor.execute(request)
        rows = cursor.fetchall()
        db.commit()
        return rows
    except:
        db.rollback()

def donordetails():
    # global v
    root = Toplevel()
    root.title("BLOOD BANK")
    root.geometry("1024x768")
    root.configure(background='#FF8F8F')
    l1 = Label(root, text="Name:", bg='white', font="Helvetica 12").place(x=40, y=40)
    l2 = Label(root, text="Age:", bg='white', font="Helvetica 12").place(x=40, y=80)
    l3 = Label(root, text="Sex:", bg='white', font="Helvetica 12").place(x=40, y=120)
    l4 = Label(root, text="Phone:", bg='white', font="Helvetica 12").place(x=40, y=220)
    l5 = Label(root, text="Blood_Group", bg='white', font="Helvetica 12").place(x=40, y=260)
    l6 = Label(root, text="Rh_val", bg='white', font="Helvetica 12").place(x=40, y=300)

    e1 = Entry(root)
    e1.place(x=120, y=40)
    e2 = Entry(root)
    e2.place(x=120, y=80)
    r1 = Radiobutton(root, text="Male", variable=v, value="Male", command=sel).place(x=120, y=120)
    r2 = Radiobutton(root, text="Female", variable=v, value="Female", command=sel).place(x=120, y=150)
    r3 = Radiobutton(root, text="Other", variable=v, value="Other", command=sel).place(x=120, y=180)
    e3=Entry(root)
    e3.place(x=120,y=220)
    e4 = Entry(root)
    e4.place(x=120, y=260)
    e5 = Entry(root)
    e5.place(x=120, y=300)

    b2=Button(root,text="Back",command=lambda : stop(root)).place(x=120,y=340)
    b1=Button(root,text="Submit",command=lambda : [insertDonor(e1.get(),e2.get(),v.get(),e3.get(),e4.get(),e5.get(),root)]).place(x=40,y=340)

    root.mainloop()



def grid1():
    root = Tk()
    root.title("LIST OF REPORTS")
    root.geometry("750x500")
    root.configure(background='#0C43F0')
    rows = retrieve_all()
    x = 0
    for row in rows:
        l1 = Label(root, text=row[0], bg="#1EDEF2", font="Verdana 15 bold").grid(row=x, column=0, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l2 = Label(root, text=row[1], bg="#1EDEF2", font="Verdana 15 bold").grid(row=x, column=1, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l3 = Label(root, text=row[2], bg="#1EDEF2", font="Verdana 15 bold").grid(row=x, column=2, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l4 = Label(root, text=row[3], bg="#1EDEF2", font="Verdana 15 bold").grid(row=x, column=3, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l5 = Label(root, text=row[4], bg="#1EDEF2", font="Verdana 15 bold").grid(row=x, column=4, sticky='E', padx=5,
                                                                                 pady=5, ipadx=5, ipady=5)
        l6 = Label(root, text=row[5], bg="#1EDEF2", font="Verdana 15 bold").grid(row=x, column=5, sticky='E', padx=5,
                                                                        pady=5, ipadx=5, ipady=5)
        x = x + 1
    root.mainloop()

def grid2(bg):
	root=Tk()
	root.title("List Of Persons With "+str(bg)+" Blood")
	root.geometry("750x500")
	root.configure(background='#0C43F0')
	rows=retrieve_Blood(bg)
	x=0
	for row in rows:
		l1=Label(root,text=row[0],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=0,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		l2=Label(root,text=row[1],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=1,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		l3=Label(root,text=row[2],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=2,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		l4=Label(root,text=row[3],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=3,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		l5=Label(root,text=row[4],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=4,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		l6=Label(root,text=row[5],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=5,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		x=x+1
	root.mainloop()

def grid3(phone_num):
	root=Tk()
	root.title("List Of Persons With Phone"+str(phone_num))
	root.geometry("750x500")
	root.configure(background='#0C43F0')
	rows=retrieve_phone(phone_num)
	x=0
	for row in rows:
		l1=Label(root,text=row[0],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=0,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		l2=Label(root,text=row[1],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=1,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		l3=Label(root,text=row[2],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=2,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		l4=Label(root,text=row[3],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=3,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		l5=Label(root,text=row[4],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=4,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		l6=Label(root,text=row[5],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=5,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
		x=x+1
	root.mainloop()


def requestall():
    grid1()


def requestblood():
	root=Tk()
	root.title("People with specified blood")
	root.geometry("1024x720")
	root.configure(background='#FF8F8F')
	l=Label(root,text="Enter the blood group").place(x=50,y=50,w=400,h=40)
	e=Entry(root)
	e.place(x=500,y=60)
	b2=Button(root,text="Back",command=lambda : stop(root)).place(x=600,y=100)
	b=Button(root,text="ENTER",command=lambda : grid2(e.get())).place(x=500,y=100)
	root.mainloop()

def requestphone():
	root=Tk()
	root.title("People with specified phone number")
	root.geometry("1024x720")
	root.configure(background='#FF8F8F')
	l=Label(root,text="Enter the phone number").place(x=50,y=50,w=400,h=40)
	e=Entry(root)
	e.place(x=500,y=60)
	b2=Button(root,text="Back",command=lambda : stop(root)).place(x=600,y=100)
	b=Button(root,text="ENTER",command=lambda : grid3(e.get())).place(x=500,y=100)
	root.mainloop()

def stop(root):
    root.destroy()

root.mainloop()