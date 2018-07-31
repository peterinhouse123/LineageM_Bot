import subprocess
from PIL import ImageGrab
import numpy as np
import win32gui, win32ui, win32con, win32api
from threading import Thread
import time

class ADB:
    def __init__(self,Device_Name):
        self.ADB_Path = "../Tool/adb.exe"
        self.Device_Name = Device_Name
        self.LD_Path = r"D:\NOXGAMES\MOMO\\"
        self.Hwnd = 0
        self.ScreenHot = None

    def Keep_Game_ScreenHot(self,Emu_Index,file_name):
        th = Thread(target=self.Keep_Game_ScreenHot_fn,args=[Emu_Index,file_name])
        th.start()


    def Keep_Game_ScreenHot_fn(self,Emu_Index,file_name):
        self.Hwnd = self.Get_Self_Hawd(Emu_Index)

        while 1:
            self.window_capture(hwnd=self.Hwnd,filename=file_name)
            time.sleep(1)

    def Get_Self_Hawd(self,Index_Num):
        Device_List = self.LD_Call()

        for k, Device_Data in enumerate(Device_List):
            if k != Index_Num:
                continue
            hawd = Device_Data[3]
            return hawd

    def Get_Rect_Img(self,x1,y1,x2,y2):
        pass

    def LD_Call(self):
        File_Path = self.LD_Path + "ldconsole.exe"
        output = subprocess.Popen([File_Path,'list2'],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

        end = []
        for line in output.stdout.readlines():
            output = line.decode('BIG5')
            output = output.strip()
            if output != "":
                output = output.split(",")
                end.append(output)
        return end

    def window_capture(self,hwnd,filename):
        game_rect = win32gui.GetWindowRect(int(hwnd))
        src_image = ImageGrab.grab(game_rect)
        src_image.save(filename)
        self.ScreenHot = src_image
        # print(type(src_image))

    def Touch(self,x,y,device_name=None):
        if device_name == None:
            device_name = self.Device_Name
        x = str(x)
        y = str(y)
        self.adb_call(device_name,['shell','input','tap',x,y])

    def adb_call(self,device_name,detail_list):
        command = [self.ADB_Path,'-s',device_name]
        for order in detail_list:
            command.append(order)
        print(command)
        subprocess.Popen(command)



if __name__ == '__main__':
    obj = ADB(Device_Name="127.0.0.1:5555")
    # obj.Touch(573,460)
    hawd = obj.Get_Self_Hawd(0)

    obj.window_capture(hawd,'test.png')
    # obj.LD_Call()