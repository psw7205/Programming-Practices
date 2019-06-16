from vpython import *
#GlowScript 2.7 VPython

#object
water = box(pos=vec(0,0,0), size=vec(10,10,10), color = color.blue, opacity = 0.5)
wood = box(pos=vec(0,10,0), size=vec(1,1,1), texture = textures.wood)

# setting
wood.v = vec(0,0,0)
wood.rho = 500
water.rho = 1000
wood.volume = wood.size.x * wood.size.y * wood.size.z
wood.volume_im = wood.volume
wood.m = wood.rho * wood.volume

g = vec(0,-9.8,0)

kv = 150
kv_im = kv
t = 0
dt = 0.03
thold = 0.001

#충돌 함수 설정
def collision(pBox,pbox, thold):
    colcheck = (pbox.pos.y - 0.5*pbox.size.y) - (pBox.pos.y - 0.5*pBox.size.y)
    if colcheck < thold:
        return True
    else:
        return False
    
def calc_im(pBox,pbox, kv):
    floatcheck = (pbox.pos.y + 0.5*pbox.size.y) - (pBox.pos.y + 0.5*pBox.size.y)
    
    #print(floatcheck)
    if floatcheck > 0:
        pbox.volume_im = pbox.volume - floatcheck*pbox.size.x*pbox.size.z
    else:
        pbox.volume_im = pbox.volume
    if pbox.volume_im < 0:
        pbox.volume_im = 0
    kv_im = pbox.volume_im/pbox.volume*kv
    return pbox.volume_im, kv_im

scene.waitfor('click')

while t < 100:
    rate(100)
    
    #collision
    if collision(water, wood, thold):
        print("colliding")
        break
    
    wood.volume_im, kv_im = calc_im(water, wood, kv)
    print(wood.volume_im)
    
    #force
    grav = wood.m*g #grvity
    drag = -kv_im*mag(wood.v)**2*norm(wood.v) #drag
    bouy = -water.rho*wood.volume_im*g #buoyancy
    wood.f = grav + bouy + drag
    
    #time integration
    wood.v = wood.v + wood.f/wood.m*dt
    wood.pos = wood.pos + wood.v*dt
    
    #time update
    t = t + dt
    
    #camera
    #scene.center = water.pos+vec(0,0.5*water.size.y,0)
