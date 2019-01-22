#蒙特卡洛办法求PI
#随机往一个正方形撒N个点，在圆内点的个数是M，则圆的面积是正方形的（M/N）
import random
import time
DARTS = 9999999 #总的撒点数
hits = 0.0#在圆内的点数
start = time.perf_counter()#记录下当前cpu的时间
for i in range(1,DARTS+1):
    x = random.random() #点的x坐标
    y = random.random() #点的Y坐标
    dist =pow(x**2+y**2,0.5)#点距离圆心的距离等于横坐标的平方+纵坐标的平方的和 再开根号
    if dist < 1: #这个点到圆心的距离小于1的时候，点就是在圆内
       hits = hits+1
pi = 4*(hits/DARTS) #
end = time.perf_counter()
time = end -start#程序经历时间
print('pi的值为{}'.format(pi))
print('计算用时间为{:.2f}s'.format(time))