#用户输入账号密码吗错误三次就退出
#正确用户密码是kate/66666
i = 0
while i <3:
    user = input('请输入用户名：')
    pasword = input('请输入密码：')
    rigtuser ='kate'
    rigtpw  ='66666'
    if user == rigtuser and pasword == rigtpw:
        print('密码正确')
        break
    else:
        i = i +1
        if i == 3:
            print('3次错误，退出程序')