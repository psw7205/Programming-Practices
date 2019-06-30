from vpython import *
#GlowScript 2.7 VPython

tol = 0.0001 #tolerance

a = vec(1, 2, 3)
b = vec(1.001, 2, 3)

#  vec(1,2,3) = vec(1.001, 2, 3) : not equal // vec(1.00001, 2, 3) : equal

#if a.x == b.x and a.y == b.y and a.z == b.z:

if abs(a.x - b.x) < tol and abs(a.y - b.y) < tol and abs(a.z - b.z) < tol : # abs = | a |
    print("Equal")
else:
    print("Not Equal")

