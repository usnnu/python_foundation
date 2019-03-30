#conding:utf-8
__author__ = 'sn'

import utils

def addstudent(filepath):
    print("输入学生信息，其中ID为四位数字：")

    name = input("name:")
    id = input("id:")
    while not utils.checkid(id):
        id = input("input the right style:")
    grade = input("grade:")
    while not utils.checkgrade(grade):
        grade = input("input the right grade:")

    print("add succesful!")
    print("name:%s, id:%s, grade:%s" %(name, id, grade))
    instruct = input('save?(y/n):')
    if instruct == 'y':
        with open(filepath,'a') as fi:
            fi.write(name + '\t' + id + '\t' + grade + '\n')
        print("save succesful!")





