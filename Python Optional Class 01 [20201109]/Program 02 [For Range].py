#Python Optional Class 01 [2020/11/09]
#Program 02
#整数序列求和：
n = input("Please input a integer:")
sum = 0
#range:创建一个整数列表（起始点，终止点，步长） 起始点默认0
for i in range(int(n)):
    sum += i + 1
print ("The result of sum 1 to n:",sum)
