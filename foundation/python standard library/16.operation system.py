# _*_ coding:UTF-8 _*_


'''
#####################
python standard library 16 
#####################
'''

# 16.1 os

import os




'''

for _ in dir(os):
    #print(type(_))
    if _.startswith('__'):
        print('%s: \n %s'%(_, getattr(os,_)))

'''


'''
# 16.1 os





#os.system('cmd')
a = os.times()

print(a)


'''





'''


# 16.2 io

import io

f1 = open('text_io_test.txt','a+', encoding='utf-8')
f1.write('test1 \n aaaaaaaaaaaaaaaaa')
print(type(f1))
f1.close()


f2 =  io.StringIO('some initial text data.')

f3 = open('t.txt', 'rb')
#f3.write(b'sdfwewe')

print(type(f3))
#f3.close()

'''



# 16.6 logging



import logging



'''
#logging.basicConfig(filename='s_log.log', level = logging.DEBUG)
#logging.debug("this message should go to the log file.")


logging.basicConfig(format='%(asctime)s%(message)s',filename='s_log.log', level = logging.DEBUG)
logging.warning(' is when this event was logged')

loga = logging.getLogger('loga')
#loga.basicConfig(filename='t_log.log')
loga.setLevel(logging.INFO)

log_han_a = logging.StreamHandler()
log_han_a.setLevel(logging.INFO)
log_han_b = logging.FileHandler('t_log.log')
log_han_b.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s--%(name)s--%(levelname)s--%(message)s')

log_han_a.setFormatter(formatter)
log_han_b.setFormatter(formatter)

loga.addHandler(log_han_a)
loga.addHandler(log_han_b)

loga.debug('debug message')
loga.info('info message')
loga.error('reeor mess')
loga.critical('critical message')

'''
'''
log_s = logging.getLogger('los')
log_s.setLevel(logging.INFO)

hand_s = logging.StreamHandler()
hand_s.setLevel(logging.INFO)
hand_f = logging.FileHandler('s_info.log')
hand_f.setLevel(logging.WARNING)

formatter1 = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')

hand_s.setFormatter(formatter1)
hand_f.setFormatter(formatter1)

log_s.addHandler(hand_s)
log_s.addHandler(hand_f)

log_s.debug('this is a debug info.')
log_s.info('this is a info info.')
log_s.warning('this is a warning info.')
log_s.error('this is a error info.')

'''

















    
