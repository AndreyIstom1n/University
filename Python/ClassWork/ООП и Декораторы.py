def log_decorator(func):
    def wrapper(*args,**kwargs):
        print("Вызов функции: ",func.__name__)
        print("Аргументы: ",args, kwargs)
        result =func(*args,**kwargs)
        print("Результат: ",result)
        return result
    return wrapper

def validate_input(func):
    def wrapprt(*args,**kwargs):
        print("Вызов функции: ",func.__name__)
        print("Аргументы: ",args)
        if args >0:
            result=func(*args)
        print("Результат: ",result)
        return result
    return wrapper

@log_decorator
def multiply(a,b):
    return a*b
multiply(3,4)

@validate_input(lambda x:x>0,input("Введите положительное число "))
def calculate_square(x):
    return x*x
calculate_square(5)
calculate_square(-2)
