# 3M Land-It Dispense Instantiation
# by: Ebenezer Dadson 1/9/2020

from time import *
import requests
from motor import *
from draw import drawing

# Dispense code
def dispense():
    print("Start Dispensing...")
        
    ## Stage 1: Quickly move slide into position
    print('Moving tray...')
    trayForward()

    ## Stage 2: Move slide until roller triggered
    print('Dispensing...')
    motorStage2()
    print('Grabbing Post-it..')
            
    ## Stage 3: Dispense with rollers
    print('Homing tray...')
    motorStage3()
    print('Dispensing Done!')
    print('Thanks for using Post-it!')


def main():
    op1 = mp(target = dispense)
    op1.start()
    op1.join()



if __name__ == '__main__':
    main()
    kit.stepper1.release()
    kit.motor3.throttle = None