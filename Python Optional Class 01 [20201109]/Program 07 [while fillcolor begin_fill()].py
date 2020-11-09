#Python Optional Class 01 [2020/11/09]
#Program 07
#绘制5角星：
from turtle import * #turtle 绘图库
fillcolor ("red")    #颜色调整
begin_fill()
while True:
    forward(200)
    right(144)
    if abs(pos())<1:
        break
end_fill()

