# -*- coding: utf-8 -*-
# @Author: bandishui_home
# @Date:   2017-09-17 22:04:41
# @Last Modified by:   bandishui_home
# @Last Modified time: 2017-09-17 22:19:11



import random
import sys

def fun1():
    type = sys.getfilesystemencoding()
    n = int( raw_input('从多少数字中挑选？ input:'.decode('utf-8').encode(type)) );
    m = int( raw_input('挑选出多少个数字？ input:'.decode('utf-8').encode(type)) );

    n = 1+n;
    res = set();
    while( len(res)<m ):
        res.add(random.choice(xrange(1,n)));

    print list(res);



if __name__=="__main__":
    fun1();
