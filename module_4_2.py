def test_function():
    def inner_function():
        print('Я в области видимости функции test_funtion')

    inner_function()


test_function()
