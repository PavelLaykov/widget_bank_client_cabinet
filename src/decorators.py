from functools import wraps
from typing import Any, Callable


def log(filename: object = None) -> Callable:
    """Декоратор для записи результата в консоль или в указанный файл, если таковой задан"""
    def my_decorator(func) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename is None:
                    print(f"{func.__name__} ok")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                return result
            except Exception as e:
                if filename is None:
                    print(f"{func.__name__} error: {e.__class__.__name__}: {e}. Inputs: {args}, {kwargs}")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}\n")
                raise

        return wrapper

    return my_decorator


if __name__ == "__main__":
    @log(filename="mylog.txt")
    def my_function(x, y):
        """
        Функция суммирует 2 числа и записывает результат в /scr/mylog.txt
        Если не задан файл для записи, то результат будет выведен в консоль
        :param x: первое значение
        :param y: второе значение
        :return: возвращает успешное/не успешное выполнение функции с записью
        в файл /scr/mylog.txt или выведение результата в консоль если файл отсутствует
        """
        return x + y


    qwe = my_function(1, 2)
    # print(qwe)
    # print(my_function.__doc__)
