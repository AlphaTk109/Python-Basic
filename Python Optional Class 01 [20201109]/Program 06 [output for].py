#Python Optional Class 01 [2020/11/09]
#Program 06
#健康食谱输出：
diet =['西红柿','花椰菜','黄瓜','牛排','虾仁']
for x in range(0,5):
    for y in range(0,5):
        if not(x==y):
            print("{}{}".format(diet[x],diet[y]))
