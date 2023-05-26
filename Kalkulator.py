
import numpy as np

# przejscie do folderu Testowanie/MyVent/bin --> dziala komenada source activate--> wyjsc z bin do folderu Testowanie
# uruchamianie testu :  pytest naza pliku  (pytest Kalkulator.py)
class Calc:
    def add(self, a, b):
        return np.add(a, b)

    def subtract(self,a,b):
        return np.subtract(a, b)

    def multiply(self,a,b):
        return np.multiply(a,b)

    def divide(self,a,b):
        return np.divide(a,b)

    def sqrt(self,a):
        return np.sqrt(a)



calc = Calc()
class TestCalc:
    def test_add_method(self):


        assert calc.add(1, 1) == 2
        assert calc.add(0, 3) == 3

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
        assert np.all(calc.divide(np.array([[4, 10, 25], [30,9,6]]),
                                   np.array([[2, 2, 5], [5 ,3 , 2]])) == np.array([2, 5, 5], [6,3,3]))



    def test_sqrt_method(self):
        assert calc.sqrt(9) == 3

        assert np.all( calc.add(np.array([1, 2, 3]), np.array([1, 2, 3])) == np.array([2, 4, 6]))


