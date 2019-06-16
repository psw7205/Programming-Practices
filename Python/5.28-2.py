from vpython import *
#GlowScript 2.7 VPython

# Written by Bruce Sherwood, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

scene.background = color.white
scene.height = scene.width = 600
scene.center = vector(0,4,0)
scene.range = 20

# clay position 0=full radius on left, 1=left, 2=top, 3=right, 4=full radius onright
position = 0

# wheel
m = 0.1
bb = []
R = 10
sr = 0.8
wheel = []

label(pos=vector(0,-1.3*R,0), text='Click to see different situations',color=color.black, box=0)

showomega = label(pos=vector(0,1.3*R,0), text='+0.3 rad/s', color=color.black,box=0, visible=False)

for theta in arange(0,2*pi,pi/4):
    bb.append(sphere(pos=vector(-R*cos(theta), R*sin(theta),0), radius=sr,color=color.red))
    
for b in bb[:4]:
    wheel.append(cylinder(pos=(b.pos), axis = (bb[bb.index(b)+4].pos - b.pos), color=color.gray(.7), radius = 0.3))

wheel.append(cylinder(pos=vector(0,0,-R/4), axis = vector(0,0,R/2), radius=1,color=color.gray(.7)))

for b in bb:
    wheel.append(b)
w = compound(wheel)

clay = sphere(pos=vector(bb[position].pos.x,20,0), radius=.5,color=vector(.7,.5,0))
clay.p = vector(0,-3,0)
clay.m = 0.1
psc = 1.5
clay.pa = arrow(pos=clay.pos, axis=clay.p*psc, color=color.green,visible=False)
I = (8*m+clay.m)*R**2

run = False
drop = True
clicked = False

def getclick(evt):
    global clicked
    clicked = True
    
scene.bind('click', getclick)

# drop clay
dt = 0.01
while True:
    rate(100)
    if clicked:
        if not drop: # interrupted the rotation
            clicked = False
            position += 1
            if position > 4:
                position = 0
            w.rotate(angle=-theta, axis=vector(0,0,10)) # restore wheel tooriginal position
            clay.pos = vector(bb[position].pos.x,20,0)
            showomega.visible = False
            drop = True
            run = False
            continue
        clicked = False
        r = (clay.pos - w.pos)
        clay.L = cross(r, clay.p)
        clay.pa.visible = True
        run = True
        drop = True
    if not run: continue
    if drop and clay.pos.y > bb[position].pos.y+sr+clay.radius:
        clay.pos = clay.pos + (clay.p/clay.m)*dt
        clay.pa.pos = clay.pos
        continue
    if drop:
        drop = False
        clay.pa.visible = False
        omega = mag(clay.L)/I
        dtheta = omega*dt
        if position > 2:
            dtheta = -dtheta
        theta = 0
        plus = '+'
        if dtheta < 0: plus = '-'
        showomega.text = plus+str(round(100*omega)/100)+ ' rad/s'
        showomega.visible = True
    w.rotate(angle=dtheta, axis=vector(0,0,1))
    clay.rotate(angle=dtheta, axis=vector(0,0,1), origin=vector(0,0,0))
    theta += dtheta
        
