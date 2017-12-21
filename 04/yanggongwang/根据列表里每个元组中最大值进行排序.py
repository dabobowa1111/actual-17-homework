#encoding=utf-8

# 作者：杨公旺
# 时间：2017-12-21
# 功能：对复杂list进行排序

# 需求：list中的元素全部是元祖，要求按照元组中最大值进行排序。

# 思路：
#   1、取出每个元组中的最大值，将元组与最大值作为键值对存入dict中，同时将最大值去重后存入一个临时的list中。
#   2、对临时list进行排序。此部分直接调用排序函数完成。
#   3、依次取出临时list中的每个元素，与dict中的value进行比较，如果相同，则将key取出并存入新的list中。

# 方法1：不使用sorted、lambda

def max_number_list(number_list):
    max_number_dic = {}
    temp_list = []
    new_number_list = []

    # 将number_list转换成dict类型，并统计出每个元素的最大值作为value
    # 此部分是基于每个元组中只有两个元素进行设计的，如果是多个元素的元组，需要使用循环语句找出最大值，或者直接使用max函数
    for i in number_list:
        max_number_dic.setdefault(i, max(i))
        if max(i) not in temp_list:
            temp_list.append(max(i))

    # 如果需要逆序排序，则将临时list进行逆序排序即可
    print   temp_list.sort()

    for i in temp_list:
        for k in max_number_dic:
            if max_number_dic[k] == i:
                new_number_list.append(k)
    print new_number_list

if __name__ == '__main__':
    number_list = [(1, 3, 44), (4,9, 7), (2, 5), (5,8, 7), (2, 1), (6, 2), (4, 1)]
    max_number_list(number_list)



# 方法2：使用sorted和lambda
number_list = [(1, 3, 44), (4,8, 7), (2, 5), (5,8, 7), (2, 1), (6, 2), (4, 1)]
print sorted(number_list, key=lambda x:max(x))
# 结果是：[(2, 1), (1, 3), (4, 1), (2, 5), (6, 2), (4, 7)]

number_list = [(1, 3, 44), (4,8, 7), (2, 5), (5,8, 7), (2, 1), (6, 2), (4, 1)]

# 方法3：手动实现max函数
# 此方法是在参考导师的代码后实现的。主要是由于对lambda的使用不熟悉，导致不知道求最大值的函数该怎么实现。
# 参考导师代码后，将导师的代码函数化了。
def my_max(number):
    max_number = None
    for i in range(len(number)):
        if number[i] >= max_number:
            max_number = number[i]
    return max_number

print sorted(number_list, key=lambda x:my_max(x))


# # 方法4：'剽窃'导师的答案。
# # 此方法仅适用于元组为2个元素的情况，单元素或多余2个元素时不适用。
#
# print sorted(number_list,key=lambda x: x[0] if x[0] > x[1] else x[1])