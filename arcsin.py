#import sys
#import math
from math import fabs
from math import pi
def asin(x):
    #x = input()
    #x = float(x)
    if x>=-1 and x<=1:  #判断输入数值是否在定义域内
        g = x
        t = x
        n = 1
        while (fabs(t) >= 1e-9):  #采用泰勒级数展开进行计算逼近函数值
            t = t * (2 * n - 1) * (2 * n - 1) * x * x / ((2 * n) * (2 * n + 1))
            n += 1
            g += t
        g = round(g / pi * 180, 1)
        return g
        # print(g)
    else:
        error = True  #实现异常处理，当输入超出定义域范围，返回异常error
        # print("错误")
        return error
