#encoding=utf-8
import sys
#user.txt为用户密码存储文件
######################################
########   说明   ####################
#       1,存储格式为  username:password
#       2,每个用户密码之间用换行符分割
#       3,三次错误输入，则退出系统
#       4，登录成功，则退出系统

#
#定义登录函数
def Login():
    #调取外部变量，获取调用次数，超过三次则退出
    global n
    n+=1
    if n <=3:
        username = raw_input('用户名：')
        if username:
            if username in user_dict:
                password = raw_input('密码：')
                if password==user_dict[username]:
                    print '登录成功'
                    sys.exit()
                else:
                    if n == 3:
                        print '您已失败三次，系统退出'
                        sys.exit()
                    else:
                        print '密码错误，请重新登录'
                        return Login()
            else:
                if n == 3:
                    print '您已失败三次，系统退出'
                    sys.exit()
                else:
                    print '用户不存在,请重新输入'
                    return Login()
        else:
            if n == 3:
                print '您已失败三次，系统退出'
            else:
                print '失败，请输入用户名.'
                return Login()
    sys.exit()

#定义注册用户函数
def Register():
    global n
    n+=1
    if n <=3:
        username = raw_input('输入注册用户名：')
        if username.strip():
            if username in user_dict:
                if n == 3:
                    print '您已失败三次，系统退出'
                    sys.exit()
                else:
                    print "抱歉，用户已存在，请重新注册"
                    return Register()
            else:
                password = raw_input('输入密码：')
                user_dict[username]=password
                print user_dict
                with open('user.txt','w') as f:
                    for u,p in user_dict.items():
                        f.write(str(u+':'+p+'\n'))
                    f.close
                print('注册成功。')
                print('请登录：')
                return Login()
        else:
            if n == 3:
                print '您已失败三次，系统退出'
                sys.exit()
            else:
                print '输入错误，请重新输入'
                Register()
#将文件获取到字典中
def User_dict():
    user_dict={}
    user_list=[]
    with open('user.txt','r') as f:
        for user in f:
            if ":" in user:     #过滤有效行数
                user_list=user.replace('\n',"").split(':')
                user_dict[user_list[0]]=user_list[1]
            else:
                continue
        f.close()
    return user_dict

#登录/注册系统代码
print '''请选择登录或注册本系统：
1）登录
2）注册'''
for i in range(3):
    user_choice = raw_input('请输入1或2:')
    n =0
    user_dict=User_dict()
    if user_choice  == '1':
        Login()
    elif user_choice == '2':
        Register()
    else:
        if i ==2:
            print '您已失败三次，系统退出'
        else:
            print '输入错误，请输入1或2'





