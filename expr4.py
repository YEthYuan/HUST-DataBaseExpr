#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import pandas as pd
from tabulate import tabulate


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
    cursor = db.cursor()
    dic_student = {'sno': [], 'sname': [], 'sex': [], 'age': [], 'dept': [], 'scholarship': []}
    print("================== Mode 1: Insert New Student Info ==================")
    print("Please input the following information! ")

    dic_student['sno'].append(input("Student ID: "))
    dic_student['sname'].append(input("Name: "))
    dic_student['sex'].append(input("Gender: "))
    dic_student['age'].append(input("Age: "))
    dic_student['dept'].append(input("Student's Department: "))
    dic_student['scholarship'].append("是" if input("Have Scholarship? (y/n)") == 'y' else "否")

    df = pd.DataFrame(dic_student)

    print("Re-check the student's information below: ")
    print(tabulate(df, headers='keys', tablefmt='psql'))

    op = input("ARE YOU SURE TO INSERT THE NEW INFORMATION? (y/n)")
    if op == 'n':
        print("rollback successfully! ")
        return
    else:
        pass

    sql = "INSERT INTO Student " \
          "VALUES('%s', '%s', '%s', %s, '%s', '%s')" % (
              dic_student['sno'][0], dic_student['sname'][0], dic_student['sex'][0], dic_student['age'][0],
              dic_student['dept'][0],
              dic_student['scholarship'][0])

    try:
        cursor.execute(sql)
        db.commit()
        print("Successfully Inserted! ")
    except:
        print("An unexpected error occurred and we rollback all the changes. ")
        db.rollback()

    return


def update_student(db):
    cursor = db.cursor()
    dic_student = {'sno': [], 'sname': [], 'sex': [], 'age': [], 'dept': [], 'scholarship': []}
    print("================== Mode 2: Modify Existing Student Info ==================")
    print("Please input the Student ID to search the student! ")

    dic_student['sno'].append(input("Student ID: "))

    sql = "SELECT * FROM Student WHERE Sno = '%s'" % dic_student['sno'][0]

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for index, row in enumerate(results):
            # dic_student['sno'].append(row[0])
            dic_student['sname'].append(row[1])
            dic_student['sex'].append(row[2])
            dic_student['age'].append(row[3])
            dic_student['dept'].append(row[4])
            dic_student['scholarship'].append(row[5])

        print("Student founded! Here is the information of this person: ")
        df = pd.DataFrame(dic_student)
        print(tabulate(df, headers='keys', tablefmt='psql'))
    except:
        print("Error: unable to fetch data")
        return

    header_list = ['', 'Sno', 'Sname', 'Ssex', 'Sage', 'Sdept', 'Scholarship']

    while True:
        modify_op = input("Select column 1~6 to modify, select 0 to exit: ")
        if modify_op == '0':
            break
        else:
            pass
        new_data = input("Input the new data: ")

        sql = "UPDATE Student SET %s = " % header_list[int(modify_op)]
        if modify_op != 4:
            sql += "'"
        sql += new_data
        if modify_op != 4:
            sql += "'"
        sql += "WHERE Sno = '%s'" % dic_student['sno'][0]

        try:
            print("Successfully Updated! ")
            cursor.execute(sql)
            db.commit()
        except:
            print("update error! ")
            db.rollback()
            return

    return


def insert_course(db):
    cursor = db.cursor()
    dic_course = {'cno': [], 'cname': [], 'cpno': [], 'ccredit': []}
    print("================== Mode 3: Insert New Course Info ==================")
    print("Please input the following information! ")

    dic_course['cno'].append(input("Course ID: "))
    dic_course['cname'].append(input("Course Name: "))
    dic_course['cpno'].append(input("Previous Course ID: "))
    dic_course['ccredit'].append(input("Credits: "))

    df = pd.DataFrame(dic_course)

    print("Re-check the course's information below: ")
    print(tabulate(df, headers='keys', tablefmt='psql'))

    op = input("ARE YOU SURE TO INSERT THE NEW INFORMATION? (y/n)")
    if op == 'n':
        print("rollback successfully! ")
        return
    else:
        pass

    sql = "INSERT INTO Course " \
          "VALUES('%s', '%s', '%s', %s)" % (
              dic_course['cno'][0], dic_course['cname'][0], dic_course['cpno'][0], dic_course['ccredit'][0])

    try:
        cursor.execute(sql)
        db.commit()
        print("Successfully Inserted! ")
    except:
        print("An unexpected error occurred and we rollback all the changes. ")
        db.rollback()

    return


def modify_course(db):
    cursor = db.cursor()
    dic_course = {'cno': [], 'cname': [], 'cpno': [], 'ccredit': []}
    print("================== Mode 4: Modify Existing Course Info ==================")
    print("Please input the Course ID to search the course! ")

    dic_course['cno'].append(input("Course ID: "))

    sql = "SELECT * FROM Course WHERE Cno = '%s'" % dic_course['cno'][0]

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for index, row in enumerate(results):
            # dic_course['cno'].append(row[0])
            dic_course['cname'].append(row[1])
            dic_course['cpno'].append(row[2])
            dic_course['ccredit'].append(row[3])

        print("Course founded! Here is the information of this course: ")
        df = pd.DataFrame(dic_course)
        print(tabulate(df, headers='keys', tablefmt='psql'))
    except:
        print("Error: unable to fetch data")
        return

    header_list = ['', 'Cno', 'Cname', 'Cpno', 'Ccredit']

    while True:
        modify_op = input("Select column 1~4 to modify, select 0 to exit: ")
        if modify_op == '0':
            break
        else:
            pass
        new_data = input("Input the new data: ")

        sql = "UPDATE Course SET %s = " % header_list[int(modify_op)]
        if modify_op != 4:
            sql += "'"
        sql += new_data
        if modify_op != 4:
            sql += "'"
        sql += "WHERE Cno = '%s'" % dic_course['cno'][0]

        try:
            print("Successfully Updated! ")
            cursor.execute(sql)
            db.commit()
        except:
            print("update error! ")
            db.rollback()
            return

    return


def delete_course(db):
    cursor = db.cursor()
    dic_course = {'cno': [], 'cname': [], 'cpno': [], 'ccredit': []}
    print("================== Mode 5: Delete Existing Course Info ==================")
    print("Please input the Course ID to search the course! ")

    dic_course['cno'].append(input("Course ID: "))

    sql = "SELECT * FROM Course WHERE Cno = '%s'" % dic_course['cno'][0]

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for index, row in enumerate(results):
            # dic_course['cno'].append(row[0])
            dic_course['cname'].append(row[1])
            dic_course['cpno'].append(row[2])
            dic_course['ccredit'].append(row[3])

        print("Course founded! Here is the information of this course: ")
        df = pd.DataFrame(dic_course)
        print(tabulate(df, headers='keys', tablefmt='psql'))
    except:
        print("Error: unable to fetch data")
        return

    header_list = ['', 'Cno', 'Cname', 'Cpno', 'Ccredit']

    confirm_op = input("ARE YOU SURE TO DELETE THIS COURSE? (y/n): ")
    if confirm_op == 'n':
        return
    else:
        pass

    sql = "DELETE FROM Course WHERE Cno = '%s'" % dic_course['cno'][0]

    try:
        print("Successfully Deleted! ")
        cursor.execute(sql)
        db.commit()
    except:
        print("delete error! ")
        db.rollback()
        return

    return


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
        elif op == '2':
            update_student(db)
        elif op == '3':
            insert_course(db)
        elif op == '4':
            modify_course(db)
        elif op == '5':
            delete_course(db)

    db.close()
    print("Thanks for using this database! Bye!")


if __name__ == '__main__':
    main()
