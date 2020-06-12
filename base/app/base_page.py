# 对象库层的基类
from utils import DriverUtils


class BasePage:
    def __init__(self):
        # 获取移动端驱动对象
        self.driver = DriverUtils.get_app_driver()

    # 公用元素定位的方法
    def find_elt(self, location):
        return self.driver.find_element(*location)


# 操作层的基类
class BaseHandle:
    # 公用模拟输入的方法
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)

