#Python Optional Class 01 [2020/11/09]
#Program 03
#打印99乘法表：
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={:2}".format(j,i,i*j),end=' ')
    print(' ')