from vpython import *
#GlowScript 2.7 VPython

#SCENE SETTING
scene.autoscale = True

r_i = vec(-10,0,0)
v_i = vec(5,5,0)
a_avg = vec(0,-2,0)
car_vel = v_i

#graph
gh = graph(fast = False) #xmin = 0, xmax = 10, ymin = 0, ymax = 10)
car_y = gcurve()
car_x = gcurve(color = color.green)
car_vy = gcurve(color = color.yellow)
car_ay = gcurve(color = color.red)

t = 0
dt = 1/60

car = box(pos=r_i, make_trail = True, trail_type = "points", trail_radius = 0.2, interval = 20)
car_arrow = arrow(pos=car.pos, color=color.red, axis = v_i, shaftwidth = 0.2)
Ycar = box(pos=vec(-10,0,0), color = color.yellow, make_trail = True, trail_type = "points", trail_radius = 0.2, interval = 20)

while t <= 10:
    
        car_y.plot(pos=(t, car.pos.y))
        car_x.plot(pos=(t, car.pos.x))
        car_vy.plot(pos=(t, car_vel.y))
        car_ay.plot(pos=(t, a_avg.y))
        
        vi = car_vel
        vf = car_vel + a_avg*dt
        car_vel = vf
        car.pos = car.pos + 0.5 * (vi+vf)*dt
        Ycar.pos = r_i - vec(0, 2,0) + v_i *t + 0.5 * a_avg * t**2        
        
        car_arrow.axis = car_vel
        car_arrow.pos = car.pos
    
        t = t + dt
        #sleep(1/144)
        
        rate(60)
        
print(car.pos, Ycar.pos, "diff. =", car.pos - Ycar.pos)