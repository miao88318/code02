# 对象库层
import time
from selenium.webdriver.common.by import By
from base.mis.base_page import BasePage, BaseHandle
from utils import select_option, DriverUtils


class AduitPage(BasePage):
    def __init__(self):
        super().__init__()
        self.search_ar_box = (By.CSS_SELECTOR, "[placeholder*='输入: 文章']")
        # self.status_checkbox = ()
        self.end_time = (By.CSS_SELECTOR, "[placeholder*='结束']")
        self.search_btn = (By.CSS_SELECTOR, ".find")
        self.aduit_ok = (By.XPATH, "//*[text()='通过']")
        self.submit_btn = (By.CSS_SELECTOR, ".el-button--primary")

    def find_shar_box(self):
        return self.find_elt(self.search_ar_box)
    def find_end_time(self):
        return self.find_elt(self.end_time)
    def find_sh_btn(self):
        return self.find_elt(self.search_btn)
    def find_ad_ok(self):
        return self.find_elt(self.aduit_ok)
    def find_submit_btn(self):
        return self.find_elt(self.submit_btn)

# 操作层
class AduitHandle(BaseHandle):
    def __init__(self):
        self.aduit_page = AduitPage()
    # 输入文章名称的搜索条件
    def input_sr_aritcal(self, text):
        self.input_text(self.aduit_page.find_shar_box(),text)
    # 选择过滤文章的状态
    def check_ar_status(self,status):
        select_option(DriverUtils.get_mis_driver(), "请选择状态",status)

    # 清空搜索发表的结束时间
    def clear_end_time(self):
        self.aduit_page.find_end_time().clear()
    # 查询按钮的点击
    def click_query_btn(self):
        self.aduit_page.find_sh_btn().click()
    # 通过按钮的点击
    def click_ps_btn(self):
        self.aduit_page.find_ad_ok().click()
    # 确定按钮的点击
    def click_sb_btn(self):
        self.aduit_page.find_submit_btn().click()


# 业务层
class AduitProxy:
    def __init__(self):
        self.aduit_handle = AduitHandle()

    def test_aduit_aritcal(self,title):
        # 输入文章名称
        self.aduit_handle.input_sr_aritcal(title)
        # 选择待审核
        self.aduit_handle.check_ar_status("待审核")
        # 清空结束时间
        time.sleep(2)
        self.aduit_handle.clear_end_time()
        # 点击查询按钮
        self.aduit_handle.click_query_btn()
        # 点击文章的通过按钮
        time.sleep(2)
        self.aduit_handle.click_ps_btn()
        # 点击确认通过按钮
        time.sleep(2)
        self.aduit_handle.click_sb_btn()
        # 选择审核通过
        time.sleep(2)
        self.aduit_handle.check_ar_status("审核通过")
        # 点击查询
        time.sleep(2)
        self.aduit_handle.click_query_btn()
        time.sleep(2)

