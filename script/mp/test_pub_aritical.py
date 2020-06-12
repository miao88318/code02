import time
from config import BASE_ARITCAL_TITLE
from page.mp.home_page import HomeProxy
from page.mp.publish_page import PubProxy
from utils import DriverUtils, element_is_exist
import pytest


@pytest.mark.run(order=3)
# 定义测试类
class TestPubAritical:

    # 定义类级别的初始化方法
    def setup_class(self):
        self.driver = DriverUtils.get_mp_driver()
        self.home_proxy = HomeProxy()
        self.pub_proxy = PubProxy()

    # 定义类级别销毁的方法
    def teardown_class(self):
        time.sleep(2)
        DriverUtils.quit_mp_driver()
    # 定义测试方法
    def test_pub_aritical(self):
        # 组织测试数据
        title = BASE_ARITCAL_TITLE
        content = "不用开风扇了,哈哈"
        option = "数码产品"
        # 调用业务层的方法
        self.home_proxy.to_publish_page()
        self.pub_proxy.test_pub_aritcal(title, content,option)
        time.sleep(3)

        # 断言实际结果
        is_suc = element_is_exist(driver=self.driver,text="新增文章成功")
        assert is_suc
