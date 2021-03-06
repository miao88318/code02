from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from base.app.base_page import BasePage, BaseHandle
from utils import DriverUtils


class IndexPage(BasePage):
    def __init__(self):
        super().__init__()
        self.channel_area = (By.XPATH, "//*[@class='android.widget.HorizontalScrollView']")
        self.channel_option = (By.XPATH, "//*[contains(@text,'{}')]")
        self.first_aritcal = (By.XPATH, "//*[contains(@text,'评论')]")

    def find_channel_area(self):
        return self.find_elt(self.channel_area)

    def find_channel_option(self, channel_name):
        return self.driver.find_element(self.channel_option[0], self.channel_option[1].format(channel_name))

    def find_channel_artical(self):
        return self.find_elt(self.first_aritcal)


class IndexHandle(BaseHandle):
    def __init__(self):
        self.index_page = IndexPage()
        self.driver = DriverUtils.get_app_driver()

    def check_channel(self, channel_name):
        area = self.index_page.find_channel_area()
        x = area.location["x"]
        y = area.location["y"]

        w = area.size["width"]
        h = area.size["height"]

        start_x = x + w * 0.5
        start_y = y + h * 0.3

        end_x = x + w * 0.25
        end_y = start_y
        while True:
            page_old = self.driver.page_source
            try:
                self.index_page.find_channel_option(channel_name).click()
                break
            except Exception as e:
                self.driver.swipe(start_x,start_y,end_x,end_y, 500)
                if page_old == self.driver.page_source:
                    raise NoSuchElementException

    def click_first_artical(self):
        self.index_page.find_channel_artical().click()


class IndexProxy:
    def __init__(self):
        self.index_handle = IndexHandle()
    def test_query_channel(self,channel_name):
        self.index_handle.check_channel(channel_name)
        self.index_handle.click_first_artical()