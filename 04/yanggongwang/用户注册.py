#encoding=utf-8

import random
import  hashlib
import time

# 作者：杨公旺
# 日期：2017-12-18
# 功能：用户注册

# 思路：
#   1、接收用户输入的账号、密码等信息，写入到文件中保存。其中密码需要输入两次，且两次密码相同
#   2、不允许账号重复
#   3、密码加密存储
#   4、用户输入字母q则退出程序

# 判断用户名是否存在的函数
# 函数接收两个参数：密码存储的文件名和用户名
# 如果用户名已经存在，则返回值是1。该返回值用于判断文件名是否存在
def is_user_password(filename,user_name):
    _count = 0
    with open(filename,'r') as f:
        for line in f.readlines():
            temp_strings = line.strip().split(':')[0]
            if temp_strings == user_name:
                return 1

# 用户名、账号输入函数
# 函数不接受参数
# 正常执行时，函数返回值是用户输入的账号和密码
def input_user_name_passwd():
    input_user_name = raw_input("请输入用户名，仅输入单个小写字母q则结束程序：")
    if input_user_name == 'q' or input_user_name == '':
        print "您输入了退出字符q或者未输入任何字符，程序终止！"
        exit()
    while True:
        input_user_password1 = raw_input("请输入密码，仅输入单个小写字母q则结束程序：")
        if input_user_password1 == 'q' or input_user_password1 == '':
            print "您输入了退出字符q或者未输入任何字符，程序终止！"
            exit()
        input_user_password2 = raw_input("请再次输入密码，仅输入单个小写字母q则结束程序：")
        if input_user_password2 == 'q' or input_user_password2 == '':
            print "您输入了退出字符q或者未输入任何字符，程序终止！"
            exit()
        if input_user_password1 == input_user_password2:
            break
        else:
            print "两次输入密码不一致，请重新输入！"
    return (input_user_name,input_user_password1)

# 加盐函数
# 接收一个参数，参数有默认值
# 函数返回值是一个字符串
# 默认salt长度是6个字符，可以在函数调用时指定slat的长度
# salt的内容来自于一个长字符串，可以根据需要灵活调整该字符串。为增加字符串的随机性，字符串包含当前的时间信息。
# 每次随机从字符串中取出一个字符作为salt字符串的一部分
def create_salt(length = 6):
    my_time = time_start = time.time()
    _salt = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789' + str(my_time)
    len_chars = len(chars) - 1
    for i in xrange(length):
        # 每次从chars中随机取一位
        _salt += chars[random.randint(0, len_chars)]
    return _salt


# 加密密码函数
# 接收两个参数，无参数默认值
# 返回值是加密后的密码密文
# 被加密的字符串是用户输入的密码和加盐函数随机生成的slat
def jiami_password(user_password,salt):
    return hashlib.sha512(user_password + salt).hexdigest()


# 账号、密码写入文件函数
# 接收三个参数用户账号、密码密文、salt
def file_write(filename,pwd,salt):
    with open(filename,'aw') as f:
        f.write(user_name+':'+pwd+':'+salt+'\n')


#####################  以上是函数定义，以下是函数调用  #####################
filename = 'user.txt'

# 调用用户输入函数
user_name_password = input_user_name_passwd()

# 将用户输入函数的返回值分别提取出来：账号、密码
user_name = user_name_password[0]
user_password = user_name_password[1]

# 调用判断用户名是否存在的函数
if is_user_password(filename,user_name) == 1:
    print "用户名已经存在！"
    exit()

# 调用创建salt的函数，创建长度为9位字符的salt
salt = create_salt(9)

# 调用加密函数，将加密后的密码赋值给pwd
pwd = jiami_password(user_password,salt)

# 调用文件写入函数
# 需要传入文件名、账号和密码三个参数
file_write(filename,pwd,salt)