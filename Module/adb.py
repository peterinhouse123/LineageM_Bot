import subprocess

class ADB:
    def __init__(self,Device_Name):
        self.ADB_Path = "../Tool/adb.exe"
        self.Device_Name = Device_Name



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
    obj.Touch(573,460)
