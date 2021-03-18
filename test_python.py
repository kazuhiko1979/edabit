import calc
import pytest


class TestClass(object):

    string = 'Hello'

    def setup(self):
        self.string = 'Hello'

    def teardown(self):
        pass

    def test_calc(self):
        assert calc.func(4) == 5

    @pytest.mark.skipif("True")
    def test_in(self):
        assert 'H' in self.string

    def test_exception(self):
        with pytest.raises(ValueError):
            raise ValueError()