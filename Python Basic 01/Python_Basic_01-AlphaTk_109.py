print("下次一定"*8)
print("===========IF ELSE==========")
temp=input("赌一把，来，输入一个数字：")
guess=int(temp)
while guess!=8:	
	temp=input("就这？再来一次：")
	guess=int(temp)
	if guess==8:
		print("耶！你是堵怪")
	else:
		if guess>8:
			print("big")
		else:
			print("small")
print("=========End========")


#输出基础：
##变量：
#teacher='小甲鱼'
#print(teacher)
#first=3
#second=8
#print(first+second)
#yourteacher='黑夜'
#ourteacher=teacher+yourteacher
#print(ourteacher)
##output:小甲鱼黑夜




