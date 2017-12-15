#!/usr/bin/env python
# -*- coding: UTF-8 -*
log_list = []
log_dict = {}
count = 0
result = {}
# get
log_file = open('./access.txt')
log = log_file.readlines()
log_file.close()
# format
for i in log:
    log_list.append((i.split()[0],i.split()[6],i.split()[8]))
# count
for j in log_list:
    if j in log_dict:
        log_dict[j] += 1
    else:
        log_dict[j] = 1
# analysis
for count in range(10):
    for t in log_dict:
        k = t
        v = log_dict[t]
        break

    for r in log_dict:
        if log_dict[r] > v:
            k = r
            v = log_dict[r]

    result = {k:v}
    log_dict.pop(k)
    print result
