# 自媒体主页
# 自媒体登录页面
from selenium.webdriver.common.by import By
from base.mp.base_page import BasePage, BaseHandle


# 对象库层
class HomePage(BasePage):
    # 定义初始化方法
    def __init__(self):
        super().__init__()
        # 将所需要操作的元素定义一个对象的实例属性
        # 实例属性存储元素定位方式以及对应值
        self.content_manager = (By.XPATH,"//*[text()='内容管理']")
        self.publish_artical = (By.XPATH,"//*[contains(text(),'发布文章')]")

    # 定义找到所有元素实例方法
    def find_content_manager(self):
        return self.find_elt(self.content_manager)

    def find_publish_artical(self):
        return self.find_elt(self.publish_artical)


# 操作层
class HomeHandle(BaseHandle):
    def __init__(self):
        self.home_page = HomePage()

    def click_content_manager(self):
        self.home_page.find_content_manager().click()

    def click_publish_artical(self):
        self.home_page.find_publish_artical().click()


# 业务层
class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    def to_publish_page(self):
        self.home_handle.click_content_manager()
        self.home_handle.click_publish_artical()


