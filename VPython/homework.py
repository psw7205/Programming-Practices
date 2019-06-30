from vpython import *
#GlowScript 2.7 VPython
# prince
prince = box(pos=vector(0,4,0),radius= 1, color=color.red, make_trail= True) #m
prince.mass = 50 # kg
prince.v = vec(4.6,0,0)
# B612
B612 = sphere(pos=vector(0,0,0),radius= 3,color=color.blue) #m
B612.mass = 1.3e12 #kg
B612.v = vec(0,0,0)
t = 0
dt = 0.0001
G = 6.67e-11 #unit: N*m^2/kg^2
while (1):
    rate(10000)
    #force between B612 and prince
    r = B612.pos-prince.pos
    F = -G*B612.mass*prince.mass/mag(r)**2*norm(r)
    B612.force = F
    prince.force = -F
    #numerical integration
    prince.v = prince.v + prince.force/prince.mass*dt
    B612.v = B612.v + B612.force/B612.mass*dt
    prince.pos = prince.pos + prince.v*dt
    B612.pos = B612.pos + B612.v*dt
    t += dt