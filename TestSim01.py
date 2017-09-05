import ControllerSimulator

myController = ControllerSimulator.Controller()
myController.send(None)

while True:
    myCntrl = list(myController)
    print (myController)
    print(myCntrl)
    for i in myCntrl:
        print("%.5f\t%d\t%d\t%d" % myCntrl[0], myCntrl[1], myCntrl[2], myCntrl[3])
