
#!/usr/bin/env python3
from eye import *
import random
#define SPEED    360
#define ASPEED    45
#define THRES    175
SPEED=360
TERUS=200
THRES=175
SAFE = 2000
LCDMenu("GO","","","END")
VWStraight(3500,500)
VWWait()
while (KEYRead() !=KEY4):


    if PSDGet(1)<SAFE:
      VWStraight(TERUS,500)
      VWWait()
    elif PSDGet(2)<SAFE:
      VWTurn(90, 75)
      VWWait()
      VWStraight(TERUS,500)
      VWWait()
    
    elif PSDGet(3)<SAFE:
      VWTurn(-90, 75)
      VWWait()
      VWStraight(TERUS,500)
      VWWait()

    elif PSDGet(5)<SAFE:
      VWTurn(48, 75)
      VWWait()
      VWStraight(TERUS,500)
      VWWait()
    
    elif PSDGet(7)<SAFE:
      VWTurn(18, 75)
      VWWait()
      VWStraight(TERUS,500)
      VWWait()

    elif PSDGet(6)<SAFE:
      VWTurn(-48, 75)
      VWWait()
      VWStraight(TERUS,500)
      VWWait()
    
    
    elif PSDGet(8)<SAFE:
      VWTurn(-18, 75)
      VWWait()
      VWStraight(TERUS,500)
      VWWait()
    # else:
    #   VWTurn(-25, 75)
    #   VWWait()

    


    # if PSDGet(7)<200:
    #   VWStraight(50,500)





    # if PSDGet(1)>200:
    #     #VWStraight(200,500)
    #     VWWait()
    #     OSWait(1000)
    # else:
    #     depan = int(PSDGet(1))
    #     VWWait()
    #     if PSDGet(1)<depan:
    #       VWStraight(50,500)
    #     else:
    #       VWTurn(180, 75)

    #     VWStraight(-200,500)
    #     VWTurn(190, 75)
    #     VWWait()

    # VWStraight(50,250)
    #   if PSDGet(1)<100:
    #     depan = int(PSDGet(1))
    #     VWWait()
    #     if PSDGet(1)<depan:
    #       VWStraight(50,500)
    #     else:
    #       VWTurn(180, 75)



    # while(PSDGet(1)!=0):
    #   if PSDGet(1)


    # if (PSDGet(1)>SAFE and PSDGet(2)>SAFE and PSDGet(3)>SAFE and PSDGet(4)>SAFE and PSDGet(5)>SAFE and PSDGet(6)>SAFE and PSDGet(7)>SAFE and PSDGet(8)>SAFE): 
    #   LCDPrintf("straight\n", "")
    #   #VWStraight(50,250)  # not required to wait

    # else:
    #    VWWait()
