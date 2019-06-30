from vpython import *
#GlowScript 2.7 VPython

# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0
# Modified by 502

scene.height = 600
scene.width = 400
scene.range = 15
th = 0.5
R = 10

M = 0.07
disc = cylinder(pos = vector(0,-th/2,0), color=color.cyan, radius=R,axis=vector(0,th,0))
band1 = box(pos=vector(0,0,0),color=color.red, size=vector(2*R,th+.2,th+.2))
band2 = box(pos=vector(0,0,0),color=color.red, size=vector(th+.2,th+.2, 2*R))
wheel = compound([disc,band1,band2])
lbar = arrow(pos=wheel.pos, color=vector(.7,.5,0), axis = vector(0,1,0),shaftwidth = 2*th)

t = 0
dt = 0.01

domega = pi/3
omega = pi

I = 0.5*M*R**2
L = I*omega

lbar.axis = vector(0,L,0)

clicked = False

def getclick():
    global clicked
    clicked = True
    
scene.bind('click', getclick)

while True:
    rate(100)
    wheel.rotate(angle=omega*dt, axis = vector(0,1,0))
    t = t + dt
    if clicked:
        clicked = False
        omega = omega - domega
        L = I*omega
        lbar.axis = vector(0,L,0)
        if (omega < pi) or (omega > pi):
            domega = -domega
            