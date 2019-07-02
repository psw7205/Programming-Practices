from vpython import *
#GlowScript 2.7 VPython

a = cone(texture = textures.earth)

a.rotate(angle = -pi/2 , axis = vec(0,0,1), origin=vec(0,0,0))

a.rot_axis = vec(0,1,0)
a.w = 0*a.rot_axis

t = 0
dt = 0.01

while t < 10:
    rate(100)
    
    #a.v = a.v + a.f/a.m*dt
    #a.pos = a.pos + a.v*dt
    
    a.alpha = pi * a.rot_axis
    a.w = a.w + a.alpha*dt
    a.rotate(angle = mag(a.w)*dt, axis = norm(a.w), origin = a.pos)
    t = t + dt
    