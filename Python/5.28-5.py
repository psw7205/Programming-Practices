from vpython import *
#GlowScript 2.7 VPython

M=1
Lrod = 10
R = .1
Laxle = 4*R
I = (1/12)*M*Lrod**2 + (1/4)*M*R**2 #회전관성
#cylinder함수를 이용하여 rod, axle 설정
#pos= 밑면의 중심좌표, radius = 반지름, color = 색, axis = cylinder의 축
rod = cylinder(pos=vector(-1,0,0), radius=R, color=color.orange, axis=vector(Lrod,0,0))
axle = cylinder(pos=vector(-1+Lrod/2,0,-Laxle/2), radius=R/6, color=color.red, axis=vector(0,0,4*R))
L = vector(0,0,0) # angular momentum
dt = 0.0001
t=0
dtheta = 0
while t<20:
    rate(1000)
    torque = vector(0,0,20) # constant torque
    #numerical time integration
    L = L + torque*dt # Apply Angular Momentum Principle
    omega = L/I
    omega_scalar = dot(omega, norm(axle.axis)) #omega벡터와 axle의 축벡    터 내적
    dtheta = omega_scalar * dt
    rod.rotate(angle=dtheta, axis=norm(axle.axis), origin=axle.pos) #rod회전
    t = t + dt