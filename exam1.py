import re
from collections import Counter
urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]

a = {}
b = set()
for i in urls:
    reg = re.sub(r'http.*:\/\/.*/', '', i)
    # print(reg)
    if reg not in b:
        a[reg] = 1
        b.add(reg)
    else:
        a[reg] += 1

c = Counter(a)
for k, v in c.most_common(3):
    print('%s: %i' % (k, v))
