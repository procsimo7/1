import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_subtraction(self):
        assert self.calc.subtraction(self, 4, 2) == 2

    def test_multiply(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_divizion(self):
        assert self.calc.division(self, 4, 2) == 2