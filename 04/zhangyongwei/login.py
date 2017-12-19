#!/usr/bin/env python
#coding:utf8

def userinfo(user,pwd,login=False):
    with open('user.txt','a+') as userinfo:
        lines = userinfo.readlines()
        count = 0
        if login:
            for line in lines:
                    count += 1
                    username = line.split(':')[0]
                    password = line.split(':')[1].strip()
                    if user == username and pwd == password:
                        print '登录成功!'
                        return '登录成功!'
                    if count == len(lines):
                        print '登录失败,用户名或密码不正确!'
                        return '登录失败,用户名或密码不正确!'
        else:
            if len(lines) == 0:
                    userinfo.write('{user}:{pwd}\n'.format(user=user,pwd=pwd))
                    print '用户添加成功'
                    return '用户添加成功'
            for line in lines:
                count += 1
                if user == line.split(':')[0]:
                    print '用户名已存在'
                    return '用户名已存在'
                if count == len(lines):
                    userinfo.write('{user}:{pwd}\n'.format(user=user,pwd=pwd))
                    print '用户添加成功'
                    return '用户添加成功'

def regesit():
    username = raw_input('请输入用户名:')
    if username.strip() is '':
        print '用户名不能为空'
    else:
        password = raw_input('请输入密码:')
        passwordA = raw_input('请再次输入密码')
        if password.strip() == passwordA.strip() and password != '':
            userinfo(username,password)
        else:
            print '两次密码输入不一致'
            return regesit()

def login():
    username = raw_input('请输入用户名:')
    password = raw_input('请输入密码:')
    if username.strip()== '' or password.strip() == '':
        print '用户名或密码不能为空'
        return '用户名或密码不能为空'
    else:
        userinfo(username,password,login=True)

if __name__ == '__main__':
    # regesit()
    login()