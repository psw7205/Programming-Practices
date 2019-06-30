from vpython import *
#GlowScript 2.7 VPython


x_axis = arrow(axis = vec(10,0,0), shaftwidth = 0.1, color = color.red)
y_axis = arrow(axis = vec(0,10,0), shaftwidth = 0.1, color = color.blue)

speed = 15 # m/s
rad = radians(20) ## 45/180*pi # radian <--> degrees(pi/4)

angry_v = speed * vector(cos(rad), cos(pi/2-rad) , 0)

arrow(axis = angry_v, shaftwidth = 0.2)

print(angry_v)