# scaleconverter 클래스 정의
class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from    # 단위1
        self.units_to = units_to        # 변환할 단위
        self.factor = factor            # 변환 요소(값) - 25

    def convert(self, value):           # 변환 계산 함수
        return self.factor*value        # 변환 값*숫자

sc = ScaleConverter("inches","mm",25)
print("Converting 10 inches")
print(str(sc.convert(10)) + sc.units_to)


