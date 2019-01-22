#求从小到大顺序输出所有的水仙花数，用逗号隔开
#水仙花数abc的定义：a的3次方+b的3次方+c的3次方 = abc
for wf in range(100,1000):#水仙花数取值范围在（100,1000）之中
    wfstr = str(wf)
    sumwf = pow(eval(wfstr[0]),3)+pow(eval(wfstr[1]),3)+pow(eval(wfstr[2]),3)
    if wf == sumwf:
        waterflower = str(wf)
        answer = '{},'.format(waterflower)
        print(answer)


