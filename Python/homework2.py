from vpython import *
#GlowScript 2.7 VPython

# objects1
ceiling = box(pos=vector(0,0,0),size = vector(0.2, 0.01, 0.2))         
ball = sphere(pos=vector(0.0, -0.25,0.0), radius=0.025, color=color.orange, make_trail=True)
spring = helix(pos=ceiling.pos, axis=ball.pos-ceiling.pos, color=color.cyan, thickness=.003, coils=40, radius=0.015)

# objects2
ball2 = sphere(pos=vector(0.0, -0.5,0.0), radius=0.025, color=color.red, make_trail=True)
spring2 = helix(pos=ball.pos, axis=ball2.pos-ball.pos, color=color.blue, thickness=.003, coils=40, radius=0.015)


# constants and physical properties
g = vector(0,-9.8,0)

ball.m = 1      
r0 = 0.25
ks = 100 #탄성계수
kv = 0.5 # 댐퍼

ball2.m = 1
r2 = 0.25
ks2 = 100  #탄성계수
kv2 = 0.5 # 댐퍼

# initial values
ball.v = vector(-1,-1,0)
Fgrav = ball.m*g

ball2.v = vector(2,2,0)
F2grav = ball2.m*g

# time setting
t = 0           
dt = 0.01  

# the display
scene.autoscale = True          
scene.center = vector(0,-r0,0)   
scene.waitfor('click')          

# graph
traj = gcurve(color=color.orange)
traj2 = gcurve(color=color.red)


# calculation loop

while t < 30:
    rate(100)
    
    # spring force
    r = mag(ball.pos)
    s = r - r0
    rhat = norm(ball.pos)
    Fspr = -ks*s*rhat
    
    r1 = mag(ball2.pos-ball.pos)
    s2 = r1 - r2
    r2hat = norm(ball2.pos-ball.pos)
    F2spr = -ks2*s2*r2hat  
    
    
    # damping force
    Fdamp = -kv*dot(ball.v,rhat)*rhat
    F2damp = -kv2*dot(ball2.v,r2hat)*r2hat
    
    # sum. of force
    Fnet = Fgrav + Fspr + Fdamp - F2spr - F2damp 
    F2net = F2grav + F2spr + F2damp

    # time stepping
    ball.v = ball.v + Fnet/ball.m*dt
    ball.pos = ball.pos + ball.v*dt
   
    ball2.v = ball2.v + F2net/ball2.m*dt
    ball2.pos = ball2.pos + ball2.v*dt 
    
    t = t + dt

    # spring update
    spring.axis = ball.pos
    spring2.pos = ball.pos
    spring2.axis = ball2.pos-ball.pos
    
    
    traj.plot(pos=(t,ball.pos.y))
    traj2.plot(pos =(t,ball2.pos.y))

