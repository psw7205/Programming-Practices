from vpython import *
#GlowScript 2.7 VPython

Earth = sphere(pos=vec(0,0,0), radius = 6.4e6, color = color.blue)
craft = sphere(pos=vec(-10*Earth.radius,0,0), radius = 1e6, color = color.yellow, make_trail=True)
moon = sphere(pos=vec(4e8,0,0), radius = 1.75e6)

G = 6.7e-11
Earth.mass = 6e24
moon.mass = 7e22
craft.mass = 15e3

#initial vel
#craft.v = vec(0,2e3,0) # initial vel without moon
#craft.v = vec(0,4e3,0) # hyperbolic
#craft.v = vec(0,3.5e3,0) # hyperbolic
#craft.v = vec(0,3.3e3,0)
craft.v = vec(0,3.27e3,0) #critical pt.
#craft.v = vec(0,3.273e3,0) #loop

t = 0
dt = 60

while t < 10*365*24*60*60:
        rate(500)
        r = craft.pos - Earth.pos
        rmag = mag(r)
        rhat = r/rmag 
        Earth.f = G*Earth.mass*craft.mass/rmag**2*rhat
        
        rmoon = craft.pos - moon.pos
        rmoonmag = mag(rmoon)
        rmoonhat = rmoon/rmoonmag
        
        moon.f = G*moon.mass*craft.mass/rmoonmag**2*rmoonhat
        
        craft.f = (-Earth.f) + (-moon.f)
        
        craft.v = craft.v + craft.f/craft.mass*dt
        craft.pos = craft.pos + craft.v*dt
        t = t + dt