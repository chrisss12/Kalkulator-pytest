
import numpy as np
import pytest

# przejscie do folderu Testowanie/MyVent/bin --> dziala komenada source activate--> wyjsc z bin do folderu Testowanie
# uruchamianie testu :  pytest naza pliku  (pytest Kalkulator.py)
class Calc:
    def add(self, a, b):
        return np.add(a, b)

    def subtract(self, a, b):
        return np.subtract(a, b)

    def multiply(self, a, b):
        return np.multiply(a, b)

    def divide(self, a, b):
        return np.divide(a, b)

    def sqrt(self, a):
        return np.sqrt(a)

    def power(self, a, b):
        return np.power(a, b)

    def log(self, x):
        '''y = ln x  -- >  x = e^y '''
        return np.log(x)
#     y = ln x





calc = Calc()
class TestCalc:
    

    @pytest.mark.parametrize(
        "x,y,results",
        [
            (2,2,4),
            (1,3,4),
            (10,25,35),
            (1.5,1.5,3)
        ]
    )
    def test_add_method(self,x,y,results):
        assert calc.add(x,y) == results

    def test_sub_method(self):
        assert calc.subtract(4,3) == 1
        assert calc.subtract(10,5) == 5
        assert np.all(calc.subtract(np.array([4, 2, 1]), np.array([1, 1, 1])) == np.array([3, 1, 0]))

    def test_multiply_method(self):
        assert calc.multiply(2,3) == 6
        assert calc.multiply(1,5) == 5
        assert np.all(calc.multiply(np.array([4, 2, 1]), np.array([1, 1, 1])) == np.array([4, 2, 1]))

    def test_divide_method(self):
        assert calc.divide(8,4) == 2
        assert calc.divide(2,4) == 0.5
        assert np.all(calc.divide(np.array([4, 10, 25]),
                                   np.array([2, 2, 5]) == np.array([2, 5, 5])))


    def test_sqrt_method(self):
        assert calc.sqrt(9) == 3
        assert calc.sqrt(64) == 8
        assert np.all( calc.sqrt(np.array([25, 9, 81])) == np.array([5, 3, 9]))

    def test_power_method(self):
        assert calc.power(3, 3) == 27
        assert calc.power(2, 3) == 8
        assert np.all(calc.power(np.array([1, 2, 3]),np.array([2, 2, 2])) == np.array([1, 4, 9]))

    def test_log_method(self):
        assert calc.log(1) == 0
        assert calc.log(np.e) == 1
        assert calc.log(np.e**2) == 2
        assert np.all(calc.log(np.array([1, np.e, np.e**2]) == np.array([0.,   1.,   2.])))

