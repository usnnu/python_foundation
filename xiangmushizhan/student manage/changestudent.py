#conding:utf-8
__author__ = 'sn'

import student
import utils

def changestudent(filepath):
    with open(filepath, 'r') as fi:
        studentlist = []
        for line in fi:
            stuinfo = line.strip().split()
            stu = student.student(stuinfo[0], int(stuinfo[1]), int(stuinfo[2]))
            studentlist.append(stu)

    if len(studentlist) == 0:
        print("no student info.")
        return

    id = input("input student id:")
    idx = utils.searchstudentid(studentlist, int(id))
    while idx >= len(studentlist):
        id = input("input student id:")
        idx = utils.searchstudentid(studentlist, int(id))

    grade = input("input the grade:")
    while not utils.checkgrade(grade):
        grade = input("input the right grade:")


    studentlist[idx][2] = grade
    instruct = input('save:(y/n)')
    if instruct.lower() == 'y':
        with open(filepath, 'w') as fi:
            for stu in studentlist:
                fi.write(str(stu)+ '\n')
        print("save succesful.")








