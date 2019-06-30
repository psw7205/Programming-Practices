from vpython import *
#GlowScript 2.7 VPython

x0 = vector(.65,0,0)


wall = box(size=vec(.04,.5,.3),pos=vec(-.77,.15,0))
spring = helix(pos=vec(-.75,0,0),axis=x0, radius=.08,coils=6,thickness=.01,color=color.blue)
block = box(pos=vec(0,0,0),size=vec(.2,.2,.2),color=color.red)
putt = arrow(pos=vec(0,0,0), axis=vec(0,0,0), shaftwidth=0.5, color=color.yellow)

k = 10
m = 10
b=2

v = vector(0,0,0)
a = vector(0,0,0)
F = vector(0,0,0)
block.pos=vec(0.25,0,0) # Set Initial position of block and connect spring

x = block.pos
spring.axis = x0 + x
finished = False
dt = .01
while not finished:
    rate(100)
    F = -k*x -b*v #용수철-댐퍼힘
    a = F/m #가속도 업데이트
    v += a * dt #속도 업데이트
    x += v + .5 * a * dt**2 #위치 업데이트
    block.pos = x
    spring.axis = x0 + x
    putt.pos = x + vec(.1,0,0)
    putt.axis = v
