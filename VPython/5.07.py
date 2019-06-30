from vpython import *
#GlowScript 2.7 VPython

scene.range = 20
scene.width = 700
scene.height = 700

ground = box(size=vec(40,40,1), color= color.green)
ball = sphere(pos=vec(-18,0,0), radius = 0.5)

ground.pos.z = ground.pos.z - ground.width/2-ball.radius
hole=cylinder(pos=vec(15,0,ground.pos.z+ground.width/2),axis=vec(0,0,1),radius=3*ball.radius, color= vec(0.8,0.8,0.8))
hole.pos.z = hole.pos.z - mag(hole.axis)*0.9
putt = arrow(pos=ball.pos, axis=vec(0,0,0), shaftwidth=0.5, color=color.yellow)

#properties
ball.m = 0.045
g = 9.8
mu = .5


initialspeed = 18
scale = initialspeed
putt.axis = scale*vec(1,0,0)
ball.v = initialspeed*vec(1,0,0)

#time
t = 0
dt = 0.01

scene.waitfor('click')

while t < 100:
    rate(100)
    
    Ffr = -mu*ball.m*g*norm(ball.v) #friction
    Fnet = Ffr
    
    #Euler method : time stepping
    ball.v = ball.v + Fnet/ball.m*dt
    ball.pos = ball.pos + ball.v*dt
    putt.pos = ball.pos
    
    scale=mag(ball.v) #ball의 속도
    
    if scale < 0.05:
        ball.v = vec(0,0,0)
    putt.axis=scale*norm(ball.v)
    print(scale)
    t = t + dt
    