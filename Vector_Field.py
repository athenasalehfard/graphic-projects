from vpython import *
import math

# 🎨 صحنه و نور
scene.background = vector(1,1,1)
scene.width, scene.height = 900,600
scene.forward = vector(0,-1,-0.4); scene.up = vector(0,0,1)
local_light(pos=vector(4,4,6), color=color.white)

# 🔵 کره متحرک
ball = sphere(radius=0.4, color=color.cyan, make_trail=True)

# 🔻 فلش‌های اطراف روی دایره
arrows = [arrow(pos=vector(3.2*math.cos(2*math.pi*i/48),
                          3.2*math.sin(2*math.pi*i/48),0),
               axis=vector(0,0,0), shaftwidth=0.05) for i in range(48)]

# فلش‌های ریاضی کنار کره
tangent = arrow(color=color.red, shaftwidth=0.04)   # بردار مماس (سرعت)
normal  = arrow(color=color.blue, shaftwidth=0.04)  # بردار نرمال سطح
binormal= arrow(color=color.green, shaftwidth=0.04) # بردار عمود (cross product)

t=0; ang=0
while True:
    rate(60)
    # مسیر پارامتریک کره
    x,y,z = 1.8*math.cos(t), 1.8*math.sin(t), 0.6*math.sin(2*t)
    ball.pos = vector(x,y,z)

    # مشتق جزئی (قاعده زنجیره‌ای) → سرعت (مماس)
    dx,dy,dz = -1.8*math.sin(t), 1.8*math.cos(t), 1.2*math.cos(2*t)
    velocity = vector(dx,dy,dz).norm()

    # گرادیان تابع ضمنی کره F(x,y,z)=x²+y²+z²-r² → نرمال سطح
    grad = vector(2*x,2*y,2*z).norm()

    # ضرب خارجی → بردار عمود (Binormal)
    binorm = cross(velocity, grad).norm()

    # نمایش فلش‌ها
    tangent.pos=ball.pos; tangent.axis=velocity*1.5
    normal.pos=ball.pos;  normal.axis=grad*1.5
    binormal.pos=ball.pos;binormal.axis=binorm*1.5

    # فلش‌های اطراف به سمت کره + رنگ گرادیانی
    for k,a in enumerate(arrows):
        dir = ball.pos - a.pos
        a.axis = dir.norm()*1.5
        d = dir.mag
        a.color = vector(0.5+0.5*math.sin(t+d),
                         0.4+0.4*math.cos(t+0.2*k),
                         0.6+0.3*math.sin(d+t))

    # حرکت نرم دوربین (نامحسوس)
    ang += 0.0015
    scene.forward = rotate(vector(0,-1,-0.4), angle=ang, axis=vector(0,1,0))
    t += 0.03