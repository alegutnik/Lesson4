class MyException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


a = 8
try:
    if a * 2 > 10:
        raise MyException("a не може бути більше 10")
    a *= 2
except MyException as e:
    print(e.message)

print(a)

a = 2
try:
    if a * 2 > 10:
        raise MyException("a не може бути більше 10")
    a *= 2
except MyException as e:

    print(e.message)
else:
    print("Усе добре")

print(a)
