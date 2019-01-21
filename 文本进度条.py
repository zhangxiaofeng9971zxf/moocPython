import time
scale =60
print('执行开始'.center(scale//2,'='))
#.center(宽度，填充) //是整除 取整数部分
start = time.perf_counter()#记录cpu时间
for i in range(scale+1):
    a = "*"*i
    b = "."*(scale-i)
    c =(i/scale)*100
    dur = time.perf_counter()-start#记录下cpu时间，两个时间差就是程序运行时间
    print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c,a,b,dur),end='')
    #end ='' 有这个，每次打印就不换行
    time.sleep(0.1)
print('\n'+'执行结果'.center(scale//2,'='))

