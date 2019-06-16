from vpython import *
#GlowScript 2.7 VPython

#box함수를 이용하여 obj1설정
#texture = 질감
obj1 = box(texture = textures.wood)
omega = vec(-3.0,1.0,2.0)
#arrow함수를 이용하여 omega_axis설정
#pos = arrow의 시작 좌표, axis = arrow의 축, shaftwidth = arrow의 두께,color = 색깔
omega_axis = arrow(pos = -0.5*omega, axis = omega, shaftwidth = 0.02,color=color.red)
scene.range = 3 #화면 범위 설정
scene.waitfor('click') #마우스 클릭이 있을 때까지 화면 멈춤
t = 0
dt = 0.01
while 1:
    rate(100)
    dtheta = mag(omega)*dt #omega벡터의 크기 와 dt의 곱으로 dtheta설정
    obj1.rotate(angle=dtheta, axis=norm(omega)) #rotate함수를 이용하여 obj1을 회전
    #dtheta 라디안 각도로 omega의 단위 벡터 방향 축을 가지고 회전