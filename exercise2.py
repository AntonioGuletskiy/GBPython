"""
Задание 3
"""
# def type_logger(function_to_decorate):
#     def wrapper(arg):
#         print(f'{arg}:', type(arg))
#     return wrapper
#
#
# @type_logger
# def cal_cube(x):
#     return x**3
#
# a = cal_cube(5)

""" 
Задание 4
"""
def val_checker(function_to_decorate):
    def wrapper(arg):
        if arg < 0:
            raise ValueError(f"wrong val: {arg}")
        else:
            print(arg**3)
    return wrapper


@val_checker
def cal_cube(x):
    return x**3


cal_cube(5)
