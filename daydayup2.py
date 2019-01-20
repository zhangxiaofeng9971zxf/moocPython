#工作日进步，休息天退步，要进步多少才能赶上每天进步1%的人一年的进度呢（37.78）
def dayUP(df):#工作日努力函数
    dayup =1.0#初始水平值
    for i in range(365):
        if i % 7 in [6, 0]:  # 365日中的休息天
            dayup = dayup*(1-0.01)  # 落后的进度
        else:
            dayup = dayup*(1 + df)
    return dayup
dayfactor = 0.01
while dayUP(dayfactor) <37.78:#37.78是每天努力1%人 一年的进步值
    dayfactor+= 0.001 #每次增加努力值0.091

print('工作日的努力参数{:.3f}'.format(dayfactor))