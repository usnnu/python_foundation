#conding:utf-8

__author__ = 'sn'
"""展示所有学生的信息"""

def iterall(filepath):
    print("开始遍历：")
    print('姓名：        编号：      成绩：')
    with open(filepath, 'r') as fi:
        for line in fi:
            stuinfo = line.strip().split()
            # print(line[0], line[1], line[2])
            print(stuinfo[0], stuinfo[1], stuinfo[2])

    input("按任意健后回车退出。。。")
