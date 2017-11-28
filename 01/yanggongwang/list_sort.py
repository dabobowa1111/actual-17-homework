#coding=utf-8

# 作者：杨公旺
# 时间：2017-11-27


list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,444,111,3333,4,5,777,65535,45,5001,33,45,6000]
for i in range(0,len(list)-1):
    for j in range(i+1,len(list)):
        if list[i] < list[j]:
            temp = list[i]
	    list[i] = list[j]
	    list[j] = temp
print list
