from vpython import *
#GlowScript 2.7 VPython

craft = box(pos= vec(0,30,0), size = vec(10,10,10)) 
craft.mass = 1
craft.v = vec(0,0,0)
barrow = arrow(pos=  craft.pos, color=color.red, axis = vec(0,-9.8,0))

ground = box(pos = vec(0,0,0), size = vec(50,1,50))

g = vec(0,-9.8/6,0)

t = 0
dt = 0.05


def mouseclick(evt):
    global a
    a = vec(0,4,0)

a = vec(0,0,0)

while 1:
    rate(10)
    scene.bind('mousedown',mouseclick)
    
    craft.f = craft.mass * g
    craft.f = craft.f + a
    craft.v = craft.v + craft.f/craft.mass*dt
    craft.pos = craft.pos + craft.v*dt
    barrow.pos = craft.pos
    barrow.axis = craft.f
    
    if craft.pos.y < ground.pos.y :
        break