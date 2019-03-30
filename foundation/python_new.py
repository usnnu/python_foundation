# _*_ coding:UTF-8 _*_

# python new


class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        print(cls, name, bases, attrs)
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


a= ProxyMetaclass


class Crawler(object, metaclass=ProxyMetaclass):
    def __init__(self):
        self.abc = 23253

    def crawl_sd_dd(self):
        pass

    def dy():
        pass
    
        


c = Crawler()
