#直接将温度值进行转换
TempStr = input('请输入带有符号的温度值，'
                '若是华氏则在数据后面加F，摄氏则加C，类似120F，C35；\n'
                '输入温度：')
if TempStr[-1] in ['F','f']:  #意思是取最后一个值出来判断
    C = (eval(TempStr[0:-1]) -32)/1.8 #eval的作用是去掉外侧的引号，执行里面的函数
    #[0:-1]的意思是去掉最后一个数值，其余的都换成数值
    print('转换后的温度为{:.2f}C'.format(C))#{:.}的意思保留小数点后的两个
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1])+32
    print('转换后的温度为{:.2f}F'.format(F))
else:
    print('输入格式错误')
