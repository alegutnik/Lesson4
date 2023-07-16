class Calculator:
    @staticmethod
    def addition(*args):
        Calculator.check_int_or_float_value(args)
        return sum(args)

    @staticmethod
    def subtraction(*args):
        Calculator.check_int_or_float_value(args)
        return args[0] - sum(args[1:])

    @staticmethod
    def multiplication(*args):
        Calculator.check_int_or_float_value(args)
        total = 1
        for value in args:
            total *= value
        return total

    @staticmethod
    def division(*args):
        Calculator.check_int_or_float_value(args)
        Calculator.zero_divide_by_zero(args)
        total = args[0]
        for value in args[1:]:
            total /= value
        return total

    @staticmethod
    def exponentiation(*args):
        Calculator.check_int_or_float_value(args)
        Calculator.exponentiation_negative_zero(args)
        total = args[0]
        for value in args[1:]:
            total **= value
        return total

    @staticmethod
    def check_int_or_float_value(values):
        for value in values:
            if not (isinstance(value, float) or isinstance(value, int)):
                raise TypeError(
                    f"Не коретний тип данних ({value}). Введіть або ціле число, або число з плаваючою крапкою")

    @staticmethod
    def zero_divide_by_zero(args):
        if 0 in args:
            raise ValueError("На нуль ділити не можна!")

    @staticmethod
    def exponentiation_negative_zero(args):
        if args[0] == 0:
            for i in args[1:]:
                if i<0:
                    raise ValueError("0 не можна в негативний ступінь")


calculator = Calculator()
# addition
print(calculator.addition(1, 2, 3, 2.3))
# print(calculator.addition(1, 2, 3, 2.3, "123")) #Помилка не правильний тип данних

# subtraction
print(calculator.subtraction(5, 7, 2, 5))
# print(calculator.subtraction(5, 7, 2, 5, [1, 2, 3]))  # Помилка не правильний тип данних

# multiplication
print(calculator.multiplication(2, 3, 2))
# print(calculator.multiplication(2, 3, 2, ("выавыа")))  # Помилка не правильний тип данних

# division
print(calculator.division(12, 3, 2))
# print(calculator.division(12, 3, 2, ("выавыа")))  # Помилка не правильний тип данних
# print(calculator.division(12, 2, 0))  # Помилка на нуль ділити не можна
#
print(calculator.exponentiation(0, 3, 2))
# print(calculator.exponentiation(12, 3, 2, ("выавыа")))  # Помилка не правильний тип данних
# print(calculator.exponentiation(0, -3, 2))  # Помилка 0 в від'ємний ступінь
