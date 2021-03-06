import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

lightstate = [[1,0,0],[1,0,0],[1,0,0],[1,0,0]]
pin = [[3,5,7],[8,10,11],[12,13,15],[16,18,19]]

for i in range(0,len(pin)):
    for j in range(0,3):
        GPIO.setup(pin[i][j], GPIO.OUT, initial=GPIO.LOW)

def control(veh):
    maxlim = 120
    minlim = 0
    avgtime = 6
    lanes = 1
    ways = len(veh) #no of lanes
    times = []
    for i in range(0,ways):
        time = (veh[i]*avgtime)/lanes
        print time
        if time>maxlim: 
            allotime = maxlim
        elif time<minlim:
            allotime=minlim
        else:
            allotime=time
        times.append(allotime)
    return times

def setlight(listate,pino):
    for i in range(0,len(pino)):
        for j in range(0,3):
            if listate[i][j] == 1:
                GPIO.output(pino[i][j], GPIO.HIGH)
            else:
                GPIO.output(pino[i][j], GPIO.LOW)
                

def blink():
    lightstate = [[1,0,0],[0,1,0],[1,0,0],[0,1,0]]
    setlight(lightstate,pin)
    time.sleep(1)
    lightstate = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    setlight(lightstate,pin)
    time.sleep(1)
    

def light(state):
    for i in range(0,len(state)):
        if state[i] == 2:
            lightstate[i] = [0,0,1]
        elif state[i] == 1:
            lightstate[i] = [0,1,0]
        elif state[i] == 3:
            blink()
            break
        else:
            lightstate[i] = [1,0,0]
        print lightstate
        setlight(lightstate,pin)
