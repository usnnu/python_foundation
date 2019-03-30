#coding:utf-8

import chardet



rawdata = b'sdfwe'


res = chardet.detect(rawdata)
#res = chardet.detect.feed(rawdata)

print(res)




data = '最新の主要ニュース'.encode('euc-jp')


res2 = chardet.detect(data)


print(res2)

