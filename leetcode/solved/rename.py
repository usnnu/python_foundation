# coding:utf-8

__author__ = "sn"

"""
文件改名
"""

"""


"""

import os,re

def rename_file():
    regex_str = r'(\d{3,5}_).+?(\.py)'
    patt = re.compile(regex_str)
    file_list = os.listdir()
    for _ in file_list:
        if not os.path.isfile(_):
            continue
        res = re.match(patt, _)
        if res:
            os.rename(_, ''.join(res.groups()))
            print("文件<%s>修改完毕。"%(_,))


if __name__ == '__main__':
    #_test()
    rename_file()
