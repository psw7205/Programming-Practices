from vpython import *
#GlowScript 2.7 VPython

#SCENE SETTING
scene.autoscale = False

r_i = vec(-10,0,0)
v_avg =vec(2,0,0)

t = 0
dt = 1/60
'''
r1 = r_i + v_avg*dt
r2 = r1 + v_avg*dt
r3 = r2 + v_avg*dt
r4 = r3 + v_avg*dt
print(r_i, r1, r2, r3)
'''

car = box(pos=r_i, make_trail = True)
car_arrow = arrow(pos=car.pos, color=color.red, axis = v_avg)
Ycar  = box(pos=vec(0,0,0), color = color.yellow, make_trail = True)

while t <= 1000:
        #print(car.pos)
        car.pos = car.pos + v_avg*dt
        car_arrow.pos = car.pos
        
        '''
        car.pos = car.pos + v_avg*dt
        =
        car.pos.x = car.pos.x + v_avg*dt
        car.pos.y = car.pos.y + v_avg*dt
        car.pos.z = car.pos.z + v_avg*dt
        '''
        Ycar.pos = vec(cos(t),sin(t),0) # circle
        #Ycar.pos = vec(t - sin(t),1- cos(t) ,0) # cycloid     
        
        t = t + dt
        #sleep(1/144)
        rate(60)