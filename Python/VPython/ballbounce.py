from vpython import *
#GlowScript 2.7 VPython
 
count=0
 
scene.range = 30
 
t = text(text='START', pos = vec(0,0,0), align='center', height = 10, depth=-0.3, color=color.red)
t2= text(text='PRESS CLICK', pos = vec(0,-10,0), align='center', height = 5, depth=-0.3, color=color.red)
 
scene.waitfor('click')
t.height = 0
t2.height = 0
 
#object
floor1 = box(pos=vec(0,0,0), size = vec(100,1,1), color=color.green)
endFlag = box(pos=vec(52,323,0), size = vec(1,6,1), color = color.red)
endFlag2 = cone(pos=vector(52,325,0), axis=vector(-5,0,0), radius=2, color = color.red)
 
ball = sphere(pos=vec(0,1.5,0), radius=1, make_trail = True,retain = 20)
ball.m = 10
ball.v = vec(0,0,0)
 
#slider Function
def exslider(s):
    return s.value

#slider
slide = slider(bind = exslider, min = -5, max = 5,step = 0.1)

# slide value initialization
slide.value = 0
scene.append_to_caption('  wind\n\n')

#about wind
wind_v = vec(0,0,0)


 
#label
timelabel=label(pos=vec(ball.pos.x-50,ball.pos.y,ball.pos.z))
windlabel=label(pos=vec(ball.pos.x+50,ball.pos.y,ball.pos.z))
 
list=[]
item_list =[]
n = 32
n2 =3
for i in range(1,n2+1):
    if i % 3 ==0  :
        itemi = box(pos = vec(2*i-30,i*32,0),size = vec(2,1,1) , color = color.magenta)
    if i % 3 ==1  :
        itemi = box(pos = vec(i*2+50,i*7+46,0), size = vec(2,1,1) , color = color.yellow)
    if i % 3 ==2 :
        itemi = box(pos = vec(i+20,i*10+2,0),size = vec(2,1,1)  , color = color.blue)   
        
    item_list.append(itemi)
    
for i in range(2,n+1):
 
    if i % 5 ==0 and i%2==0 :
        floori = box(pos = vec(2*i-100,i*7+50,0), size = vec(20,1,1), color = color.green)
    if i % 5 ==1 and i%2==1 :
        floori = box(pos = vec(2*i-50,i*10-20,0), size = vec(20,1,1), color = color.green)
    if i % 5 ==2 :
        floori = box(pos = vec(i+20,i*10,0), size = vec(20,1,1), color = color.green)
        if i==32 : 
            floori =box(pos = vec(i+20,i*10,0), size = vec(20,1,1), color = color.white)
    if i % 5 ==3 and i%2==1 :
        floori = box(pos = vec(i*2+50,i*7+30,0), size = vec(20,1,1), color = color.green)
    if i % 5 ==4 and i%2==0 :
        floori = box(pos = vec(i*2+100,i*10,0), size = vec(20,1,1), color = color.green)
        
    list.append(floori)
 
 
#constants and physical properties
g = vec(0,-9.8,0)
item_g=1
e = 0.9 # restitution coefficient
rho = 1.204 # air density
cd = 0.35 # drag coefficient
 
scene.camera.follow(ball)
blue_effect=2
a = False
#function
def mouseclick(evt):
    global a
    global count
    a = True
    ball.v =blue_effect*( evt.pos - ball.pos)
    
mouseclick_limit=3

def itemcollision(ball,itemi) :
    if ball.pos.x + ball.radius > (itemi.pos.x - itemi.size.x/2) and ball.pos.x - ball.radius < (itemi.pos.x + itemi.size.x/2):
        if ball.pos.y - ball.radius - itemi.pos.y < 0.5+0.1 :
            if ball.pos.y > itemi.pos.y-0.5 :
                    return 1
           
 
def collision(ball, floori, e) :
    if ball.pos.x + ball.radius > (floori.pos.x - floori.size.x/2) and ball.pos.x - ball.radius < (floori.pos.x + floori.size.x/2):
        if ball.pos.y - ball.radius - floori.pos.y < 0.5 :
            if ball.pos.y > floori.pos.y :
                ball.v.y = -ball.v.y * e
                if abs(ball.v.y) < 0.05:
                    ball.v = vec(0,0,0)
                    Fnet = 0
                    ball.pos.y = floori.pos.y +1.5
                    ball.color = color.white
                    #ball.trail_color=color.white
                    scene.bind('mousedown',mouseclick)
                    return 1
                    #if ball.pos.y - ball.radius - floori.pos.y - 0.05 < 0.1:
                            #return 0
 
#mouse
scene.bind('mousedown',mouseclick)
 
# time setting
t = 0
dt = 0.01
bluetime=0
magentatime=0
flag = 1
 
def firework():
    riList = []
    objList = []
    #box를 이용하여 ground 설정
    ground = box(pos=vec(52,320,0), size = vec(20,1,1), color = color.red)
 
    for i in range(0,20):
        riList.append(vec(52,320,0))
    for ri in riList:
        objList.append(sphere(pos = ri, radius = 0.5, color = vec(random(), 
        random(), random()), make_trail=True, retain = 15))
        
    vi = vec(0,20.0,0) #속도
    a = vec(0,-16,0) #가속도
    
    for obj in objList:
        obj.v = vi + vector(random(),random(), 0)
        
    t = 0
    dt = 0.01
    
    while t < 10:
        if abs(t - 3) < 0.01:
            #rate(1)
            for obj in objList:
                obj.v = obj.v + vec(5*(random()-0.5),5*(random()-0.5),0)
        for obj in objList:
            obj.v = obj.v + a*dt #속도 업데이트
            obj.pos = obj.pos + obj.v*dt #위치 업데이트
            if obj.pos.y < 320:
                obj.pos.y = 320
                obj.color = vec(random(),random(), random()) #랜덤으로 색지정
                obj.v.y = -0.9*obj.v.y
        t = t + dt #시간 업데이트
        rate(500)
 
moveflo=1
moveflo2=1
blue_on=0
magenta_on=0
#while 1:
    #scene.bind('mousedown',mouseclick)
    #flag = 1
    
while 1:
        a = False ################################
        rate(300)
        if blue_on==1:
            if t-bluetime-15>0 :
                mouseclick_limit=3
                ball.color=color.white
                ball.trail_color=color.white
                count=0
                blue_on=0
        if magenta_on==1:
            if t-magentatime-15>0 :
                ball.color=color.white
                ball.trail_color=color.white                
                magenta_on=0
                item_g=1
             
        if a == True: ################################
            ball.color=color.white
            #ball.trail_color=color.white
            count = count + 1 ################################
    
        if count >= mouseclick_limit: 
            scene.unbind('mousedown',mouseclick)
            ball.color=color.cyan
            #ball.trail_color=color.cyan
            count=0
            
        
        for i in list :            
            if i == list[5] :
                i.color=color.red
        for i in list :            
            if i == list[11] :
                i.color=color.red 
        for i in list :            
            if i == list[28] :
                i.color=color.red
                
        for i in list :            
            if i == list[15] :
                i.color=color.yellow
                if i.pos.x >50 or i.pos.x <-50:
                    moveflo= moveflo*-1
                i.pos.x=i.pos.x + 0.05 *moveflo
        for i in list :            
            if i == list[20] :
                i.color=color.yellow
                
                if i.pos.x >50 or i.pos.x <-50:
                    moveflo2= moveflo2*-1
                i.pos.x=i.pos.x + 0.05 *moveflo2
                
        if ball.pos.y < -50:
            ball.v = vec(0,0,0)
            Fnet = 0
            text(text='GAME OVER', pos = ball.pos, align='center', height = 10, depth=-0.3, color=color.red)
            ball.visible = False
            ball.clear_trail()
            
     
        Fgrav = ball.m*g*item_g  
        ball.v_w=ball.v-wind_v
        Fdrag = -0.5*rho*cd*(pi*ball.radius**2)*mag(ball.v_w)**2*norm(ball.v_w)
        Fnet = Fgrav + Fdrag
        
        ball.v = ball.v + Fnet/ball.m*dt
        ball.pos=ball.pos+ball.v*dt
        
        #label position update by box's position
        #t5 = text(text='time : ' + t  + 's' , align='left', height = 2, depth=-0.3)
        #t6 = text(text='wind :'+wind_v.x + 'm/s' , align='right', height = 2, depth=-0.3) 
        wind_v = vec(slide.value,0,0) 
        timelabel.pos = vec(ball.pos.x+40,ball.pos.y,ball.pos.z)
        windlabel.pos=vec(ball.pos.x-40,ball.pos.y,ball.pos.z)
        
        
        #label can be only string
        timelabel.text = 'time : ' + int(t,1)  + 's' 
        windlabel.text = 'wind : ' + wind_v.x + 'm/s' 
        
        #anothert=anothert+dt
        
        if collision(ball,floor1,e):
            if count >=mouseclick_limit:
                count = 0
            #break
        
        
                   
        for k in list:
            if collision(ball,k,e):
                if count >=mouseclick_limit:
                    count = 0
                #flag = 0
                if k == list[5]:
                    k.size=vec(0,0,0)
                    k.visible =False
                    del k
                if k == list[11] :
                    k.size=vec(0,0,0)
                    k.visible =False
                    del k
                if k == list[28] :
                    k.size=vec(0,0,0)
                    k.visible =False
                    del k
                if k == list[15] :
                    ball.pos.x = ball.pos.x + 0.05 * moveflo
                if k == list[20] :
                    ball.pos.x = ball.pos.x + 0.05 * moveflo2
                
        for q in item_list:
            if itemcollision(ball,q):
                if q == item_list[0]:
                   ball.color=color.yellow
                   ball.trail_color=color.yellow
                   
                   r = round(random()*10)
                   ball.pos = list[r].pos + vec(0,2.5,0)
                   ball.clear_trail()
                   
                if q == item_list[1] :
                   ball.color=color.blue
                   ball.trail_color=color.blue
                   mouseclick_limit=1000
                   bluetime=t
                   blue_on=1
                if q == item_list[2] :
                   ball.color=color.magenta
                   ball.trail_color=color.magenta
                   item_g=1/6
                   magenta_on=1
                   magentatime=t
                q.size=vec(0,0,0)
                q.pos=vec(0,100,0)
                q.visible =False
                del q    
        #if flag == 0:
            #break
    
        if abs(ball.pos.x - endFlag.pos.x) < 10 and abs(ball.pos.y - endFlag.pos.y) < 0.05:
            firework()
            t3 = text(text='GOAL IN', pos = vec(32,330,0), align='center', height = 10, depth=-0.3, color=color.red)
            t4 = text(text='TIME : '+ int((t),1) + 's', pos = vec(32,310,0), align='center', height = 10, depth=-0.3, color=color.red)
            break
        t = t + dt