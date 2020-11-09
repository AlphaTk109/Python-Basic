#Python Optional Class 01 [2020/11/09]
#Program 08
#绘制太阳花：
from turtle import *
color ('red','yellow')
begin_fill()
while 1:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()