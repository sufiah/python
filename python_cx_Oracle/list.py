#!user/bin/python
# -*- coding: utf8 -*-

def generate_index(n, step=1):
    for i in range(0, n, step):
        yield (i, i + step) if i + step < n else (i, None)


lst = [{'1':2, '2': 3},{'4':0},{'oder':'000000'} ]
for i, j in generate_index(len(lst)):
    print lst[i:j]

f = open(r'D:\11.txt', 'w+')
# 写数据
f.write(str(lst))
# 关闭文件
f.close()