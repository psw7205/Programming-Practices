from vpython import *
#GlowScript 2.7 VPython

ground = box(pos = vec(0, -0.05, 0), size = vec(120,0.1,70), color = color.green)

ball = sphere(pos= vec(0,0.11, 0), radius = 0.11, color = color.yellow, make_trail = True)
ball.m = 0.45 #kg
ball.speed = 20 #m/s
ball.angle = 45*pi/180
ball.v = ball.speed*vec(cos(ball.angle),sin(ball.angle),0)#ball의 초기 속도 설정

wind_speed = 0 #m/s
wind_v = wind_speed*vec(20,0,0) #wind의 초기 속도 설정

#graph object
#gd = graph(xmin = 0, xmax =20, ymin=-12, ymax=12)
gcurve #함수를 이용하여 그래프 그리기
gball_vy = gcurve()
gball_y = gcurve(color=color.cyan)

scale = 0.2
#arrow를 이용하여 ball_vel 설정
#pos = 벡터의 시작 좌표, axis = 벡터의 축, shaftwidth = 벡터의 폭
#ball_vel = arrow(pos=ball.pos, axis=scale*ball.v, shaftwidth = 0.1)
attach_arrow(ball, "v", scale=scale, shaftwidth=0.1, color=color.white)


#scene setting
#scene.autoscale = False
#scene.range = 30

#const.
g = -9.8 #m/s**2

rho = 1.204 #kg/m**3 #밀도
Cdl = 0.275#0.3#1 #laminar 저항계수
#time setting
t = 0
dt = 0.005
#scene.waitfor('click')

while t < 20:
    rate(100)
#Gravity Force
    grav = ball.m * vec(0,g,0) #gravity
#Drag Force
    ball.v_w = ball.v - wind_v
    Cd = Cdl
    drag = -0.5*rho*Cd*(pi*ball.radius**2)*mag(ball.v_w)**2*norm(ball.v_w)
#공기저항력
    print(mag(grav), mag(drag))
#Sum of Forces
    ball.f = grav + drag #ball에 작용하는 알짜힘
#Euler method: time stepping
    ball.v = ball.v + ball.f/ball.m*dt #ball 속도 업데이트
    ball.pos = ball.pos + ball.v*dt #ball 위치 업데이트
    #ball_vel.pos = ball.pos
    #ball_vel.axis = scale*ball.v
#graph
    gball_vy.plot(pos=(t,mag(ball.v)))
    gball_y.plot(pos=(t,ball.pos.y))
#collision
    if ball.pos.y - ball.radius < 0:
        print(ball.pos.x)
        break
    t = t + dt
    
    
    
    
    
    
    
    
    
    
    
    
    