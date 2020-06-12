from utils import DriverUtils
import pytest


@pytest.mark.run(order=199)
class TestEnd:
    def test_end(self):
        DriverUtils.change_mis_key(True)
        DriverUtils.quit_mis_driver()