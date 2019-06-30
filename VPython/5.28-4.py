from vpython import *
#GlowScript 2.7 VPython

M = 10 #질량 설정 
L = 2 #길이 설정
#cylinder함수를 이용하여 disc설정
#radius = 밑면 반지름, axis = pos에서 원통의 다른 끝을 가리킴(length를 설정하게 되면 축 크기가 length와 동일하게 됨), color = 실린더 색깔

disc = cylinder(radius = .1, axis = vec(1,0,0), length = L, color = color.red)
x = 0
dx = .01
I = 0
density = M/L #밀도 설정

#cylinder함수를 이용하여 element설정
element = cylinder(radius = .11, length = dx, pos = vec(0,0,0), axis = vec(1,0,0), color = color.cyan)

while x < L: #적분을 이용하여 회전관성 구함
    rate(50)
    dI = dx * density * x**2
    I = I + dI
    element.pos.x = element.pos.x + dx
    x = x + dx

print(I) #회전관성 출력
print("Error = ", abs(I-1/3*M*L**2)) #적분을 이용하여 구한 회전관성과 공식을 이용하여 구한 회전관성의 차이