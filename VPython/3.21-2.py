from vpython import *
#GlowScript 2.7 VPython

v = vec(3,4,0)
r = norm(vec(1,0.5,0)) # axis x

v_x = dot(v,r) * r  #horizon
v_y = v - v_x  #vertical

v_arr = arrow(axis=v, shaftwidth = 0.2)
r_arr = arrow(axis=r, shaftwidth = 0.1, color = color.green)
v_x_arr = arrow(axis=v_x, shaftwidth = 0.1, color = color.red)
v_y_arr = arrow(axis=v_y, shaftwidth = 0.1, color = color.blue)

