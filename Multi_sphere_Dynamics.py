from vpython import *
import math

scene.background=color.white
scene.width,scene.height=800,500
local_light(pos=vector(4,4,6),color=color.white)

# جعبه‌ی شفاف
boundary=box(pos=vector(0,0,0),size=vector(10,10,10),color=color.yellow,opacity=0.1)

# کره‌ها با سرعت اولیه
balls=[sphere(pos=vector(-3,0,0),radius=0.3,color=color.cyan,make_trail=True),
       sphere(pos=vector(2,-2,0),radius=0.3,color=color.magenta,make_trail=True),
       sphere(pos=vector(0,3,0),radius=0.3,color=color.green,make_trail=True)]
vel=[vector(0.04,0.03,0.02),vector(-0.03,0.05,0.01),vector(0.02,-0.04,0.03)]

# فلش‌های ریاضی کنار اولین کره
tangent=arrow(color=color.red,shaftwidth=0.04)
normal=arrow(color=color.blue,shaftwidth=0.04)
binormal=arrow(color=color.green,shaftwidth=0.04)

t=0; ang=0
while True:
    rate(60)
    for i in range(len(balls)):
        balls[i].pos+=vel[i]

        # برخورد با مرز → برعکس شدن سرعت
        for axis in ['x','y','z']:
            if abs(getattr(balls[i].pos,axis))>5:
                setattr(vel[i],axis,-getattr(vel[i],axis))

        # رنگ پویا
        balls[i].color=vector(0.3+0.7*abs(balls[i].pos.x%1),0.5,0.8)

    # 🔴 ریاضیات روی اولین کره
    x,y,z=balls[0].pos.x,balls[0].pos.y,balls[0].pos.z
    # مشتق جزئی مسیر → سرعت (مماس)
    v=vel[0].norm()
    tangent.pos=balls[0].pos; tangent.axis=v*1.5
    # گرادیان تابع ضمنی کره F=x²+y²+z²-r² → نرمال سطح
    grad=vector(2*x,2*y,2*z).norm()
    normal.pos=balls[0].pos; normal.axis=grad*1.5
    # ضرب خارجی → بردار عمود (Binormal)
    binorm=cross(v,grad).norm()
    binormal.pos=balls[0].pos; binormal.axis=binorm*1.5

    # حرکت نرم دوربین (نامحسوس)
    ang+=0.001
    scene.forward=rotate(vector(0,-1,-3),angle=ang,axis=vector(0,1,0))
    t+=0.03