# _*_ coding:UTF-8 _*_


# 12 data

# 12.1 pickle



import pickle
from json import load


a = pickle.HIGHEST_PROTOCOL

print(a)

a = pickle.DEFAULT_PROTOCOL
print(a)


with open('nums.txt', 'r', encoding='utf-8') as fi:
    lisa = load(fi)

print(len(lisa))
    


file_a = 'pickle_a.txt'
with open(file_a, 'wb+') as fi:
    pass
    pickle.dump(lisa,fi)


file_a = 'pickle_a.txt'
with open(file_a, 'rb+') as fi:
    pass
    pickle.dump(lisa,fi)
































