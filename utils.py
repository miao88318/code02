# 获取浏览器驱动的工具类
import json
import selenium.webdriver
import appium.webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import BASE_PATH


def build_data():
    result_data = []
    with open(BASE_PATH + "/data/mp_login_data.json",encoding="utf-8")as f:
        json_str = json.load(f)
        for case_data in json_str.values():
            result_data.append(list(case_data.values()))
    return result_data


def select_option(driver,channel_element, option):
    # 点击选项栏
    xpath = "//*[contains(@placeholder,'{}')]".format(channel_element)
    driver.find_element_by_xpath(xpath).click()
    # 获取所有的选项的元素对象
    option_list = driver.find_elements_by_css_selector(".el-select-dropdown__item span")
    is_element = False
    for i in option_list:
        if i.text == option:
            i.click()
            is_element = True
            break
        else:
            ActionChains(driver).move_to_element(i).send_keys(Keys.DOWN).perform()
            is_element = False
    if is_element is False:
        NoSuchElementException("can't find {} option".format(option))


# 根据文本判断元素是否存在的公用函数
def element_is_exist(driver, attr=None, text=None):
    if attr is None:
    # 定义找元素xpath的表达式
        xpath = "//*[contains(text(),'{}')]".format(text)
    else:
        xpath = "//*[contains(@{},'{}')]".format(attr, text)
    try:
        # 根据xpath表达式去查找操作之后页面是的该元素
        element = driver.find_element(By.XPATH, xpath)
        # 如果找的到则返回不为空
        return element is not None
        # 如果找不到则返回False
    except Exception as e:
        print("NoSuchElement text is {} element".format(text))
        return False


class DriverUtils:
    # MP 自媒体
    __mp_driver = None
    # MIS 后台管理系统
    __mis_driver = None
    # APP 移动端
    __app_driver = None
    # MP开关
    __mp_key = True

    __mis_key = True

    # 修改mp开关的方法
    @classmethod
    def change_mp_key(cls, key):
        cls.__mp_key = key

    # 获取自媒体浏览器驱动
    @classmethod
    def get_mp_driver(cls):
        if cls.__mp_driver is None:
            cls.__mp_driver = selenium.webdriver.Chrome()
            cls.__mp_driver.maximize_window()
            cls.__mp_driver.implicitly_wait(30)
            cls.__mp_driver.get("http://ttmp.research.itcast.cn/")
        return cls.__mp_driver

    # 关闭自媒体浏览器驱动
    @classmethod
    def quit_mp_driver(cls):
        if cls.__mp_driver is not None and cls.__mp_key:
            cls.__mp_driver.quit()
            cls.__mp_driver = None

    # 获取后台管理系统浏览器驱动
    @classmethod
    def get_mis_driver(cls):
        if cls.__mis_driver is None:
            cls.__mis_driver = selenium.webdriver.Chrome()
            cls.__mis_driver.maximize_window()
            cls.__mis_driver.implicitly_wait(30)
            cls.__mis_driver.get("http://ttmis.research.itcast.cn/")
        return cls.__mis_driver

    @classmethod
    def change_mis_key(cls, key):
        cls.__mis_key = key

    # 关闭后台管理系统浏览器驱动
    @classmethod
    def quit_mis_driver(cls):
        if cls.__mis_driver is not None and cls.__mis_key:
            cls.__mis_driver.quit()
            cls.__mis_driver = None

    # 获取移动端驱动
    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            cap = {
                "platformName": "Android",
                "deviceName": "emulator",
                "appPackage": "com.itcast.toutiaoApp",
                "appActivity": ".MainActivity",
                "noReset": True
            }
            cls.__app_driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)
            cls.__app_driver.implicitly_wait(30)
        return cls.__app_driver

    # 关闭移动端驱动
    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver is not None:
            cls.__app_driver.quit()
            cls.__app_driver = None
