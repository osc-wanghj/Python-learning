"""
turtle库:
https://blog.csdn.net/zhouheng2018/article/details/79809374
https://blog.csdn.net/weixin_40575956/article/details/80148458
海龟，也叫海龟库，诞生于1969年，是python语言的标准库之一，是入门级的图形绘制函数库。

Version：0.1
Author: osc-wanghj
Date: 2019年09月30日

"""
import turtle

# 1.1 画笔的属性
# 画笔的尺寸 width()、pensize()均可
# turtle.width(10)
turtle.pensize(2)

# 1.2 画笔运动
# 抬起画笔，海龟飞行，不绘制痕迹。 没有参数
turtle.penup()
# 落下画笔，海龟爬行。 没有参数
turtle.pendown()
# 停止画笔绘制，但绘图窗体不关闭。 没有参数
# turtle.done()

# 2 turtle绘图窗体布局
# turtle的一个画布空间，最小单位是像素。
# setup(width, height, start-x, start-y) 设置窗体大小及位置，不是必须的。
# width画布宽、height画布高、start-x画布左边框距电脑显示器左边框距离、start-y画布上边框距电脑显示器上边框距离
# start-x、start-y两个参数可选，不写默认在电脑显示器中间
# turtle.setup(1000, 1000)
# https://blog.csdn.net/zhouheng2018/article/details/79809374 看图示
turtle.setup(800, 800, 100, 10)

# 3 turtle空间坐标体系
# 3.1 绝对坐标
# 使用turtle库中goto(x, y)方法，画出从当前位置到坐标点(x, y)的直线。
# 初始化开始时海龟在画布空间的中心。
# https://blog.csdn.net/zhouheng2018/article/details/79809374 看图示
# 3.2 海龟坐标
# https://blog.csdn.net/zhouheng2018/article/details/79809374 看图示
# 3.2.1 海龟坐标方法
# 前进forward：turtle.fd(d)
# 后退back：turtle.bk(d)
# 画圆周：turtle.circle(r, angle)
# r的绝对值其实就是圆半径长度；angle的绝对值其实就是起始点到圆心连线、结束点到圆心连线的夹角
#     r > 0 圆心在海龟的左侧r处；
#     r < 0 圆心在海龟的右侧r处；
#     angle > 0 海龟向前爬，转angle度；
#     angle < 0 海龟向后爬，转angle度；
# https://blog.csdn.net/zhouheng2018/article/details/79809374 看图示

# 4 turtle角度坐标体系
# 4.1 绝对角度
# 使用turtle.seth(angle) 来改变海龟行进的方向
#    angle为绝对度数
#    seth()只改变方向但不行进
# https://blog.csdn.net/zhouheng2018/article/details/79809374 看图示
turtle.seth(90)
# 4.2 海龟角度
# https://blog.csdn.net/zhouheng2018/article/details/79809374 看图示
# turtle.left(angle)、turtle.right(angle)

# 5 RGB色彩体系
# RGB指红蓝绿三个通道的颜色组合
# RGB每色取值范围0-255整数或0-1小数（默认采用小数值）
# 设置画笔颜色的方法turtle.colormode(mode)，可以是字符串如“green”，也可以是RGB3元组。
# 如下所示设置画笔为蓝色
turtle.pencolor('blue')

# turtle.setup(800, 800)
# 画横坐标
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.speed(1)
turtle.goto(300, 0)
turtle.speed()
turtle.penup()
turtle.ht()

# 横坐标箭头
turtle.pendown()
turtle.goto(296, 3)
turtle.penup()
turtle.goto(300, 0)
turtle.pendown()
turtle.goto(296, -3)
turtle.penup()
turtle.ht()

# 画纵坐标
turtle.goto(0, -300)
turtle.pendown()
turtle.speed(1)
turtle.goto(0, 300)
turtle.speed()
turtle.penup()
turtle.ht()

# 画纵坐标箭头
turtle.pendown()
turtle.goto(3, 296)
turtle.penup()
turtle.goto(0, 300)
turtle.pendown()
turtle.goto(-3, 296)
turtle.penup()
turtle.ht()

# 画二限象圆
turtle.pensize(1)
turtle.goto(0, 0)
turtle.goto(100, 0)
turtle.left(90)
turtle.pendown()
turtle.circle(50, 180)

# 画四限象圆
turtle.circle(-50, 180)

# 隐藏画笔
turtle.ht()

# 显示绘画窗口
turtle.mainloop()

