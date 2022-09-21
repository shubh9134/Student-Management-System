
import mysql.connector
from mysql.connector import cursor
con = mysql.connector.connect(
    host="localhost", user="jittu1", password="<Jittu>12",database="student_management_system")
c=con.cursor()

# c.execute("CREATE TABLE IF NOT EXISTS student_details (ID int NOT NULL ,Name varchar(255) NOT NULL,Age int NOT NULL,Gender varchar(1) NOT NULL,class int NOT NULL,PRIMARY KEY (ID));")
# c.execute("ALTER r=c.fetchall("select * from student_details;")
# for i in r:
#     print(i)TABLE student_details AUTO_INCREMENT=1001;")
# c.execute("INSERT INTO student_details(Name,Age,Gender,Class) VALUES('Jitendra',22,'Manager',150000);")
# c.execute("INSERT INTO student_details(Name,Age,Gender,Class) VALUES('Ajay',21,'Chief_executive',170000);")
# con.commit()
# r=c.fetchall("select * from student_details;")
# for i in r:
#     print(i)

# c.execute('alter table student_details RENAME COLUMN class to Class;')
# c.commit()
# c.execute('select * from student_details;')
# for i in c:
#     print(i)
import re
from dns.rdatatype import SSHFP


def add_student(ID,Name,Age,Gender,Class):
    if check_student(ID)==True:
        print("student with this ID already exist\n Try again\n")
        main()
    else:
        cmd="INSERT INTO student_details VALUES(%s,%s,%s,%s,%s)"
        data=(ID,Name,Age,Gender,Class)
        c=con.cursor()
        c.execute(cmd,data)
        con.commit()
        print('student added successfully******************')
        print('\n')
        main()
    
def update_student_details(ID,Name,Age,Gender,Class):
    if check_student(ID)==True:
        cmd="update student_details set Name=%s,Age=%s,Gender=%s,Class=%s where ID=%s"
        data=(ID,Name,Age,Gender,Class)
        c=con.cursor()
        c.execute(cmd,data)
        con.commit()
        print('details updated successfully******************')
        print('\n')
        main()

    else:
        print("student with this ID does not exist in the database")
        print('\n')
        main()



def check_student_byname(Name):
    cmd="select * from student_details where Name=%s"
    data=(Name,)
    c=con.cursor(buffered=True)
    c.execute(cmd,data)
    r=c.rowcount
    if r==1:
        return True
    return False


def check_student(ID):
    cmd="select * from student_details where ID=%s"
    data=(ID,)
    c=con.cursor(buffered=True)
    c.execute(cmd,data)
    r=c.rowcount
    if r==1:
        return True
    return False

def remove_student(k):
    if k.isdigit()==True:
        if check_student(int(k))==True:
            cmd="delete from student_details where ID=%s"
            data=(int(k),)
            c=con.cursor()
            c.execute(cmd,data)
            con.commit()
            print("student removed successfully***********")
        else:
            print("student with this ID does not exist in the database\n*********Try again***********\n ")
    else:
        if check_student_byname(k)==True:
            cmd="delete from student_details where Name=%s"
            data=(k,)
            c=con.cursor()
            c.execute(cmd,data)
            con.commit()
            print("student removed successfully***********")
        else:
            print("student does not exist in the database\n***********Please Try Again************\n ")
    main()

def display_student(ID):
    if ID==0:
        cmd="select * from student_details"
        c=con.cursor()
        c.execute(cmd)
        for i in c:
            print("student ID: ",i[0])
            print("student Name: ",i[1])
            print("student Age: ",i[2])
            print("student Gender: ",i[3])
            print("student Class: ",i[4])
            print("\n")

    else:
        if check_student(ID)==True:
            cmd=f"select * from student_details where ID={ID}"
            c=con.cursor()
            c.execute(cmd)
            for i in c:
                print("student ID: ",i[0])
                print("student Name: ",i[1])
                print("student Age: ",i[2])
                print("student Gender: ",i[3])
                print("student Class: ",i[4])
                print("\n")
        else:
            print("student does not exist, please enter valid ID")
    main()

def main():
    print("Welcome to student Management Record")
    print("press")
    print("1 to add student")
    print("2 to remove student")
    print("3 to display details")
    print("4 to update details")
    n=int(input("Enter your choice"))
    if n==1:
        ID=input("Enter student ID")
        Name=input("Enter student Name")
        Age=int(input("Enter student Age"))
        Gender=input("Enter student Gender")
        Class=input("Enter student class")
        add_student(ID,Name,Age,Gender,Class)
    elif n==2:
        k=input("Enter student ID or Name")
        remove_student(k)
    elif n==3:
        print("press 0 to display all details or Enter student ID")
        ID=int(input("Enter your choice"))
        display_student(ID)
    elif n==4:
        # print("Enter student  to update")
        ID=int(input("Enter student-ID to update the details"))
        if check_student(ID)==False:
            print("student with this ID Does not exist****\n PLEASE ENTER VALID ID")
            main()
        else:
            Name=input("Enter Name")
            Age=int(input("Enter Age"))
            Gender=input("Enter Gender")
            Class=int(input("Enter Class"))
            update_student_details(ID,Name,Age,Gender,Class)
    else:
        print("Invalid choice")
        main()


main()






        

