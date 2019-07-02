from vpython import *
#GlowScript 2.7 VPython

#sphere함수를 이용하여 ball1, ball2설정
#radius = 구의 반지름, pos = 구의 중심좌표, color = 구의 색
ball1 = sphere(radius=0.5*65.5e-3) #korean pool
ball2 = sphere(radius=0.5*65.5e-3, pos=vec(1,0,0), color=color.red)

#ball1,ball2의 속도, 질량, 힘 설정
ball1.v = vec(1,0,0)
ball2.v = vec(0,0,0)
ball1.m = 0.21
ball2.m = 0.21
ball1.f = vec(0,0,0)
ball2.f = vec(0,0,0)

#반발계수 설정
e = 1.0

tot_energy = 0.5*ball1.m*mag(ball1.v)**2+0.5*ball2.m*mag(ball2.v)**2 #ball1과 ball2의 운동에너지 합

t = 0
dt = 0.03

#gcurve를 이용하여 그래프 그리기
traj =gcurve()
en_traj = gcurve(color = color.cyan)

scene.autoscale = True
scene.range = 2

#collision함수 정의
def collision(b1, b2, e) :
    dist = mag(b1.pos-b2.pos) #b1과 b2의 위치 차이의 크기
    tot_m = b1.m + b2.m #b1과 b2의 질량 합
    if dist < b1.radius + b2.radius : #충돌 확인
        v1 = ((b1.m-e*b2.m)*b1.v + (1+e)*b2.m*b2.v) / tot_m
        v2 = ((b2.m-e*b1.m)*b2.v + (1+e)*b1.m*b1.v) / tot_m
        b1.v = v1
        b2.v = v2
        
        return True
    else:
        return False
        
while t < 10:
    rate(30)
    colcheck = collision(ball1,ball2, e)
    if colcheck == True:
        print("Collision!")
        #scene.waitfor('click')
    
    #Euler method: time stepping
    ball1.v = ball1.v + ball1.f/ball1.m*dt
    ball2.v = ball2.v + ball2.f/ball2.m*dt
    ball1.pos = ball1.pos + ball1.v*dt
    ball2.pos = ball2.pos + ball2.v*dt
    
    tot_energy = 0.5*ball1.m*mag(ball1.v)**2+0.5*ball2.m*mag(ball2.v)**2
    traj.plot(pos=(t,ball1.v.x))
    en_traj.plot(pos=(t,tot_energy))
    
    t = t + dt


