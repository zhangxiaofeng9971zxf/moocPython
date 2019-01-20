import turtle
turtle.setup(650,350,200,200)#设置绘图窗体的大小/位置
turtle.penup()#将画笔抬起
turtle.fd(-250)#前进-250
turtle.pendown()#落笔
turtle.pensize(25)#设置笔画宽度为25
turtle.pencolor('purple')#设置笔的颜色
turtle.seth(-40)#转角度-40度
for i in range(4):
    turtle.circle(40,80)#在距离左边半径为40的地方，转80度
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()