#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql

def main():
    ip_addr = input("Input the IP Address: ") or "localhost"
    usr = input("Username: ") or "yuanye"
    passwd = input()

    db = pymysql.connect(
        host=ip_addr,
        user=usr,
        password=passwd,
        database='S_T_U201911808'
    )

    cursor = db.cursor()

    cursor.execute("SELECT VERSION()")

    db_version = cursor.fetchone()

    print("------------------欢迎使用学生管理系统------------------")
    print("      作者信息： 网安1902班   袁也   U201911808")
    print("               MySQL Version: {}".format(db_version))




if __name__ == '__main__':
    main()