#conding:utf-8
__author__ = 'sn'

class student():
    def __init__(self,name, id, grade):
        '''初始化函数'''
        self.name = name
        self.id = id
        self.grade = grade

    def __lt__(self, other):
        return (self.grade > self.grade)

    def __str__(self):
        return self.name + '\t' + str(self.id) + '\t' + str(self.grade)

    def getstudentname(self):
        return self.name

    def getstudentid(self):
        return self.id

    def getstudentgrade(self):
        return self.grade

    def setstudentgrade(self, grade):
        self.grade = grade



