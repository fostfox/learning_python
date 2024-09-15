import task3.app as app


def test_func1(capsys):
    app.func1(5)
    captured = capsys.readouterr()
    assert captured.out == "5 4 3 2 1 "


def test_func2(capsys):
    app.func2(5)
    captured = capsys.readouterr()
    assert captured.out == "1 2 3 4 5 "


def test_func3(capsys):
    app.func3(20, 5, 55)
    captured = capsys.readouterr()
    assert captured.out == "20 25 30 35 40 45 50 55 "
    app.func3(34, 5, 55)
    captured = capsys.readouterr()
    assert captured.out == "34 39 44 49 54 "


def test_func4():
    res = app.func4(6)
    assert res == [1, 2, 4, 8, 16, 32, 64]


def test_func5():
    res = app.func5(4)
    assert res == [81, 27, 9, 3, 1]


def test_func_factorial():
    assert app.calc_factorial(7) == 5040


def test_func_fibonacci():
    assert app.calc_fibonacci(15) == 610


def test_func6():
    arr = [1, 2, 3, 4, 5]
    assert app.func6(arr, len(arr)) == 15
