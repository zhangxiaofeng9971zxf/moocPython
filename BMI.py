height = eval(input('请输入身高m:'))
weight = eval(input('请输入体重kg:'))
def BMI(weight,height):
    bmih = height*height
    bmi = weight/bmih
    if bmi <18.5:
        print('国际标准偏瘦')
    elif 18.5<bmi<25:
        print('国际标准正常')
    elif 25<bmi<30:
        print('国际标准偏胖')
    else:
        print('国际肥胖')
    print('{:.2f}'.format(bmi))
BMI(weight,height)
