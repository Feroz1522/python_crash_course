key = True
engine = False
print("enter start for starting \n stop for stoping \n quit for quiting game")
while key:
    car = input(">> ").lower()
    if car == "start":
        if engine:
            print("vroom.... vrom..... car has been already started")
        else:
            print("engine has been started")
            engine = True
    elif car == "stop":
        if  not engine:
            print("ush..... ush..... car has been already started ")
        else:
            print("car has been stopped")
            engine = False
    elif car == "quit":
        print("exited the game")
        break
