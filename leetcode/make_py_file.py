# coding:utf-8

__author__ = "sn"

"""


"""

"""


"""

from os.path import exists

file_str = '''# coding:utf-8

__author__ = "sn"

"""


"""

"""


"""



    '''

    
def make_file(start=0, end=0):
    start = start if start else 0
    end = end if end else 1000
    # file_path = os.path.
    for x in range(200,500):
        #print(str(x).zfill(3) + '_')
        file_name = str(x).zfill(3) + '_.py'
        if not exists(file_name):
            with open(file_name, 'w', encoding='utf-8') as fi:
                fi.write(file_str)
        else:
            print(2222)


# make_file()
def path_test():
    import os
    res = os.path.dirname(os.path.abspath('.'))
    print(res)

#path_test()

if __name__ == "__main__":
    make_file()
    pass
