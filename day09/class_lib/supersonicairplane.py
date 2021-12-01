# supersonicairplane 클래스 정의

from day09.class_lib.airplane import AirPlane

class SuperSonicAirPlane(AirPlane):
    NORMAL = 1      #클래스 상수(대문자로 표기)
    SUPERSONIC = 2

    def __init__(self):
        self.fly_mode = SuperSonicAirPlane.NORMAL       #맴버-비행모드

    def fly(self):
        if self.fly_mode == SuperSonicAirPlane.SUPERSONIC:
            print("비행기가 초고속으로 비행합니다.")
        else:   #fly_mode == NORMAL
            super().fly()
