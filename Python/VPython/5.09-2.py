from vpython import *
#GlowScript 2.7 VPython

#object
ceiling = box(pos = vec(0,0,0), size = vec(0.2, 0.01 ,0.2))
ball = sphere(pos=vec(0,-0.25,0), radius = 0.025 ,color = color.red,  make_trail= True) 
spring = helix(pos = ceiling.pos, axis = ball.pos - ceiling.pos, color = color.cyan, thickness = 0.003, coils = 40, radius = 0.015)

#const & physical prop
g = vec(0, -9.8, 0)
r0 = 0.25
ball.m = 1
kv = 0.5
ks = 100

#init
ball.v = vec(4,4,0)
Fgrav = ball.m*g

#time
t = 0
dt = 0.01

#display
scene.autoscale = True
scene.center = vec(0,-r0,0)
scene.waitfor('click')

#graph
traj = gcurve(color=color.red)


while t < 30:
    rate(100)
    
    #spring force
    r = mag(ball.pos)
    s = r - r0
    rhat = norm(ball.pos)
    Fspr = -ks*s*rhat
    
    
    #damping force
    Fdamp = - kv*dot(ball.v,rhat)*rhat
    
    #sum
    Fnet = Fgrav + Fspr + Fdamp
    
    
    #time stepping
    ball.v = ball.v + Fnet/ball.m*dt
    ball.pos = ball.pos + ball.v*dt
    t += dt
    
    #spring update
    spring.axis = ball.pos
    
    traj.plot(pos=(t, ball.pos.y))
    