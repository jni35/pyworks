#2
from ex.calculator import Calculator

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
        return self.value

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)
