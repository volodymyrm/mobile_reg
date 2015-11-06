__author__ = 'volodymyrm'
import random
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class registration_page:
    def __init__(self,link):
        self.driver = webdriver.Firefox()
        self.driver.get(link)
        self.firstName = fName(self.driver)
        self.lastName = lName(self.driver)
        self.form = regForm(self.driver)

    def close_page(self):
        self.driver.close()

class fName:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_first_name")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='first_name']/div[@class='error_msg']")

class lName:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_last_name")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='last_name']/div[@class='error_msg']")

class regForm:
    def __init__(self, driver):
        self.emptyField = driver.find_element_by_class_name("form_box_title")

    def click(self):
        self.emptyField.send_keys(Keys.ARROW_DOWN)

#######################         RUNNING TESTS

class EG_mobile(unittest.TestCase):

    eg = registration_page("!!!!.....LINK...LINK....LINK....!!!!")
    error_msg_name_valid = "Please only use letters (a-z) and characters (,-.)"

    def setUp(self):
        time.sleep(1)

    def test_first_name(self):
        self.eg.firstName.inputField.send_keys("Bla bla bla ***")
        self.eg.lastName.inputField.send_keys("Bla bla bla ***")
        self.eg.form.click()
        assert self.eg.firstName.errorMsg.text in self.error_msg_name_valid
        assert self.eg.lastName.errorMsg.text in self.error_msg_name_valid

    def tearDown(self):
        time.sleep(2)
        self.eg.close_page()


if __name__ == "__main__":
    unittest.main()