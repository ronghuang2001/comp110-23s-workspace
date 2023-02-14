"""Example functions to learn definition and calling syntax"""
def my_max(number1: int, number2: int) -> int:
    """returns max value out of two numbers"""
    if number1 >= number2:
        return number1
    else:  # number1 < number2
        return number2


max_number: int = my_max(1,10)
print(max_number)
Other_max_number: int = my_max(11,3)
print(Other_max_number)
