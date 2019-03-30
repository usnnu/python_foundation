# conding:utf-8
__author__ = 'sn'

import student
import utils


def delstudent(filepath):
    with open(filepath, 'r') as fi:
        studentlist = []
        for line in fi:
            stuinfo = line.strip().split()
            stu = student.student(stuinfo[0], int(stuinfo[1]), int(stuinfo[2]))
            studentlist.append(stu)

    if len(studentlist) == 0:
        print("no student info.")
        return

    id1 = input("input id:")
    idx = utils.searchstudentid(studentlist, int(id1))
    while idx >= len(studentlist):
        id1 = input("none of this id,input the right id:")
        idx = utils.searchstudentid(studentlist, int(id1))

    instruct = input("confirm:(y/n)")
    if instruct.lower() == "y":
        del studentlist[idx]
        with open(filepath, 'w') as fi:
            for stu in studentlist:
                fi.write(str(stu) + '\n')
        print("save succesful.")
