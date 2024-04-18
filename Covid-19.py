print("----------------------------------------------------------------------")
print("------------Welcome to Covid Patients Management System---------------")
print("----------------------------------------------------------------------")
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="Vishwesh28")
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("create database if not exists covid")
mycursor.execute("use covid")
mycursor.execute("create table if not exists staff(sno varchar(25) not null, age varchar(25) not null, gender char(1) not null, post varchar(25) not null, salary varchar(25) not null)")
mycursor.execute("create table if not exists patients(sno varchar(25) not null, age varchar(25) not null, gender char(1) not null, date date not null)")
mycursor.execute("create table if not exists login(admin varchar(25) not null, password varchar(25) not null)")
mycursor.execute("create table if not exists sno(patient varchar(25), staff varchar(25) not null)")
mycursor.execute("select * from sno")
z = 0
for i in mycursor:
    z = 1
if z == 0:
    mycursor.execute("insert into sno values('0','0')")
    mydb.commit()
j = 0
mycursor.execute("select * from login")
for i in mycursor:
    j = 1
if j == 0:
    mycursor.execute("insert into login values('Admin','ng')")
    mydb.commit()
loop1 = 'y'
while loop1 == 'y' or loop1 == 'y':
    print("_______________________")
    print("1. Admin")
    print("2. Patient")
    print("3. Exit")
    print("_______________________")
    break
ch1 = int(input("Enter your choice: "))
if ch1 == 1:
    pas = input("Enter your Password: ")
    mycursor.execute("select * from login")
    for i in mycursor:
        username, password = i
        if pas == password:
            loop2 = 'n'
            while loop2 == 'n' or loop2 == 'N':
                print("______________________")
                print("1. Add Patients")
                print("2. Add Staff")
                print("3. Display Patients Record")
                print("4. Display Staff Record")
                print("5. Change Password")
                print("6. Remove Patients")
                print("7. Remove Staff")
                print("8. Logout")
                print("______________________")
                ch2 = int(input("Enter your choice : "))
                if ch2 == 1:
                    loop3 = 'y'
                    while loop3 == 'y' or loop3 == 'Y':
                        name = input("Enter patients name : ")
                        age = input("Enter patients age : ")
                        gender = input("Enter date of covid confiration : ")
                        mycursor.execute("select * from sno")
                        for i in mycursor:
                            patients, staff = i
                            patient = int(patient) + 1
                            mycursor.execute("insert into patients values('" + str(patient) + "', '" + name + "', '" + age + "', '" + gender + "', '" + date + "')")
                            mycursor.execute("update sno set patient = '" + str(patient) + "'")
                            mydb.commit()
                            print("Data of Patient has been saved successfully...")
                            mycursor.execute("select * from patients")
                            t = 0
                            for i in mycursor:
                                t += 1
                                t_id1, name, age1, gender1, date1 = i
                                print(f"Total number of Corona Infected patients--> {patients}")
                                print(f"Active Corona Cases--> {t}")
                                print(f"This patient with id {t_id1} will be in quarantine upto 14 days from {date1}")
                                loop3 = input("Do you want to enter more data of more patients (y/n): ")
                                loop2 = input("Do you want to logout (y/n) : ")
                elif ch2 == 2:
                    loop3 = 'y'
                    while loop3 == 'y' or loop3 == 'Y':
                        name = input("Enter New Staff Name : ")
                        age = input("Enter Age : ")
                        gender = input("Enter Gender (m/f) : ")
                        post = input("Enter Post : ")
                        salary = input("Enter Salary : ")
                        mycursor.execute("select * from sno")
                        for i in mycursor:
                            patient, staff = i
                            staff = int(staff) + 1
                            mycursor.execute("insert into staff values('" + str(staff) + "','" + name + "','" + age + "','" + gender + "','" + post + "','" + salary + "')")
                            mycursor.execute("update sno set staff = '" + str(staff) + "'")
                            mydb.commit()
                            print(f"staff with id (staff) has been saved successfully...")
                            mycursor.execute("select * from staff")
                            t = 0
                            for i in mycursor:
                                t += 1
                                print(f"Active Saff Members--> (t)")
                                loop3 = input("Do You Want To Enter More Staff Data (y/n) : ")
                                loop2 = input("Do you want to Logout (y/n) : ")
                elif ch2 == 3:
                    idd = input("Enter patients id : ")
                    t_id2, name2, age2, gender2, date2 = ["", "", "", "", ""]
                    mycursor.execute("select * from patients where sno = '" + idd + "'")
                    for i in mycursor:
                        t_id2, name2, age2, gender2, date2 = i
                        print("| ID | NAME | AGE | GENDER | CORONA CONFIRMATION DATE |")
                        print(f"| [t_id2] | [name2] | [age2] | [gender2] | [date2] |")
                elif ch2 == 4:
                    idd = input("Enter staff ID : ")
                    t_id3, name3, age3, gender3, post3, salary3 = ["", "", "", "", "", ""]
                    mydb.commit()
                    mycursor.execute("select * from staff where sno = '" + idd + "'")
                    for i in mycursor:
                        t_id3, name3, age3, gender3, post3, salary3 = i
                        print("| ID | NAME | AGE | GENDER | POST | SALARY |")
                        print(f"| [t_id3] | [name3] | [age3] | [gender3] | [post3] | [salary3] |")
                elif ch2 == 5:
                    pas = input("Enter old password : ")
                    mycursor.execute("select * from login")
                    for i in mycursor:
                        username, password = i
                        if pas == password:
                            npas = input("Enter new password : ")
                            mycursor.execute("update login set password = '" + npas + "'")
                            mydb.commit()
                        else:
                            print("Wrong Password...")
                elif ch2 == 6:
                    loop3 = 'y'
                    while loop3 == 'y' or loop3 == 'Y':
                        idd = input("Enter Patient ID : ")
                        mycursor.execute("delete from patients where sno = '" + idd + "'")
                        mydb.commit()
                        print("Patient have been removed successfully...")
                        loop3 = input("Do you want to Remove more patient (y/n) : ")
                elif ch2 == 7:
                    loop2 = 'y'
                    while loop3 == 'y' or loop3 == 'Y':
                        idd = input("Enter Staff ID : ")
                        mycursor.execute("delete from Staff where sno = '" + idd + "'")
                        mydb.commit()
                        print("Staff have been removed successfully...")
                        loop3 = input("Do you want to Remove more staff (y/n) : ")
                elif ch2 == 8:
                    break
elif ch1 == 2:
    print("Thank you for coming forward for your test... ")
    icough = input("Are you having cough (y/n) : ").lower()
    dry_cough = 'n'
    cough = 'n'
    sneeze = 'n'
    pain = 'n'
    weakness = 'n'
    mucus = 'n'
    if icough == 'y' or icough == 'Y':
        dry_cough = input("Are you having dry cough (y/n) : ").lower()
        cough = input("Are you having normal cough (y/n) : ").lower()
        sneeze = input("Are you having Sneeze (y/n) : ").lower()
        pain = input("Are you having bodypain (y/n) : ").lower()
        weakness = input("Are you having weakness (y/n) : ").lower()
        mucus = input("Are you having mucus (y/n) : ").lower()
        itemp = int(input("Please enter your body temperature : "))
        if itemp <= 100:
            temp = 'low'
        else:
            temp = 'high'
        breath = input("Are you having problem in breathing (y/n) : ").lower()
        if dry_cough == 'y' and sneeze == 'y' and pain == 'y' and weakness == 'y' and temp == 'high' and breath == 'y':
            print("You are covid positive.")
            name = input("Enter your name : ")
            age = input("Enter your age : ")
            gender = input("Enter your gender (m/f) : ")
            mycursor.execute("select * from sno")
            for i in mycursor:
                patient, staff = i
                patient = int(patient) + 1
                mycursor.execute("insert into patients values('" + str(patient) + "', '" + name + "', '" + age + "', '" + gender + "', now())")
                mycursor.execute("update sno set patient = '" + str(patient) + "'")
                mydb.commit()
                print("Data of patient have been saved successfully...")
                print(f"Total number of Corona Infected patients--> {patient}")
                mycursor.execute("select * from patients")
                t = 0
                for i in mycursor:
                    t += 1
                print(f"Active Corona cases--> {t}")
                mycursor.execute("select * from patients")
                for i in mycursor:
                    t_id5, name5, age5, gender5, date5 = i
                    print(f"This patient with id {t_id5} will be in quarantine for upto 14 days from {date5}")
        elif dry_cough == 'y' and sneeze == 'y' and pain == 'n' and weakness == 'n' and temp == 'low' and breath == 'n':
            print("Nothing to worry, its normal infection due to air pollutants...")
        elif cough == 'y' and mucus == 'y' and sneeze == 'y' and pain == 'n' and weakness == 'n' and temp == 'low' and breath == 'n':
            print("Don't worry, its just common cold...")
        else:
            print("You are not Corona infected, if not feeling well, just rest")
    print("If you don't feel better even after taking rest, please consult to a doctor.")
else:
    print("")  # debug this code with proper indentation
