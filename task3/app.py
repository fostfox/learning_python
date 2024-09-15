# -----------------------------------------------------------------------------
# 1. Direct Recursion
#    a function calls itself from within itself
# -----------------------------------------------------------------------------

def func1(num: int) -> None:
    if num <= 0:
        return
    print(num, end=' ')
    func1(num - 1)


def func2(num: int) -> None:
    if num <= 0:
        return
    func2(num - 1)
    print(num, end=' ')


def func3(num: int, step: int, max_val: int) -> None:
    if num > max_val:
        return
    print(num, end=' ')
    func3(num + step, step, max_val)


def func4(num: int) -> list:
    if num < 0:
        return []
    test = func4(num - 1)
    test.append(2**num)
    return test


def func5(num: int) -> list:
    if num < 0:
        return []
    test = func5(num - 1)
    test.insert(0, 3**num)
    return test


def calc_factorial(num: int) -> int:
    if num <= 0:
        return 1
    return num * calc_factorial(num - 1)


def calc_fibonacci(num: int) -> int:
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return calc_fibonacci(num - 1) + calc_fibonacci(num - 2)


def func6(arr: list, arr_size) -> 15:
    if arr_size <= 0:
        return 0
    return func6(arr, arr_size - 1) + arr[arr_size - 1]


# -----------------------------------------------------------------------------
# 2. Indirect Recursion
#    more than one function call one another mutually
# -----------------------------------------------------------------------------


def _is_odd(num: int) -> str:
    if num == 0:
        return 'Odd'
    return _is_even(num - 1)


def _is_even(num: int) -> str:
    if num == 0:
        return 'Even'
    return _is_odd(num - 1)


def is_odd_or_even(num: int) -> str:
    return _is_even(abs(num))
