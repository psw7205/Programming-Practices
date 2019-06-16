from vpython import *
#GlowScript 2.7 VPython

r_i = vec(1,1,0)
v_avg =vec(1,2,0)

t = 0
dt = 2

r1 = r_i + v_avg*dt
r2 = r1 + v_avg*dt
r3 = r2 + v_avg*dt
r4 = r3 + v_avg*dt
...

print(r_i, r1, r2, r3)