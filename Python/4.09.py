from vpython import *
#GlowScript 2.7 VPython

tol = 0.0001

v_i = vec(3,0,0)
a_avg = vec(1,0,0)
Ycar_v = vec(0,0,0)

#graph
gh = graph(fast = False) #xmin = 0, xmax = 10, ymin = 0, ymax = 10)

car_x = gcurve(color = color.red)
Ycar_x = gcurve(color = color.blue)

t = 0
dt = 0.01

car = box(pos=vec(-8,0,0), color = color.red)
Ycar = box(pos=vec(-8,2,0), color = color.blue)

while t <= 10:
    
        car_x.plot(pos=(t, car.pos.x))
        Ycar_x.plot(pos=(t, Ycar.pos.x))
        

        car.pos = car.pos + v_i*dt
        Ycar_v = Ycar_v + a_avg * dt
        Ycar.pos = Ycar.pos + Ycar_v *dt  
        
        if abs(car.pos.x - Ycar.pos.x) < tol :
            break
        
        t = t + dt
        #sleep(1/144)
        
        rate(144)
        