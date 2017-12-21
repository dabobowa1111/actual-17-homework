#!/usr/bin/env python
# -*- coding:utf8 -*-

def userdata(filename, data=None):
    '''
    data为None时，从文件中获取用户名和密码
    data不为None时，追加新的用户至文件中
    '''
    users = {}
    try:
        if data is None:
            with open(filename, 'r') as point:
                for line in point:
                    username, password = line.strip('\n').split(':')
                    users[username.strip('"')] = password
                return users
        else:
            with open(filename, 'a') as handle:
                handle.write(str(data) + '\n')
            return
    except IOError as err:
        open(filename, 'w+')
		return users

# print(userdata('users.txt'))


def username_is_empty(username):
    '''检查用户输入是否为空，为空则触发异常'''
    # return True if username != '' else False
    if username == '':
        raise Exception("Username: [{}] can't be empty".format(username))


def username_already_exist(username, users):
    '''检查用户名是否已注册，如果已注册就触发异常'''
    if username in users:
        raise Exception("Username: [{}] already exist".format(username))


def check_password(username, password, users):
    '''验证密码是否正确'''
    if users[username] != password:
        raise Exception("Invalid password ")

def check_password_len(password):
    '''验证密码长度'''
    if len(password) < 5:
        raise Exception("The password length is at least 5 bits")

def double_check_password(password, repeat_password):
    if password != repeat_password:
        raise Exception("Sorry, passwords do not match")

def check_login_user(username, users):
    '''验证要登陆的用户是否存在'''
    if username not in users:
        raise Exception("Invalid user")


# def check_login_in(username, record ):
#    if userame not in record:
#        raise Exception("Username: [{}] is not logged in!")

def check_choice(choice, command):
    '''验证用户输入的选项是否合法'''
    if not choice.isdigit() or choice not in command:
        raise Exception("Invalid choice")


def register():
    '''注册程序，检查用户名是否已注册，验证密码'''
    users = userdata('users.txt')
    flag = True

    while flag:
        try:
            # 用户名输入及检测
            new_user = raw_input('Enter your name：')
            username_is_empty(new_user)
            username_already_exist(new_user, users)

            # 密码输入及检测
            new_passwd = raw_input('New password: ')
            check_password_len(new_passwd)
            tmp_passwd = raw_input('Retype new password: ')
            double_check_password(new_passwd, tmp_passwd)

            # 用户数据写入
            data = '"{0}":{1}'.format(new_user, new_passwd)
            userdata('users.txt', data)
            print("You have been registered")

            # 结束循环
            flag = False
        except Exception as err:
            print(err)


def login():
    '''登陆函数，检测用户名和密码是否正确，对已登陆用户进行标记'''
    login_in = {}
    users = userdata('users.txt')

    try:
        login_user = raw_input("Who are you? ")
        login_passwd = raw_input("Password: ")
        check_login_user(login_user, users)
        check_password(login_user, login_passwd, users)
    except Exception as err:
        print('Username or password is invalid!')

    else:
        print("Welcom back!")
        login_in[login_user] = 1

def quit():
    print("Bye!")
    # return居然退不出来，用sys.exit()把调试窗口都关了
    # return
    raise SystemExit()


def print_menu():
    print(
        '''
Choice a number:
        [1]: Login
        [2]: Register
        [3]: Quit
        ''')


def main():
    login_in = {}

    menu_map = {
        '1': login,
        '2': register,
        '3': quit
    }

    while True:
        print_menu()
        choice = raw_input("What your choice[1-3]: ")
        try:
            check_choice(choice, ['1', '2', '3'])
            func = menu_map[choice]
        except Exception as err:
            print(err)
        else:
            func()

if __name__ == '__main__':
    main()

