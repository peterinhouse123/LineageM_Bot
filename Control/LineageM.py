from Module import  adb
import time

class LM:
    def __init__(self,Device_Name):
       self.ADB = adb.ADB(Device_Name=Device_Name)

    def Click_System_Btn(self,name):
        Btn_Map = {}
        Btn_Map['F1'] = [544, 637]
        Btn_Map['F2'] = [620, 637]
        Btn_Map['F3'] = [706, 637]
        Btn_Map['F4'] = [784, 637]
        Btn_Map['F5'] = [960, 637]
        Btn_Map['F6'] = [1047, 637]
        Btn_Map['F7'] = [1125, 637]
        Btn_Map['F8'] = [1203, 637]
        Btn_Map['Auto'] = [970, 512]
        Btn_Map['Self'] = [1060, 402]
        Btn_Map['Pick_up'] = [1168, 429]
        Btn_Map['Attack'] = [1104, 520]
        Btn_Map['Store'] = [935, 45]
        Btn_Map['Item_Box'] = [1009, 45]
        Btn_Map['Skill'] = [1080, 45]
        Btn_Map['Mission'] = [1161, 45]
        Btn_Map['Mission_Close_Menu'] = [1237, 45]
        Btn_Map['Menu'] = [1237, 45]

        if name not in Btn_Map:
            print("無此按鍵名稱：{}".format(name))
            return 0

        click_loc = Btn_Map[name]
        self.ADB.Touch(click_loc[0],click_loc[1])



if __name__ == '__main__':
    obj = LM(Device_Name="127.0.0.1:5555")
    obj.Click_System_Btn('Menu')
    time.sleep(0.2)

    # obj.Click_System_Btn('Item_Box')
    # time.sleep(0.2)
    # obj.Click_System_Btn('Pick_up')
    # time.sleep(0.2)
    # obj.Click_System_Btn('Attack')

