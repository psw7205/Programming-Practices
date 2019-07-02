from vpython import *
#GlowScript 2.7 VPython

scene = display(background = color.white,forward = vec(-1,-0.5,-1))
#좌표계

curve(scene = scene, pos = [vec(10,0,0),vec(-10,0,0)],color=color.red) #x축
curve(scene = scene, pos = [vec(0,10,0),vec(0,-10,0)],color=color.blue) #y축
curve(scene = scene, pos = [vec(0,0,10),vec(0,0,-10)],color=color.red) #z축
ball1 = sphere(pos = vec(0,1,0),radius = 0.5, color=color.red)
ball2 = sphere(pos = vec(5,1,0),radius = 0.5, color=color.blue)
velocity1 = vector(1,0,0)
velocity2 = vector(0,0,0)
dt = 0.01

while True:
    ball1.pos = ball1.pos + velocity1*dt
    ball2.pos = ball2.pos + velocity2*dt
    if mag(ball1.pos - ball2.pos) <= 1.0:
        velocity2.x = velocity1.x
        velocity1.x = 0
    rate(100)