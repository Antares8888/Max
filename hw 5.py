import colorama


class Shifr:
    def init(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

o = Shifr()
l = []
print(dir(l))
print(dir(o))
print(hasattr(o, 'num2'))
print(callable(colorama.colorama_text()))
print(dir(colorama.AnsiToWin32))
