#!/usr/bin/python
# -*-coding: UTF-8 -*-
for m in range(168):
    for n in range(m):
        if (m+n)*(m-n)==168:
            x=n**2-100
            print u"符合条件的整数有:",x
            
