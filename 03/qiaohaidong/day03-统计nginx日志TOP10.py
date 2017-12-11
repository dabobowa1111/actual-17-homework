#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 需求：取nginx的字段ip, url, status并统计这三个字段出现的top10
# 思路：
# 1 读取文件，将每行文件切割取字段
# 2 将字段封装成元组，用字典统计出现次数
# 3 将字典转换成列表进行排序
# 4 尽量不要把列表数据放到内存中

count = {}

with open('access.txt', 'r') as f:
    for line in f:
        tmp = line.split(' ')
        ip = tmp[0]
        url = tmp[6]
        status = tmp[8]
        key = (ip, url, status)
        count[key] = count.get(key,0) + 1



tmp_list = sorted(count.iteritems(), key=lambda x:x[1], reverse=True)

for i in range(10):
    print tmp_list[i]