#conding:utf-8
'''主程序：
内容：选项，交互；'''
__author__ = "sn"

import os
import addstudent
import deletestudent
import changestudent
import iterallstudent

filepath = 'e:\student.txt'
def main():
    if not os.path.isfile(filepath):
        open(filepath,'a').close()

    while True:
        print("-" * 30)
        print("     学生管理系统  v1.0")
        print(" 1.添加学生的信息")
        print(" 2.删除学生的信息")
        print(" 3.修改学生的信息")
        print(" 4.查询学生的信息")
        print(" 5.所有学生的信息")
        print(" 0.退出系统")
        print('-' * 30)
        instruction = input('请输入选项：')
        if instruction == "0":
            exit(0)
        elif instruction == "1":
            addstudent.addstudent(filepath)
            print(os.getcwd())
        elif instruction == "2":
            deletestudent.delstudent(filepath)
        elif instruction == "3":
            changestudent.changestudent(filepath)

        elif instruction == "4":
            pass
        elif instruction == "5":
            iterallstudent.iterall(filepath)
        else:
            print('输入错误，请输入正确选项！')




if __name__ == '__main__':
    main()