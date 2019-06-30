from vpython import *
#GlowScript 2.7 VPython

riList = []
objList = []
scene.range=5

#box를 이용하여 ground 설정
ground = box(length = 10, height = 0.001, width = 10)

for i in range(0,100):
    riList.append(vec(0,0,0))
for ri in riList:
    objList.append(sphere(pos = ri, radius = 0.05, color = vec(random(), 
    random(), random()), make_trail=True, retain = 30))
    
vi = vec(0,5.0,0) #속도
a = vec(0,-3,0) #가속도

for obj in objList:
    obj.v = vi #+ vector(random(),random(),random())
    
t = 0
dt = 0.01

while t < 15:
    print(t)
    if abs(t - 1) < 0.001:
        print("explosion!")
        #rate(1)
        for obj in objList:
            obj.v = obj.v + vec(random()-0.5,random()-0.5,random()-0.5)
    for obj in objList:
        obj.v = obj.v + a*dt #속도 업데이트
        obj.pos = obj.pos + obj.v*dt #위치 업데이트
        if obj.pos.y < 0:
            obj.pos.y = 0
            obj.color = vec(random(), random(), random()) #랜덤으로 색지정
            obj.v.y = -0.8*obj.v.y
    t = t + dt #시간 업데이트
    rate(100)