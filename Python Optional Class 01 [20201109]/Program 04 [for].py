#Python Optional Class 01 [2020/11/09]
#Program 04
#计算阶乘的和：
sum, tmp = 0, 1
for i in range(1,11):
    tmp*=i
    sum+=tmp
print("Result is:{}".format(sum))
print('')#换行操作
print(sum)
print(tmp)