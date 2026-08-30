from tkinter import *                                              #FOR CREATING GUI'S
import mysql.connector                                       #FOR CONNECTING PYTHON WITH MYSQL
from tkinter import messagebox                      #FOR CALLING MESSAGE BOX
from PIL import Image, ImageTk                     # Import Pillow for image handling
from datetime import datetime
import random

#SOME IMPORTANT COMMAND ALREADY RUN IN MY SQL 
'''
1. CREATE DATABASE IF NOT EXISTS GYM;
2. USE GYM;
3. create table if not exists fees(silver int,gold int,platinum int)
4. create table if not exists login(username varchar(25),password varchar(25))
5.CREATE TABLE IF NOT EXISTS member (did VARCHAR(8) PRIMARY KEY,name VARCHAR(50),gender CHAR(1),category VARCHAR(25),amt DECIMAL(10, 2));
6. create table if not exists trainer(id varchar(8),name varchar(25),age varchar(5),gender char,salary varchar(10)")
7.CREATE TABLE IF NOT EXISTS billing (id INT AUTO_INCREMENT PRIMARY KEY,member_id VARCHAR(8),billing_date DATE,amount DECIMAL(10, 2),payment_method VARCHAR(25),FOREIGN KEY (member_id) REFERENCES member(did));
8.CREATE TABLE IF NOT EXISTS attendance (id INT AUTO_INCREMENT PRIMARY KEY,member_id VARCHAR(8),attendance_date DATE,FOREIGN KEY (member_id) REFERENCES member(did));
9. insert into fees values(1000,900,800);
10. insert into login values ('admin', '1234')
'''
#Database Connectivity 
mydb = mysql.connector.connect(host='localhost', user='root', database='gym', password='fathersonji')
mycursor = mydb.cursor()
def login():
    log = Toplevel(root)
    log.title("login form")
    log.geometry("400x700")
    log.configure(background="#212122")      #black ink colour "#212122

    def check():
        afterlog = Toplevel(log)
        afterlog.title("REVIVE APKA APNA GYM")      # to change title
        afterlog.geometry("900x800")# Width x Height
        def memid():
#PREPARING TK INTER GUI FOR MEMBER LOGIN WINDOW
            mem = Toplevel(afterlog)
            mem.geometry("600x800")
            mem.title("MEMBER SIGN UP")
            mem.configure(background="#212122")  # black ink color "#212122"

            # Other labels and entries
            l1 =Label(mem, text="REVIVE", font="Algerian 55 bold", bg='#212122', fg='white', compound=TOP)
            l1.pack(fill=Y, pady=(50, 56))

            l2 =Label(mem, text="MEMBER NAME", font="ArialBaltic 25 bold", bg='#212122', fg='white', compound=CENTER)
            l2.pack(fill=Y, pady=(4, 6))

            e2 =Entry(mem, width=60)
            e2.pack(ipady=12, pady=(6, 26))

            f1 =Frame(mem, bg="#212122", relief=SUNKEN)
            f1.pack(side=LEFT, fill=X)

            l3 =Label(mem, text="GENDER", font="ArialBaltic 25 bold", bg='#212122', fg='white', compound=CENTER)
            l3.pack(fill=Y, pady=(4, 6))

            e3 =Entry(mem, width=60)
            e3.pack(ipady=12, pady=(6, 20))

            l4 =Label(mem, text="MEMBERSHIP", font="ArialBaltic 25 bold", bg='#212122', fg='white', compound=CENTER)
            l4.pack(fill=Y, pady=(4, 6))

            l5 = Label(mem, text="""PLATINUM     15000/year
            GOLD               12000/year
            SILVER             7500/year""", font="ArialBaltic 19 bold", bg='#212122', fg='#FF6961', compound=CENTER)
            l5.pack(fill=Y, pady=(4, 6))

            e5 =Entry(mem, width=60)
            e5.pack(ipady=12, pady=(6, 56))
    #FUNTION FOR PROCESS USER GIVEN COMMAND
            def mem2():
                name=e2.get()
                gender=e3.get()
                if e5=="silver"or e5=="Silver" or e5=="SILVER":
                    category='silver'
                    amt=7500
                elif e5=='gold'or e5=="GOLD" or e5=="Gold":
                    category='gold'
                    amt=12000
                else:
                    category='platinum'
                    amt=15000
                a=random.randint(0,9)
                b=random.randint(0,9)
                c=random.randint(0,9)
                d=random.randint(0,9)
                did='MEM'+str(a)+str(b)+str(c)+str(d)
                mycursor.execute('insert into member(did,name,gender,category,amt) values("{}","{}","{}","{}",{})'.format(did,name,gender,category,amt))
                mydb.commit()
                #MESSAGE BOX FOR MEMBER ID
                messagebox.showinfo("Success", f"your member id:---{did}")
                mem.destroy()
            #BUTTON FOR SIGN UP
            b1 = Button(mem, text="Sign Up", font="Arial 16 bold", fg="white", bg="#555555", compound=BOTTOM, activebackground="green", activeforeground="white", padx=20, pady=10, borderwidth=0, highlightthickness=0,command=mem2)
            b1.pack() 
            mem.mainloop()


        def TRAid():
                tra = Toplevel(afterlog)
                tra.geometry("800x1000")
                tra.configure(background="#212122")  # black ink colour "#212122"
                tra.title("trainer train")

                l1 = Label(tra, text="REVIVE", font="Algerian 55 bold", bg='#212122', fg='white', compound=CENTER)
                l1.pack(fill=Y, pady=(12, 20))

                l2 = Label(tra, text="TRAINER NAME", font="ArialBaltic 19 bold", bg='#212122', fg='white', compound=CENTER)
                l2.pack(fill=Y, pady=(4, 6))

                e2 = Entry(tra, width=60)
                e2.pack(ipady=12, pady=(6, 20))

                l3 = Label(tra, text="GENDER", font="ArialBaltic 19 bold", bg='#212122', fg='white', compound=CENTER)
                l3.pack(fill=Y, pady=(4, 6))

                e3 = Entry(tra, width=60)
                e3.pack(ipady=12, pady=(6, 20))

                l4 = Label(tra, text="TRAINERS AGE", font="ArialBaltic 19 bold", bg='#212122', fg='white', compound=CENTER)
                l4.pack(fill=Y, pady=(4, 6))

                e5 = Entry(tra, width=60)
                e5.pack(ipady=12, pady=(6, 20))

                l5 = Label(tra, text="SALARY WILL BE 9000/MONTH", font="ArialBaltic 19 bold", bg='#212122', fg='#FF6961', compound=CENTER)
                l5.pack(fill=Y, pady=(4, 6))

                # Load the image using Pillow
                image_path = "C:\\GYM MANAGMENT\\gettyimages-1437851885-612x612.jpg"
                image = Image.open(image_path)
                photo = ImageTk.PhotoImage(image)

                def TRA():
                    name = str(e2.get())
                    gender = str(e3.get())
                    age = str(e5.get())
                    salary = "9000"
                    a = random.randint(0, 9)
                    b = random.randint(0, 9)
                    c = random.randint(0, 9)
                    d = random.randint(0, 9)
                    tid = 'TRA' + str(a) + str(b) + str(c) + str(d)
                    mycursor.execute(f'insert into trainer values("{tid}","{name}","{age}","{gender}",{salary})')
                    mydb.commit()
                    messagebox.showinfo("Success", f"your member id:---{tid}")
                    tra.destroy()

                # Add the image to the frame
                l = Label(tra, image=photo, height=275, bg="#212122")
                l.image = photo  # Keep a reference to the image to prevent garbage collection
                l.pack(fill=X)

                b1 = Button(tra, text="Sign Up", font="Arial 16 bold", fg="white", bg="#555555", compound=BOTTOM, activebackground="green", activeforeground="white", padx=20, pady=10, borderwidth=0, highlightthickness=0, command=TRA)
                b1.pack(fill=Y)

                tra.mainloop()

        
        # Create a frame with a border and a sunken relief
        f1 = Frame(afterlog, bg="#212122", relief=SUNKEN)
        # Load the image using PhotoImage
        img_path ="C:\\GYM MANAGMENT\\c42a8c23165aa07f0b072a957379805d.jpg"                       #Replace with the actual path to your image file
        image = Image.open(img_path)
        photo = ImageTk.PhotoImage(image)
          
        gym = Label(afterlog,image=photo,height=750,width=700,bg="#212122")
        gym.pack(fill=X)

        # Create a button with customized appearance
        b1 = Button(f1, text="Add Member", font="Arial 24 bold", fg="white", bg="#555555", compound=BOTTOM, activebackground="green", activeforeground="white", padx=20, pady=10, borderwidth=3, highlightthickness=2, command=memid)
        b2 = Button(f1, text="Add Trainer", font="Arial 24 bold", fg="white", bg="#555555", compound=BOTTOM, activebackground="green", activeforeground="white", padx=20, pady=10, borderwidth=3, highlightthickness=2,command=TRAid)

        # Pack the frame at the bottom of the afterlog window, anchored to the southeast corner
        f1.pack(side=BOTTOM, fill=X) 

        # Pack the button inside the frame
        b1.pack(side=RIGHT, padx=20)
        b2.pack(side=LEFT, padx=20)

        # to make loop constant
        afterlog.mainloop()


    l1 = Label(log, text="REVIVE", font="Algerian 55 bold", bg='#212122', fg='white', compound=CENTER)
    l1.pack(fill=Y, pady=(50, 56))
    l2 = Label(log, text="USERNAME", font="ArialBaltic 19 bold", bg='#212122', fg='white', compound=CENTER)
    l2.pack(fill=Y, pady=(4, 6))

    e1 = Entry(log, width=60)
    e1.pack(ipady=12, pady=(6, 56))

    l3 = Label(log, text="PASSWORD", font="ArialBaltic 19 bold", bg='#212122', fg='white', compound=CENTER)
    l3.pack(fill=Y, pady=(4, 6))

    e2 = Entry(log, width=60)
    e2.pack(ipady=12, pady=(6, 56))


    def ch_log():
        u = e1.get()
        p = e2.get()
        mycursor.execute('select * from login')
        for i in mycursor:
            use, pas = i
            if pas == p and use == u:
                check()
            else:
                messagebox.showerror("Error", "Login failed")
                log.destroy()
    b1 = Button(log, text="Sign Up", font="Arial 16 bold", fg="white", bg="#555555", compound=BOTTOM, activebackground="green", activeforeground="white", padx=20, pady=10, borderwidth=0, highlightthickness=0, command=ch_log)
    b1.pack()
    log.mainloop()
def attendance():
    attend =Toplevel(root)
    attend.title("ATTENDANCE")      # to change title
    attend.geometry("800x700")                        # Width x Height

    def memattendance():
        mattend = Toplevel(attend)
        mattend.geometry("800x700")
        mattend.title('Member Attendance')
        mattend.configure(background="#212122")

        # Create a label for the application title
        l1 = Label(mattend, text="REVIVE", font="Algerian 55 bold", bg='#212122', fg='white', compound=TOP)
        l1.pack(fill=Y, pady=(20,10))

        # Create a label for the Member ID prompt
        l2 = Label(mattend, text="Member ID", font="ArialBaltic 25 bold", bg='#212122', fg='white', compound=CENTER)
        l2.pack(fill=Y, pady=(4, 6))

        # Create an entry widget for the Member ID input
        e2 = Entry(mattend, width=80)
        e2.pack(ipady=12, pady=(6, 26))

        # Load the image (make sure the image path is correct)
        img_path = "C:\\GYM MANAGMENT\\gettyimages-1437851885-612x612.jpg"  # Replace with the actual path to your image file
        image = Image.open(img_path)
        photo = ImageTk.PhotoImage(image)
        def membermark():
                member_id =e2.get()
                attendance_date = datetime.now().strftime('%Y-%m-%d')
                mycursor.execute("SELECT * FROM attendance WHERE member_id = {}".format(member_id))
                attendance_history = mycursor.fetchall()
                if attendance_history:
                    # Insert attendance record into the database
                    mycursor.execute("INSERT INTO attendance (member_id, attendance_date) VALUES (%s, %s)", (member_id, attendance_date))
                    mydb.commit()
                    messagebox.showinfo("Success", "Your Attendance Marked Sucessfully")
                else:
                    messagebox.showinfo("Error", "Your Attendance marking Failed")


        b1 = Button(mattend, text="Mark Your Attendance", font="Arial 16 bold", fg="white", bg="#555555", compound=BOTTOM, activebackground="green", activeforeground="white", padx=20, pady=10, borderwidth=0, highlightthickness=0,command=membermark)
        b1.pack(side=BOTTOM, padx=20)
            

        # Create a label to display the image
        img_label = Label(mattend, image=photo)
        img_label.pack()

        mattend.mainloop()


    def trainerattend():
        tattend =Toplevel(attend)
        tattend.geometry("800x700")
        tattend.title('Trainer Attendance')
        tattend.configure(background="#212122")

        # Create a label for the application title
        l1 = Label(tattend, text="REVIVE", font="Algerian 55 bold", bg='#212122', fg='white', compound=TOP)
        l1.pack(fill=Y, pady=(20,10))

        # Create a label for the Member ID prompt
        l2 = Label(tattend, text="Trainer ID", font="ArialBaltic 25 bold", bg='#212122', fg='white', compound=CENTER)
        l2.pack(fill=Y, pady=(4, 6))

        # Create an entry widget for the Member ID input
        e2 = Entry(tattend, width=80)
        e2.pack(ipady=12, pady=(6, 26))

        # Load the image (make sure the image path is correct)
        img_path = "C:\\GYM MANAGMENT\\360_F_317724775_qHtWjnT8YbRdFNIuq5PWsSYypRhOmalS.jpg"  # Replace with the actual path to your image file
        image = Image.open(img_path)
        photo = ImageTk.PhotoImage(image)

        #function for saving attendance report in database
        def traneirmark():
                trainer_id =str( e2.get())
                attendance_date = datetime.now().strftime('%Y-%m-%d')
                mycursor.execute("SELECT * FROM trainerattendance WHERE trainer_id = %s", (trainer_id))
                attendance_history = mycursor.fetchall()
                if attendance_history:
                    # Insert attendance record into the database
                    mycursor.execute("INSERT INTO trainerattendance (trainer_id, attendance_date) VALUES (%s, %s)", (trainer_id, attendance_date))
                    mydb.commit()
                    messagebox.showinfo("Success", "Your Attendance Marked Sucessfully")
                else:
                    messagebox.showinfo("Error", "Your Attendance marking Failed")
                    
        b1 = Button(tattend, text="Mark Your Attendance", font="Arial 16 bold", fg="white", bg="#555555", compound=BOTTOM, activebackground="green", activeforeground="white", padx=20, pady=10, borderwidth=0, highlightthickness=0,command=traneirmark)
        b1.pack(side=BOTTOM, padx=20)
        

        # Create a label to display the image
        img_label = Label(tattend, image=photo)
        img_label.pack()

        tattend.mainloop()


    # Create a frame with a border and a sunken relief
    f1 = Frame(attend, bg="#212122", relief=SUNKEN)
    f2 = Frame(attend,bg="#212122",relief=GROOVE)
    # Create a button with customized appearance
    b1 = Button(f1, text="Member Attendance", font="Arial 16 bold", fg="white", bg="#555555", compound=BOTTOM,activebackground="green", activeforeground="white", padx=20, pady=10, borderwidth=0, highlightthickness=0,command=memattendance)
    b2 = Button(f1, text="TrainerAttendance", font="Arial 16 bold", fg="white", bg="#555555", compound=BOTTOM,activebackground="green", activeforeground="white", padx=20, pady=10, borderwidth=0, highlightthickness=0,command=trainerattend)
    # Load the image using Pillow
    image = "C:\\GYM MANAGMENT\\Screenshot 2024-07-11 185457.png"
    photo = PhotoImage(file=image)
    # Create a label with the image as the background 
    gym = Label(f2, text="REVIVE", image=photo, font="Algerian 79 bold", bg='#212122', fg='white', compound=CENTER)
    gym.pack(fill=X)
    # Pack the frame at the bottom of the attend window, anchored to the southeast corner
    f1.pack(side=BOTTOM,fill=X) 
    f2.pack(fill=X,side=TOP)
    # Pack the button inside the frame
    b1.pack(padx=50,side=RIGHT)
    b2.pack(padx=50,side=LEFT)

    attend.mainloop()

def bmi_measure():
    bmi=Toplevel(root)
    bmi.geometry("600x600")
    bmi.configure(background="#212122")
    bmi.title("BMI Calculator For Diet Plan")
    def diet_chart():
        height=float(e2.get())
        weight=float(e3.get())
        bmi_level=weight/height/height*10000
        if bmi_level>=25:
                dc=Tk()
                dc.geometry("1200x1000")
                dc.configure(background="#212122")
                dc.title("Diet Chart")
                l1 =Label(dc, text="DIET PLAN", font="Algerian 45 bold", bg='#212122', fg='white', compound=TOP)
                l1.pack(fill=Y, pady=(10, 10))
                l2=Label(dc, text="""=======Monday======
    Breakfast (8:00-8:30AM)	1 onion stuffed chapatti + 1/2 cup low fat curd
    Mid-Meal (11:00-11:30AM)	1 cup coconut water
    Lunch (2:00-2:30PM)	1 cup moong dal/ chicken curry + 1 chapatti + salad
    Evening (4:00-4:30PM)	1 cup pomegranate
    Dinner (8:00-8:30PM)	1 cup beans + 1 chapatti + salad
    =======Tuesday=======
    Breakfast (8:00-8:30AM)	2 besan cheela + 1/2 cup low fat curd
    Mid-Meal (11:00-11:30AM)	1 apple
    Lunch (2:00-2:30PM)	1 cup masoor dal + 1 chapatti + 1/2 up low fat curd + salad
    Evening (4:00-4:30PM)	1 cup tomato soup
    Dinner (8:00-8:30PM)	1 cup carrot peas vegetable +1 chapatti + salad
    =======Wednesday======
    Breakfast (8:00-8:30AM)	1 cup vegetable brown bread upma + 1/2 cup low fat milk (no sugar)
    Mid-Meal (11:00-11:30AM)	1 cup musk melon
    Lunch (2:00-2:30PM)	1 cup rajma curry + 1 chapatti + salad
    Evening (4:00-4:30PM)	1 cup vegetable soup
    Dinner (8:00-8:30PM)	1 cup parwal vegetable + 1 chapatti + salad
    =======Thursday========
    Breakfast (8:00-8:30AM)	1 cucmber hungcurd sandwich + 1/2 tsp green chutney + 1 orange
    Mid-Meal (11:00-11:30AM)	1 cup buttermilk
    Lunch (2:00-2:30PM)	1 cup white chana/ fish curry + 1 chapatti + salad
    Evening (4:00-4:30PM)	1 cup low fat milk (no sugar)
    Dinner (8:00-8:30PM)	1 cup cauliflower vegetable + 1 chapatti + salad
    =======Friday=======
    Breakfast (8:00-8:30AM)	1 cup vegetable poha + 1 cup low fat curd
    Mid-Meal (11:00-11:30AM)	1 cup watermelon
    Lunch (2:00-2:30PM)	1 cup chana dal + 1 chapatti + salad
    Evening (4:00-4:30PM)	1 cup sprouts salad
    Dinner (8:00-8:30PM)	1 cup tinda vegetable + 1 chapatti + salad
    =======Saturday=======
    Breakfast (8:00-8:30AM)	1 cup low fat milk with oats + 3-4 strawberries
    Mid-Meal (11:00-11:30AM)	1 cup coconut water
    Lunch (2:00-2:30PM)	1 cup soybean curry + 1 chapatti + 1/2 cup low fat curd + salad
    Evening (4:00-4:30PM)	1 cup fruit salad
    Dinner (8:00-8:30PM)	1 cup ghia vegetable + 1 chaptti + salad""", font="Arialbaltic 12 bold", bg='#212122', fg='white', compound=TOP)

                l2.pack(fill=Y)
                dc.mainloop()
        else:
            dc=Tk()
            dc.geometry("1500x1000")
            dc.configure(background="#212122")
            dc.title("Diet Chart")
            l1 =Label(dc, text="DIET PLAN", font="Algerian 45 bold", bg='#212122', fg='white', compound=TOP)
            l1.pack(fill=Y, pady=(10, 10))
            l2=Label(dc, text="""======Monday======
Breakfast (8:00-8:30AM)	3 onion stuffed parantha + 1 cup curd + 3 cashews + 4 almonds + 2 walnuts
    Mid-Meal (11:00-11:30AM)	1 cup mango shake
    Lunch (2:00-2:30PM)	1 cup moong dal/ chicken curry + 1 cup potato and caulifllower vegetable + 3 chapatti + 1/2 cup rice + salad
    Evening (4:00-4:30PM)	1 cup pomegranate juice + 2 butter toasted bread
    Dinner (8:00-8:30PM)	1 cup beans potato vegetable + 3 chapatti + salad
    =======Tuesday======
    Breakfast (8:00-8:30AM)	3 paneer stuffed besan cheela + green chutney + 1 cup curd + 3 cashews + 4 almonds + 2 walnuts
    Mid-Meal (11:00-11:30AM)	1 apple smoothie with maple syrup
    Lunch (2:00-2:30PM)	1 cup masoor dal + 1 cup calocasia + 3 chapatti + 1/2 cup rice + 1 cup low curd + salad
    Evening (4:00-4:30PM)	1 cup tomato soup with bread crumbs + 1 cup aloo chaat
    Dinner (8:00-8:30PM)	1 cup carrot peas vegetable +3 chapatti + salad
    =======Wednesday=======
    Breakfast (8:00-8:30AM)	1.5 cup vegetable bread upma + 1 cup milk + 3 cashews + 4 almonds + 2 walnuts
    Mid-Meal (11:00-11:30AM)	1 cup ripe banana with 2 tsp ghee
    Lunch (2:00-2:30PM)	1 cup rajma curry + 1 cup spinach potato + 3 chapatti + 1/2 cup rice + salad
    Evening (4:00-4:30PM)	1 cup vegetable juice + 1 cup upma
    Dinner (8:00-8:30PM)	1.5 cup parwal vegetable + 3 chapatti + salad
    =======Thursday======
    Breakfast (8:00-8:30AM)	2 cucmber potato sandwich + 1 tsp green chutney + 1 orange juice + 3 cshews + 2 walnuts + 4 almonds
    Mid-Meal (11:00-11:30AM)	1 cup buttermilk + 1 cup sweet potato chaat
    Lunch (2:00-2:30PM)	1 cup white chana/ fish curry + 3 chapatti + 1/2 cup rice + salad
    Evening (4:00-4:30PM)	1 cup almond milk + banana
    Dinner (8:00-8:30PM)	1 cup cauliflower potato vegetable + 3 chapatti + salad
    ======Friday======
    Breakfast (8:00-8:30AM)	2 cup vegetable poha + 1 cup curd + 3 cashews + 4 almonds + 2 walnuts
    Mid-Meal (11:00-11:30AM)	2 cups watermelon juice
    Lunch (2:00-2:30PM)	1 cup chana dal + 1 cup bhindi vegetable + 3 chapatti + 1/2 cup rice + salad
    Evening (4:00-4:30PM)	1 cup sprouts salad + 2 potato cheela + green chutney
    Dinner (8:00-8:30PM)	1 cup peas mushroom vegetable + 3 chapatti + salad
    =======Saturday======
    Breakfast (8:00-8:30AM)	3 vegetable suji cheela + 1 cup strawberry shake + 4 cashews + 4 almonds + 3 walnuts
    Mid-Meal (11:00-11:30AM)	1 cup coconut water + 1 cup pomegrate
    Lunch (2:00-2:30PM)	1 cup mix dal + 1 cup soybean curry + 3 chapatti + 1/2 cup curd + salad
    Evening (4:00-4:30PM)	1 cup fruit salad + 4 pc vegetable cutlets + green chutney
    Dinner (8:00-8:30PM)	1 cup karela vegetable + 3 chaptti + salad""", font="Arialbaltic 12 bold", bg='#212122', fg='white', compound=TOP)

            l2.pack(fill=Y)
            dc.mainloop()

    l1 =Label(bmi, text="REVIVE", font="Algerian 45 bold", bg='#212122', fg='white', compound=TOP)
    l1.pack(fill=Y, pady=(30, 30))

    l2 =Label(bmi, text="Height in cm", font="ArialBaltic 30 italic",bg='#212122', fg='white', compound=CENTER)
    l2.pack(fill=Y, pady=(4, 6))

    e2 =Entry(bmi, width=70)
    e2.pack(ipady=12, pady=(6, 26))

    l3 =Label(bmi, text="Weight in kg", font="ArialBaltic 30 italic",bg='#212122', fg='white', compound=CENTER)
    l3.pack(fill=Y, pady=(4, 6))

    e3 =Entry(bmi, width=70)
    e3.pack(ipady=12, pady=(6, 26))

    b1 = Button(bmi, text="Calculate BMI (Body Mass Index)", font="Arial 16 bold", fg="white", bg="#555555", compound=BOTTOM, activebackground="green", activeforeground="white", padx=20, pady=10, borderwidth=0, highlightthickness=0,command=diet_chart)
    b1.pack(pady=(30,6)) 

    bmi.mainloop()




#MAIN PROGRAM STARTS

root =Tk()
root.title("REVIVE APKA APNA GYM")      # to change title
root.geometry("800x700")                        # Width x Height

# Create a frame with a border and a sunken relief
f1 = Frame(root, bg="#212122", relief=SUNKEN)
f2 = Frame(root,bg="#212122",relief=GROOVE)

# Load the image using Pillow
image = "C:\\GYM MANAGMENT\\Screenshot 2024-07-11 185457.png"
photo = PhotoImage(file=image)

# Create a label with the image as the background 
gym = Label(f2, text="REVIVE", image=photo, font="Algerian 79 bold", bg='#212122', fg='white', compound=CENTER)
gym.pack(fill=X)

# Create a button with customized appearance
b1 = Button(f1, text="Log In", font="Arial 16 bold", fg="white", bg="#555555", compound=BOTTOM,activebackground="green", activeforeground="white", padx=20, pady=10, borderwidth=0, highlightthickness=0,command=login)
b2 = Button(f1, text="Attendance", font="Arial 16 bold", fg="white", bg="#555555", compound=BOTTOM,activebackground="green", activeforeground="white", padx=20, pady=10, borderwidth=0, highlightthickness=0,command=attendance)
b3 = Button(f1, text="Diet Plan", font="Arial 16 bold", fg="white", bg="#555555", compound=BOTTOM,activebackground="green", activeforeground="white", padx=20, pady=10, borderwidth=0, highlightthickness=0,command=bmi_measure)

# Pack the frame at the bottom of the root window, anchored to the southeast corner
f1.pack(side=BOTTOM,fill=X) 
f2.pack(fill=X,side=TOP)

# Pack the button inside the frame

b1.pack(padx=30,side=RIGHT)
b2.pack(padx=30,side=LEFT)
b3.pack(padx=30,side=BOTTOM)

# to make loop constant
root.mainloop()
