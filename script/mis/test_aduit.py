import time

import pytest

from config import BASE_ARITCAL_TITLE
from page.mis.aduit_page import AduitProxy
from page.mis.home_page import HomeProxy
from utils import DriverUtils, element_is_exist


@pytest.mark.run(order=103)
class TestAduit:
    def setup_class(self):
        self.driver = DriverUtils.get_mis_driver()
        self.home_proxy = HomeProxy()
        self.aduit_proxy = AduitProxy()

    def test_aduit_aritcal(self):
        title = BASE_ARITCAL_TITLE
        self.home_proxy.to_aduit_page()
        self.aduit_proxy.test_aduit_aritcal(title)
        time.sleep(2)
        assert element_is_exist(driver=self.driver,text=title)

    def teardown_class(self):
        time.sleep(2)
        DriverUtils.quit_mis_driver()