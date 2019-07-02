from vpython import *
#GlowScript 2.7 VPython

a = box(pos = vec(-10,0,0),size = vec(2,1,1), color = color.white)
a.v = vec(1,0,0)

#button Fucntion
def startbtn(b):
    b.disabled = True
    stopbtn.disabled = False
    return b.disabled
    
def stop(b):
    b.disabled = True
    btnStart.disabled = False
    return b.disabled
    
def reset(b):
    # a box's position and velocity intialization
    a.pos = vec(-10,0,0)
    a.v = vec(1,0,0)
    # slide.value intialization
    slide.value = 1
    return b.disabled

#slider Function
def exslider(s):
    return s.value
    
#keyboard input Function
def keyInput(evt):
    # The key value is input by the user's keyboard.
    s = evt.key
    if s == 'w':
        a.pos.y += 1
    elif s == 's':
        a.pos.y -= 1
    elif s == 'r':
        # a box's position and velocity intialization
        a.pos = vec(-10,0,0)
        a.v = vec(1,0,0)
        # slide.value intialization
        slide.value = 1
            
#mouse down Function
def mouseclick(evt):    
    # The evt value is input by the user's mouse.
    a.pos = evt.pos

    
#How to use functions
#1. slider
slide = slider(bind = exslider, min = 0, max = 10,step = 0.1)
# slide value initialization
slide.value = 1
scene.append_to_caption('  velocity\n\n')
        
#2. button
btnStart = button(text = '출발',bind = startbtn)
stopbtn = button(text = '멈추거라!',bind = stop)
resetbtn = button(text = 'reset',bind = reset)

#3. label
exlabel = label(pos = vec(a.pos.x,a.pos.y+1,a.pos.z))

#4. keyboard, mouse
scene.bind('keydown',keyInput)
scene.bind('mousedown',mouseclick)

#5. caption
scene.append_to_caption('\n\t\t\t\t\tw : 위로 한칸\n')
scene.append_to_caption('\t\t\t\t\ts : 아래로 한칸')
scene.append_to_caption('\n\t\t\t\t\tr : 리셋\n')

dt = 0.01

while 1:
    rate(100)
    
    # a box's velocity follows slide.value
    a.v = vec(slide.value,0,0)
    
    #label position update by box's position 
    exlabel.pos = vec(a.pos.x,a.pos.y+1,a.pos.z)
    
    #label can be only string
    exlabel.text = '속도 : ' + str(slide.value)
    
    # if start button is disabled, a box will be moved
    if btnStart.disabled == True:
        a.pos = a.pos + a.v*dt
        
    # if stop buttion is disabled, a box will be stopped
    if stopbtn == True:
        btnStart.disabled = False
    
    