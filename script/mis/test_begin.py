from utils import DriverUtils
import pytest


@pytest.mark.run(order=101)
class TestBegin:
    def test_begin(self):
        DriverUtils.change_mis_key(False)
