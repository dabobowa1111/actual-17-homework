#!/usr/bin/env python
#-*- coding:utf-8 -*-
f = open('access.txt','r')
new_dict = {}
for line in f:
    if not line:
        break
    ip_url_status= line.split(' ')[0],line.split(' ')[6],line.split(' ')[8]
    if ip_url_status in new_dict:
        new_dict[ip_url_status] +=1
    else:
        new_dict[ip_url_status] = 1
new_list = new_dict.items()
for i in range(len(new_list)-1):
    for j in range(len(new_list)-i-1):
        if new_list[j][1] < new_list[j+1][1]:
            new_list[j],new_list[j+1] = new_list[j+1],new_list[j]

print new_list[0:11]
f.close()