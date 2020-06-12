# 文章发布页面
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.mp.base_page import BasePage, BaseHandle
from utils import DriverUtils, select_option


# 对象库层
class PubPage(BasePage):
    def __init__(self):
        super().__init__()
        self.title = (By.CSS_SELECTOR, "[placeholder='文章名称']")
        self.frame = (By.CSS_SELECTOR, "#publishTinymce_ifr")
        self.aritcal_content = (By.CSS_SELECTOR, "body")
        self.aritcal_cover = (By.XPATH, "//*[text()='自动']")
        self.channel = (By.CSS_SELECTOR,"[placeholder='请选择']")
        self.channel_option = (By.XPATH, "//*[text()='区块链']")
        self.publish_btn = (By.XPATH, "//*[text()='发表']")

    def find_title(self):
        return self.find_elt(self.title)

    def find_frame(self):
        return self.find_elt(self.frame)

    def find_ar_content(self):
        return self.find_elt(self.aritcal_content)

    def find_ar_cover(self):
        return self.find_elt(self.aritcal_cover)

    def find_channel(self):
        return self.find_elt(self.channel)

    def find_ch_option(self):
        return self.find_elt(self.channel_option)

    def find_pb_btn(self):
        return self.find_elt(self.publish_btn)


# 操作层
class PubHandle(BaseHandle):
    def __init__(self):
        self.pub_page = PubPage()
        self.driver = DriverUtils.get_mp_driver()

    def input_title(self, title):
        self.input_text(self.pub_page.find_title(),title)

    def input_content(self, content):
        self.driver.switch_to.frame(self.pub_page.find_frame())
        self.input_text(self.pub_page.find_ar_content(),content)
        self.driver.switch_to.default_content()

    def check_cover(self):
        self.pub_page.find_ar_cover().click()

    def check_channel(self, option):
        # self.pub_page.find_channel().click()
        # self.pub_page.find_ch_option().click()
        select_option(self.driver,"请选择",option)

    def click_publish(self):
        self.pub_page.find_pb_btn().click()


# 业务层
class PubProxy:
    def __init__(self):
        self.pub_handle = PubHandle()

    def test_pub_aritcal(self, title,content, option):
        self.pub_handle.input_title(title)
        self.pub_handle.input_content(content)
        self.pub_handle.check_cover()
        self.pub_handle.check_channel(option)
        self.pub_handle.click_publish()