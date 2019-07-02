from vpython import *
#GlowScript 2.7 VPython

#Newton's 3rd law

scale_factor = 10

Earth = sphere(pos = vector(0,0,0), radius = scale_factor*6370000, texture = textures.earth)

r = 3.84e8
Moon = sphere(pos = vector(r,0,0), radius = scale_factor*1737000, color = color.white) 

G = 6.68e-11 ## 만유인력 상수 설정

Earthmass = 5.97e24 # kg
Moonmass = 7.36e22 # kg


F = G*Earthmass*Moonmass/r**2 # 달과 지구의 만유인력

print("Force btn earth and moon = ", F, "N")


Earthacc = F / Earthmass
Moonacc = -F / Moonmass

print("Earthacc = ", Earthacc, "m/s^2")
print("Moonacc = ", Moonacc, "m/s^2")