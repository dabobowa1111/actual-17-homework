# -*- coding:utf-8 -*- 
__author__ = 'ABigLazyCat'
#print 'Test:注册和登录'
#文件储存数据参考：Refence = {name:{'age':25,'job':'DI','password':'168168'}}
#以str(dict)方式把字典转换成字符串写入文件，将文件读取后通过eval(str)把字符串转换成字典进行使用。
#也可选用pickle模块或者json模块里的dumps和loads的方法。dumps是将dict转化成str格式，loads是将str转化成dict格式。
#dump和load功能类似，结合了文件操作。pickle.dump(对象，文件，True):格式转换并写入到文件中。pickle.load(对象，文件，True):读取文件并格式转换。
#选cPickle,因为看起来更加简单暴力。
#文件User_File.txt中已写入了{'sudo':{'password':123456}}数据作为最初始状态。(主要是避免报错。)




import cPickle as pickle






#注册功能
def sign_up():
	with open('User_Info_File.pkl','r+') as user_info:
		new_info = pickle.load(user_info)
	name = raw_input('Please input the name: ')	
	if len(name) == 0:
		print 'Error, please input again.'
	elif name in new_info: 
		print 'The user is exsit.Please input again.'
	else:
		print 'Enter your security password.(The one you enter twice.)'
		password_01 = raw_input('Your password: ')
		password_02 = raw_input('Plaese again:')
		if password_01 != password_02:
			print 'The password entered did not match.'
			print 'Please try again.'
		else:
			password = password_01
		print 'Please input your personal informations.'
		age = raw_input('Your age: ')
		job = raw_input('Your job: ')
		new_info.setdefault(name,{})
		new_info[name].setdefault('age',age)
		new_info[name].setdefault('job',job)
		new_info[name].setdefault('password',password)
		with open('User_Info_File.pkl','w') as user_info:
			pickle.dump(new_info, user_info)
	print 'Congratulation,create your account successfully.'



def log_in():
	with open('User_Info_File.pkl','r') as user_file:
		user_info = pickle.load(user_file)
	name = raw_input('Please input the name: ')
	if len(name) == 0:
		print 'Error, please input again.'
	elif name not in user_info:
		print 'The user is not exsit, please sign up first.'
	else:
		print 'Please enter your password: '
		password = raw_input('Your password: ')
		if password == user_info[name]['password']:
			print 'Log in successfully.Enjoy your time.'
		else:
			print 'The password is not correct.Please try again.'
	#if name == 'sudo':
		#action = raw_input('Continue or Modify: ')
		#if action == 'Continue':
		#	print_list()
		#elif action == 'Modify':
		#	modify_info()





#def modufy_info():




#def print_list():
	

	

#	print 'Nice to see you again,enjoy yourself.'


#初始化
try:
	f = open('User_Info_File.pkl','r')
	f.read()
	f.close()
except:
	print 'Erro!'
	f = open('User_Info_File.pkl','w')
	Initial_Info = {'sudo':{'password':123456}}
	pickle.dump({'sudo':{'password':123456}},f)
	f.close()
finally:
	print 'Welcome to join us.'


#功能选择
function = raw_input('sign_up or log_in:')
if function == 'sign_up':
	sign_up()
elif function == 'log_in':
	log_in()



