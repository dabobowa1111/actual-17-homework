#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 需求：根据列表里每个元组中最大值进行排序
test = [(1, 3), (4, 7), (2, 5), (2, 1), (6, 2), (4, 1)]

# 方法1：使用max
result1 = sorted(test, key=lambda x: max(x))
print result1

# 方法2：自定义max函数
def my_max(*args):
	# 更通用的方法
	# return sorted(args, reverse=True)[0]
	
    x, y = args
    if x >= y:
        return x
    else:
        return y

result2 = sorted(test, key=lambda x: my_max(*x))
print result2


