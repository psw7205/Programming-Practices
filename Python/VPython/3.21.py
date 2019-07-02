from vpython import *
#GlowScript 2.7 VPython

a = vec(0,4,0)
b = vec(3,0,0)

c = a - b

e = dot(a, b)
rad = acos(e/mag(a)/mag(b)) # ==  arccos(e/(mag(a)*mag(b)))
degree = degrees(rad)

f = cross(a,b)


a_arr = arrow(pos = vec(0,0,0), axis = a, color = color.red,shaftwidth=0.2)
b_arr = arrow(pos = vec(0,0,0), axis = b, color = color.green,shaftwidth=0.2)
c_arr = arrow(pos = b, axis = c, color = color.blue,shaftwidth=0.2)
f_arr = arrow(axis = f, color = color.cyan, shaftwidth=0.2)

#pos = start point, axis = vector

print("a + b = ", c)
print("dot product (a, b) = ", e)
print("degree = ", degree)
print("cross product (a, b) = ", f)