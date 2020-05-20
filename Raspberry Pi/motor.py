# 3M Land-It Dispense Functions
# by: Ebenezer Dadson 1/9/2020

import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from multiprocessing import Process as mp
from detect import senseDistance


# Initialize Motor Hat
kit = MotorKit()
kit.stepper1.release()
kit.motor3.throttle = None
forwardMovement = 730 # Move to the end of the rail
backstep = 400 # A little less than length of a post-it note
backwardMovement = 2*forwardMovement - backstep # has to be double the forward movement
throttle1 = -0.35 # throttle of first roller stage (Pick up top note)
throttle2 = -0.4 # throttle of second roller stage (Peel note off pad)


# Stepper motor movements
def trayForward():
    for i in range(forwardMovement):
        kit.stepper1.onestep(direction=stepper.FORWARD, style = stepper.DOUBLE)
    return trayForward

def trayBackward():
    # We found moving the rail back a bit after picking up the top note for some extra slack 
    # helped prevent double dispensation. It can also angle the note to dispense at an
    # angle that is less likely to get stuck in the rollers.
    for i in range(backstep):
        kit.stepper1.onestep(direction=stepper.BACKWARD, style = stepper.DOUBLE)

    # Wait for note to be peeled off pad    
    time.sleep(3)

    # Move actuator back to starting position
    for i in range(backwardMovement):
        kit.stepper1.onestep(direction=stepper.BACKWARD, style = stepper.DOUBLE)
    return trayBackward

# Roller motor movements
def rollerStage1():
    time.sleep(1.5) # Wait for actuator to be near the wall
    print('Roller starting!')
    kit.motor3.throttle = throttle1

    # Sensor waits for top note to be pulled high enough to be dispensed, 
    # but not too high to prevent double dispensation.
    # distance is measured in mm, 
    # when the distance drops we know the note is in front of the sensor.
    distance = 100 # relative distance from sensor to wall
    while(distance > 80):
        distance = senseDistance()
        print(distance)
        time.sleep(0.1)
    # Depending on where the sensor is located, you may want to roll a little longer,
    # We found our sensor position did not need this.
    #time.sleep(0.15)

    # Release motor
    kit.motor3.throttle = None
    return rollerStage1

def rollerStage2():
    # Wait for actuator to be moved back a bit
    time.sleep(2)
    print('Rolling...')
    kit.motor3.throttle = throttle2 #-0.4 was required if rollers had tape.
    time.sleep(3)
    # Release motor
    kit.motor3.throttle = None
    return rollerStage2

# Stages
def motorStage2():
    stage2_1 = mp(target = trayForward)
    stage2_2 = mp(target = rollerStage1)
    stage2_1.start()
    stage2_2.start()
    # Concurrency
    stage2_1.join()
    stage2_2.join()
    return stage2

def motorStage3():
    stage3_1 = mp(target = trayBackward)
    stage3_2 = mp(target = rollerStage2)  
    stage3_1.start()
    stage3_2.start()
    # Concurrency
    stage3_1.join()
    stage3_2.join()
    return stage3

