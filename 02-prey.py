
#!/usr/bin/env python3
from eye import *
import random
#define SPEED    360
#define ASPEED    45
#define THRES    175
SPEED=360
ASPEED=45
THRES=175
SAFE = 1000
TERUS=200
LCDMenu("GO","","","END")
VWStraight(3500,500)
VWWait()
VWTurn(100, 75)
VWWait()

while (KEYRead() !=KEY4):
    print(PSDGet(1))
    if PSDGet(1)>400:
        VWStraight(300,500)
        VWWait()
        # direc = int ((random.random()-0.2) * 360+random.random())  # [-0.5 .. +0.5] * 360
        # VWTurn(direc, 90)
        # VWWait()

        if PSDGet(1)<SAFE:
            VWStraight(-TERUS,500)
            VWWait()
            VWTurn(-180, 75)
            VWWait()

        elif PSDGet(2)<SAFE:
            VWTurn(-90, 75)
            VWWait()
            VWStraight(TERUS,500)
            VWWait()
            
        elif PSDGet(3)<SAFE:
            VWTurn(90, 75)
            VWWait()
            VWStraight(TERUS,500)
            VWWait()

        elif PSDGet(5)<SAFE:
            VWTurn(-48, 75)
            VWWait()
            VWStraight(TERUS,500)
            VWWait()
            
        elif PSDGet(7)<SAFE:
            VWTurn(-18, 75)
            VWWait()
            VWStraight(TERUS,500)
            VWWait()

        elif PSDGet(6)<SAFE:
            VWTurn(48, 75)
            VWWait()
            VWStraight(TERUS,500)
            VWWait()
            
        elif PSDGet(8)<SAFE:
            VWTurn(18, 75)
            VWWait()
            VWStraight(TERUS,500)
            VWWait()
    else:
        VWStraight(-300,500)
        VWTurn(90, 75)
        VWWait()


 

       
       