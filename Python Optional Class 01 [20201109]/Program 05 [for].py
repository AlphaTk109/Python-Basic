#Python Optional Class 01 [2020/11/09]
#Program 05
#猴子第一天摘了很多桃子，第一天吃一半零一个，连续4天，第五天早上剩一个，求总数：
n=1
for i in range(4,0,-1):
    n=(n+1)<<1  #疑问
    print(n)
