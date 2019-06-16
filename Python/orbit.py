from vpython import *
#GlowScript 2.7 VPython

scene = display(title = 'orbit', width = 800, height = 800,range = vec(25000,25000,25000), center = vec(1000,0,0))
scene.autoscale = True

#sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune 설정 

sun = sphere(pos = vec(0,0,0),radius = 100,color=color.yellow,mass=10)

mercury = sphere(pos = vec(200.,0,0),radius = 50,color =color.red)
mercury.trail = curve(color=mercury.color)
mercury.velocity=vector(0,0,295)

venus = sphere(pos = vec(373.664,0,0),radius = 50,color = color.orange)
venus.trail = curve(color=venus.color)
venus.velocity = vector(0,0,225)

earth = sphere(pos = vec(516.664,0,0),radius = 50,mass=2)
earth.trail = curve(color=color.yellow)
earth.velocity = vector(0,0,195)

mars = sphere(pos = vec(787.222,0,0),radius = 50,color=color.green)
mars.trail = curve(color=mars.color)
mars.velocity = vector(0,0,155)

jupiter = sphere(pos = vec(2688.068,0,0),radius = 75,color=color.cyan)
jupiter.trail = curve(color=jupiter.color)
jupiter.velocity = vector(0,0,70)

saturn = sphere(pos = vec(4920.048,0,0),radius = 75,color=color.blue)
saturn.trail = curve(color=saturn.color)
saturn.velocity = vector(0,0,50)

uranus = sphere(pos = vec(9924.19,0,0),radius = 75,color=color.magenta)
uranus.trail = curve(color=uranus.color)
uranus.velocity = vector(0,0,30)

neptune = sphere(pos = vec(15544.811,0,0),radius = 75,color=color.red)
neptune.trail = curve(color=neptune.color)
neptune.velocity = vector(0,0,23)

G = -6.7*10**-4 #증력가속도 설정 # 태양계 행성 질량 설정 
m_sun = 2*10**10
m_mercury = 3.29*10**3
m_venus = 4.87*10**4
m_earth = 6.0*10**4
m_moon = 7.35*10**2
m_mars = 6.39*10**3
m_jupiter = 1.90*10**7
m_saturn = 5.68*10**6
m_uranus = 8.68*10**5
m_neptune = 1.02*10**6

t = 0
dt = 0.01

while True:
    rate(100)
    
    mercury.trail.append(pos = mercury.pos)
    distanceMercury = mag(mercury.pos)
    UnitVectorMercury = (mercury.pos - sun.pos)/distanceMercury
    FgravMercury = (G*m_sun*m_mercury*UnitVectorMercury)/distanceMercury**2
    mercury.velocity = mercury.velocity + (FgravMercury/m_mercury)*dt
    mercury.pos = mercury.pos + mercury.velocity*dt
    mercury.rotate(angle = radians(10),axis = vec(0,1,0))
    
    if distanceMercury <= sun.radius: break

    venus.trail.append(pos = venus.pos)
    distanceVenus = mag(venus.pos)
    UnitVectorVenus = (venus.pos - sun.pos)/distanceVenus
    FgravVenus = (G*m_sun*m_venus*UnitVectorVenus)/distanceVenus**2
    venus.velocity = venus.velocity + (FgravVenus/m_venus)*dt
    venus.pos = venus.pos + venus.velocity*dt
    venus.rotate(angle = radians(20),axis = vec(0,1,0))
    
    if distanceVenus <= sun.radius: break

    earth.trail.append(pos = earth.pos)
    distanceEarth = mag(earth.pos)
    UnitVectorEarth = (earth.pos - sun.pos)/distanceEarth
    FgravEarth = (G*m_sun*m_earth*UnitVectorEarth)/distanceEarth**2
    earth.velocity = earth.velocity + (FgravEarth/m_earth)*dt
    earth.pos = earth.pos + earth.velocity*dt
    earth.rotate(angle = radians(30),axis = vec(0,1,0))
    
    if distanceEarth <= sun.radius: break

    mars.trail.append(pos = mars.pos)
    distanceMars = mag(mars.pos)
    UnitVectorMars = (mars.pos - sun.pos)/distanceMars
    FgravMars = (G*m_sun*m_mars*UnitVectorMars)/distanceMars**2
    mars.velocity = mars.velocity + (FgravMars/m_mars)*dt
    mars.pos = mars.pos + mars.velocity*dt
    mars.rotate(angle = radians(15),axis = vec(0,1,0))
    
    if distanceMars <= sun.radius: break

    jupiter.trail.append(pos = jupiter.pos)
    distanceJupiter = mag(jupiter.pos)
    UnitVectorJupiter = (jupiter.pos - sun.pos)/distanceJupiter
    FgravJupiter = (G*m_sun*m_jupiter*UnitVectorJupiter)/distanceJupiter**2
    jupiter.velocity = jupiter.velocity + (FgravJupiter/m_jupiter)*dt
    jupiter.pos = jupiter.pos + jupiter.velocity*dt
    jupiter.rotate(angle = radians(15),axis = vec(0,1,0))
    
    if distanceMars <= sun.radius: break

    saturn.trail.append(pos = saturn.pos)
    distanceSaturn = mag(saturn.pos)
    UnitVectorSaturn = (saturn.pos - sun.pos)/distanceSaturn
    FgravSaturn = (G*m_sun*m_saturn*UnitVectorSaturn)/distanceSaturn**2
    saturn.velocity = saturn.velocity + (FgravSaturn/m_saturn)*dt
    saturn.pos = saturn.pos + saturn.velocity*dt
    saturn.rotate(angle = radians(15),axis = vec(0,1,0))
    
    if distanceSaturn <= sun.radius: break

    uranus.trail.append(pos = uranus.pos)
    distanceUranus = mag(uranus.pos)
    UnitVectorUranus = (uranus.pos - sun.pos)/distanceUranus
    FgravUranus = (G*m_sun*m_uranus*UnitVectorUranus)/distanceUranus**2
    uranus.velocity = uranus.velocity + (FgravUranus/m_uranus)*dt
    uranus.pos = uranus.pos + uranus.velocity*dt
    uranus.rotate(angle = radians(15),axis = vec(0,1,0))
    
    if distanceUranus <= sun.radius: break

    neptune.trail.append(pos = neptune.pos)
    distanceNeptune = mag(neptune.pos)
    UnitVectorNeptune = (neptune.pos - sun.pos)/distanceNeptune
    FgravNeptune = (G*m_sun*m_neptune*UnitVectorNeptune)/distanceNeptune**2
    neptune.velocity = neptune.velocity + (FgravNeptune/m_neptune)*dt
    neptune.pos = neptune.pos + neptune.velocity*dt
    neptune.rotate(angle = radians(15),axis = vec(0,1,0))
    
    if distanceUranus <= sun.radius: break

    t = t + dt
    

