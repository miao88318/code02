from page.app.index_page import IndexProxy
from utils import DriverUtils, element_is_exist


class TestQueryAritcal:
    def setup_class(self):
        self.driver = DriverUtils.get_app_driver()
        self.index_proxy = IndexProxy()

    def test_qy_ar_by_channel(self):
        channel_name = "linux"
        self.index_proxy.test_query_channel(channel_name)
        is_suc = element_is_exist(self.driver,"text", "猜你喜欢")
        assert is_suc

    def teardown_class(self):
        DriverUtils.quit_app_driver()