#coding=utf-8

# 作者：杨公旺
# 时间：2017-11-27

list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,444,111,3333,4,5,777,65535,45,5001,33,45,6000]
max1=None
max2=None

for i in range(0,len(list)):
    if list[i] >= max1:
            max2 = max1
            max1 = list[i]
    elif list[i] >= max2 :
	    max2 = list[i]

print "最大值是%s"%(max1)
print "次大值是%s"%(max2)
