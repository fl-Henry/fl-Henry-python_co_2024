# #### Install
# pip install selenium-wire
# pip install fake-headers
# pip install webdriver-manager

try:
    from driver_utils import Utilities as SeleniumUtils
    from driver_initialization import Initializer, webdriver, uc
except ModuleNotFoundError:
    from selenium_lib.driver_utils import Utilities as SeleniumUtils
    from selenium_lib.driver_initialization import Initializer, webdriver, uc


__all__ = ['Initializer', 'SeleniumUtils', 'webdriver', 'uc']