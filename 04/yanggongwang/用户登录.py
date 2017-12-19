#encoding=utf-8

import  hashlib

# 作者：杨公旺
# 日期：2017-12-18
# 功能：用户登录

# 思路：
#   1、接收用户输入的账号、密码等信息
#   2、判断账号是否存在，如果不存在即返回错误
#   3、对密码信息进行加密后比对，如果一致，则登录成功。因密码是不可逆加密，所以比对加密后的密文内容


# 判断用户名是否存在的函数
# 需要传入两个参数：文件名和账号名
# 将每行的第一个元素（用户名）取出来，放到一个list中，判断用户输入的账号是否在这个list中
def is_user_password(filename,user_name):
    with open(filename,'r') as f:
        user_list = []
        for line in f.readlines():
            temp_strings = line.strip().split(':')[0]
            user_list.append(temp_strings)
        if user_name in user_list:
            return line.strip().split(':')[2]
        else:
            return 1

# 取用户密码和salt的函数
# 需要传入两个参数：文件名和用户名
def get_password(filename,user_name):
    with open(filename,'r') as f:
        for line in f.readlines():
            temp_strings = line.strip().split(':')[0]
            if temp_strings == user_name:
                return (line.strip().split(':')[1],line.strip().split(':')[2])

# 用户名登录的输入函数
def input_user_name_passwd():
    input_user_name = raw_input("请输入用户名，仅输入单个小写字母q则结束程序：")
    if input_user_name == 'q' or input_user_name == '':
        print "您输入了退出字符q或者未输入任何字符，程序终止！"
        exit()
    input_user_password = raw_input("请输入密码，仅输入单个小写字母q则结束程序：")
    if input_user_password == 'q' or input_user_password == '':
        print "您输入了退出字符q或者未输入任何字符，程序终止！"
        exit()
    return (input_user_name,input_user_password)

# 加密函数
def jiami_password(user_password,salt):
    return hashlib.sha512(user_password + salt).hexdigest()




#####################  以上是函数定义，以下是函数调用  #####################

filename = 'user.txt'

# 调用用户输入函数，并获得用户输入的账号和密码
user_name_password = input_user_name_passwd()
user_name = user_name_password[0]
user_password = user_name_password[1]

# 判断用户输入的账号是否存在
if is_user_password(filename,user_name) == 1:
    print "您输入的用户名或密码错误，请核对后重新登录！"
    exit()

# 取出用户名对应的salt字符串，对用户输入的密码进行加密
salt = get_password(filename,user_name)[1]
pwd = get_password(filename,user_name)[0]
tmp_pwd = jiami_password(user_password,salt)

# 比对用户输入密码的密文与文件中存储的密文是否相同
if pwd == tmp_pwd:
    print "登录成功！"
else:
    print "您输入的用户名或密码错误，请核对后重新登录！"
    exit()













