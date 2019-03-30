#conding:utf-8
__author__ = 'sn'

import student


def searchstudentid(studentlist, id):
    idx = 0
    for stu in studentlist:
        if stu.getstudentid() == id:
            return idx
        else:
            idx += 1
    return idx

def fileread(filepath):
    with open(filepath, 'r') as fi:
        studentlist = []
        for line in fi:
            stuinfo = line.strip().split()
            stu = student.student(stuinfo[0], int(stuinfo[1]), int(stuinfo[2]))
            studentlist.append(stu)
    return studentlist

def filewrite(filepath,studentlist):
    with open(filepath,'w') as fi:
        for stu in studentlist:
            fi.write(str(stu) + '\n')

def checkid(id):
    if len(id) == 4 and id.isdigit():
        return True
    else:
        return False

def checkgrade(grade):
    if grade.isdigit() and int(grade) > 0 and int(grade) < 101:
        return True
    else:
        return False






