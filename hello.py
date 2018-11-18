#! python3
#这个程序用来向用户问好并登记用户的名字

print('尊敬的用户，您好！')
print('请输入您的姓名或昵称：') #询问用户姓名或昵称
user_name = input()
print('欢迎您加入本社区'+user_name)
print('请输入您的年龄：')
user_age = input()
print('您快要'+str(int(user_age)+1)+'呢了')
