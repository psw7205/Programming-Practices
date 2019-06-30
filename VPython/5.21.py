from vpython import *
#GlowScript 2.7 VPython

#time
t = 0 #second
sf = 6#scale factor설정
dt = 60*60 # 1 hour
G = 6.673e-11 #중력상수 설정
r = 384400000

#Drawing
#sphere함수를 이용하여 Earth, Moon 설정
#pos = 구의 중심좌표, radius = 구의 반지름, texture = 질감, make_trail =자취 그리기
Earth = sphere(pos = vector(0,0,0), radius = sf*6400000,
texture=textures.earth)
Moon = sphere(pos = vector(r,0,0), radius = sf*1737000,
color=color.white, make_trail = True)

#Earth와 Moon의 질량 설정
Earth.mass =5.972e24 #kg
Moon.mass = 7.36e22 #kg

vi = sqrt(G*Earth.mass/r**1) #(구심력=만유인력)을 이용하여 Moon의 초기 속도를 구함

#Moon.v = vec(0,0,0)
Moon.v = vec(0,vi*0.7,0) #ellipse
#Moon.v = sqrt(2)*vec(0,vi,0)
#Moon.v = sqrt(3)*vec(0,vi,0) #parabolic
#Earth.v = vec(0,0,0)

Earth.v = -Moon.v*Moon.mass/Earth.mass #Moon과 Earth의 질량비를 이용하여 Earth의 초기 속도를 구함

#gcurve함수를 이용하여 k,u,ku그래프를 그림
#color = 그래프의 색
k_graph = gcurve(color = color.cyan)
u_graph = gcurve(color = color.green)
ku_graph = gcurve(color = color.black)

scene.waitfor('click') #클릭이 있을 때까지 기다림

while t < 10*365*24*60*60:
    rate(100)
    #calc. force
    #F = G*mEarth*mMoon/r**2
    #scene.waitfor('click')
    r = Moon.pos-Earth.pos #위치가 업데이트 되면서 Moon과 Earth의 거리업데이트
    Moon.f = -G*Earth.mass*Moon.mass/mag(r)**2*norm(r) #만유인력을 이용하여 Moon에 작용하는 힘을 구함
    Earth.f= -Moon.f #작용반작용 법칙을 이용하여 Earth에 작용하는 힘을 구함(Moon에 작용하는 힘과 크기는 같고 방향은 반대)
    
    #numerical integ.
    Moon.v = Moon.v + Moon.f/Moon.mass*dt
   
   #Earth.v = Earth.v + Earth.f/Earth.mass*dt
    Moon.pos = Moon.pos + Moon.v*dt
   
   #Earth.pos = Earth.pos + Earth.v*dt
    k = 0.5*Moon.mass*mag(Moon.v)**2 #운동에너지
    u = -G*Earth.mass*Moon.mass/mag(Moon.pos) #위치에너지
    k_graph.plot(t/60/60/24, k)
    u_graph.plot(t/60/60/24, u)
    ku_graph.plot(t/60/60/24, k + u)
    
    #print(mag(Earth.v))
    if mag(r) < Earth.radius+Moon.radius: #Earth와 Moon의 충돌확인
        print(t/60/60/24)
        break
    #time update
    t = t + dt