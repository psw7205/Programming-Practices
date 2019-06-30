from vpython import *
#GlowScript 2.7 VPython

x_axis = arrow(axis = vector(10, 0, 0), color = color.red, shaftwidth=0.1)
y_axis = arrow(axis = vector(0, 10, 0), color = color.green, shaftwidth=0.1)
z_axis = arrow(axis = vector(0, 0, 10), color = color.blue, shaftwidth=0.1) 

r = vector(3,4,5)
r_2 = -r/2


r_arrow = arrow(pos = vector(0,0,0), axis = r, shaftwidth=0.5)
r_arrow_2 = arrow(pos = vector(0,0,0), axis = r_2, shaftwidth=0.25)

r_mag = mag(r) #sqrt(r.x**2 + r.y**2 + r.z**2) # magnitude
r_mag_2 = mag(r_2)
r_hat = norm(r) #r / r_mag

r_arrow_3 = arrow(pos = vector(0,0,0), axis = r_hat, shaftwidth=1)


print(r, r_mag, r_mag_2, r_hat)

r_mag_3 = mag(r_hat)
print(r_mag_3)

