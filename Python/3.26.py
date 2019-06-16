from vpython import *
#GlowScript 2.7 VPython

r_i = vec(1,2,0)
r_f = vec(1,4,0)
dr = r_f - r_i

t_i = 1
t_f = 1.3
dt =  t_f - t_i

v_avg = dr/dt

ball = sphere(pos = r_i)
ball_arrow = arrow(pos = ball.pos, axis = v_avg, color = color.red, shaftwidth = 0.1)

