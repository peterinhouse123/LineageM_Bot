from Module import adb
from Control import  LineageM

class Main():
    def __init__(self):
        self.LM = LineageM.LM(Device_Name="127.0.0.1:5555")


    def start(self):
        pass




if __name__ == "__main__":
    obj = Main()
    # obj.start()