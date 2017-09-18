# -*- coding: utf-8 -*-
# @Author: bandishui_home
# @Date:   2017-09-17 22:04:41
# @Last Modified by:   Administrator
# @Last Modified time: 2017-09-18 10:57:04



import random
import sys

def strEncode(str):
    '''
    文字转码到控制台输出的格式
    '''
    type = sys.getfilesystemencoding()
    return str.decode('utf-8').encode(type);

def fun1():
    '''
    从N个数字中随机选出M个数字
    '''
    while True:
        try:
            n = int( raw_input( strEncode('从多少数字中挑选？(大于等于0) n=') ) );
            m = int( raw_input( strEncode('挑选出多少个数字？(大于等于0,小于等于n) m=') ) );
        except:
            print strEncode('请输入数字!');
            print '';
        if( n>=0 and m<=n ):
            break;
        else:
            print strEncode('n大于等于0, 并且 m小于等于n! ');

    res = set();
    while( len(res)<m ):
        res.add(random.randint(1,n));

    print sorted(list(res));


def fun2():
	'''
	去除重复的数据，并排序
	'''
	lst = [4, 7, 3, 4, 1, 9, 8, 3, 7];
	res = set(lst)
	lst = list(res)
	print sorted(lst)

def fun3():
	'''
	找到数字， 重组成字符串
	'''
	text = "aAsmr3idd4bgs7Dlsf9eAF";
	lst = [];
	for c in text:
		try:
			int(c);
		except:
			continue;
		lst.append(c);
	print ''.join(lst);

if __name__=="__main__":
    fun3();
