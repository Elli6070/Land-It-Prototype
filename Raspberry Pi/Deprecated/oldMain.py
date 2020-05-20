# 3M Land-It Dispense Instantiation
# by: Ebenezer Dadson 1/9/2020

from time import *
import requests
from motor import *
from draw import drawing



# Web app communication
def comm():
    x = requests.get('http://land-it-prototype.herokuapp.com/')
    global status
    status = x.status_code
    return status

## All packages have been defined above. ##


# Main code
def main():
    # Enable communication
    comm()
    if status == 200:
    # Web app active 
        print('Printing...')
        #drawing()
        print("Start Dispensing...")
        

    # Enable sensor

    ## Stage 1: Quickly move slide into position
    step_detect = 0; roll_detect = 0; 
    if step_detect == 0 and roll_detect == 0:
        print('Moving tray...')
        trayForward()

    ## Stage 2: Move slide until roller triggered
    step_detect = 1; roll_detect = 0
    if step_detect == 1 and roll_detect == 0:
        print('Dispensing...')
        stage2()
        print('Grabbing Post-it..')
            
    ## Stage 3: Dispense with rollers
    step_detect = 1; roll_detect = 1
    if step_detect == 1 and roll_detect == 1:
        print('Homing tray...')
        stage3()
        print('Dispensing Done!')
        print('Thanks for using Post-it!')


if __name__ == '__main__':
    main()