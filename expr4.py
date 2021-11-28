#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql


def print_menu():
    print('''
    ************************************* Menu *************************************
    1. Insert New Student Info                  2. Modify Existing Student Info
    3. Insert New Course Info                   4. Modify Existing Course Info
    5. Delete Existing Course Info              6. Record Student Grade
    7. Modify Student Grade                     8. Print Analytical Info by Dept
    9. Print Grade Rank by Dept                 10. Print Student Info
                                        
                                        0. Exit
    ********************************************************************************
    ''')
    return


def insert_student(db):
    print("================== Mode 1: Insert New Student Info ==================")
    print("Please input the following information! ")

    sno = input("Student ID: ")
    sname = input("Name: ")
    sex = input("Gender: ")
    age = input("Age: ")
    dept = input("Student's Department: ")
    scholarship = "是" if input("Have Scholarship? (y/n)") == 'y' else "否"

    print("Re-check the student's information below: ")
    print(f'''
    Student ID: {sno}, \tName: {sname},
    Gender: {sex}, \tAge: {age},
    Department: {dept}, \tHave Scholarship: {scholarship}.
    ''')

    op = input("ARE YOU SURE TO INSERT THE NEW INFORMATION? (y/n)")
    if op == 'n':
        print("rollback successfully! ")
        return
    else:
        pass

    cursor = db.cursor()

    sql = f"INSERT INTO Student" \
          f"VALUES({sno},{sname},{sex},{age},{dept},{scholarship})"

    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("An unexpected error occurred and we rollback all the changes. ")
        db.rollback()



def main():
    ip_addr = input("Input the IP Address (default: localhost): ") or "localhost"
    usr = input("Username (default: yuanye): ") or "yuanye"
    passwd = input("Password (default: yuanye): ") or "yuanye"
    select_db = input("Select one database to operate (default: S_T_U201911808): ") or "S_T_U201911808"

    print(" ... Connecting to the Database ... ")

    db = pymysql.connect(
        host=ip_addr,
        user=usr,
        password=passwd,
        database=select_db
    )

    cursor = db.cursor()

    cursor.execute("SELECT VERSION()")

    db_version = cursor.fetchone()

    print("---------------- Student Management System ----------------")
    print("         Author： 网安1902班   袁也   U201911808")
    print("         MySQL Version: {}".format(db_version[0]))
    print("  User: {}@{}   Database: {}".format(usr, ip_addr, select_db))

    while True:
        print_menu()
        op = input("Choose what you want (0~10): ")
        if op == '0':
            break
        elif op == '1':
            insert_student(db)


    db.close()
    print("Thanks for using this database! Bye!")


if __name__ == '__main__':
    main()