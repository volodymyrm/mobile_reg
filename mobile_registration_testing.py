__author__ = 'volodymyrm'
import random
import link
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class registration_page:
    def __init__(self,link):
        self.driver = webdriver.Firefox()
        self.driver.get(link)
        self.first_name = fName(self.driver)
        self.last_name = lName(self.driver)
        self.email = eMail(self.driver)
        self.phone_number = pNumber(self.driver)
        self.address = aDdress(self.driver)
        self.city = cIty(self.driver)
        self.zip = zIp(self.driver)
        self.username = userName(self.driver)
        self.password = passWord(self.driver)

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

class eMail:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_email")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='email']/div[@class='error_msg']")

class pNumber:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_phone_number")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='phone_number']/div[@class='error_msg']")

class aDdress:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_address")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='address']/div[@class='error_msg']")

class cIty:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_city")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='city']/div[@class='error_msg']")

class zIp:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_zip")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='zip']/div[@class='error_msg']")

class userName:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_username")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='username']/div[@class='error_msg']")

class passWord:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_password")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='password']/div[@class='error_msg']")

class passwordConfirm:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_password_confirm")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='password_retype']/div[@class='error_msg']")

class regButton:
    def __init__(self, driver):
        self.Button = driver.find_element_by_xpath("//div[@class='reg_btn']")

class regForm:
    def __init__(self, driver):
        self.emptyField = driver.find_element_by_class_name("form_box_title")

    def click(self):
        self.emptyField.send_keys(Keys.ARROW_DOWN)

#######################         RUNNING TESTS           #####################

class EG_mobile(unittest.TestCase):

    eg = registration_page(link.lnk)

    error_msg_mandatory = "This field is mandatory"
    error_msg_name_valid = "Please only use letters (a-z) and characters (,-.)"
    error_msg_name_long = "First name should have 1-50 characters"
    error_msg_last_name_long = "Last name should have 1-50 characters"

    error_msg_email_valid = "Please enter a valid e-mail, using letters (a-z), numbers (0-9) and characters (._-@)"

    error_msg_address_valid = "Please use only letters (a-z), numbers (0-9) and characters (,-'/#&)"
    error_msg_address_long = "Address should have 2-160 characters"

    error_msg_city_valid  = "Please enter your city using letters (a-z), numbers (0-9) and characters (.-')"

    error_msg_zip_valid = "Please enter your postal code using letters (a-z), numbers (0-9) and characters (_-/)"
    error_msg_zip_long = "Postal code should have 1-12 characters"

    error_msg_phone_valid = "Please enter your mobile phone number (10-20 digits)"
    error_msg_username_valid = "Please select a username using letters, numbers and characters (.-_@). 5-16 characters long"
    error_msg_password_valid = "Please choose a password 5-10 characters long, using letters (a-z) and numbers (0-9) only"
    error_msg_password_confirm_valid = "Please choose a password 5-10 characters long, using letters (a-z) and numbers (0-9) only"

    population1 = "!@$%^&*=+"
    population2 = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    population3 = "1234567890"
    random_invalid_name = str("".join(random.sample(population1,3)))+str("".join(random.sample(population2,3)))+str("".join(random.sample(population3,3)))
    random_valid_name = str("".join(random.sample(population2,5)))+str("".join(random.sample(",-.",2)))
    random50 = str("".join(random.sample(population2,50)))
    random160 = str("".join(random.sample(population2,50)))+str("".join(random.sample(population2,50)))+str("".join(random.sample(population2,50)))

    def rand_val(self, pop, len):
        return str("".join(random.sample(pop,len)))

    def setUp(self):
        time.sleep(1)

    def test_invalid_data(self):
        self.eg.first_name.inputField.send_keys(self.random_invalid_name)
        self.eg.last_name.inputField.send_keys(self.random_invalid_name)
        self.eg.email.inputField.send_keys(self.random_invalid_name)

        self.eg.form.click()
        assert self.eg.first_name.errorMsg.text in self.error_msg_name_valid
        assert self.eg.last_name.errorMsg.text in self.error_msg_name_valid
        assert self.eg.email.errorMsg.text in self.error_msg_name_valid


    def tearDown(self):
        time.sleep(2)
        self.eg.close_page()


if __name__ == "__main__":
    unittest.main()

'''
class EG_mobile(unittest.TestCase):





    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("link.lnk")

        self.firstNameField = self.driver.find_element_by_class_name("hook_reg_first_name")
        self.lastNameField = self.driver.find_element_by_class_name("hook_reg_last_name")
        self.emailField = self.driver.find_element_by_class_name("hook_reg_email")
        self.phoneNumberField = self.driver.find_element_by_class_name("hook_reg_phone_number")
        self.addressField = self.driver.find_element_by_class_name("hook_reg_address")
        self.cityField = self.driver.find_element_by_class_name("hook_reg_city")
        self.zipField = self.driver.find_element_by_class_name("hook_reg_zip")
        self.usernameField = self.driver.find_element_by_class_name("hook_reg_username")
        self.passwordField = self.driver.find_element_by_class_name("hook_reg_password")
        self.passwordConfirmField = self.driver.find_element_by_class_name("hook_reg_password_confirm")
        self.regButton = self.driver.find_element_by_xpath("//div[@class='reg_btn']")
        self.form = self.driver.find_element_by_class_name("form_box_title")

        self.firstName_error = self.driver.find_element_by_xpath("//div[@id='first_name']/div[@class='error_msg']")
        self.lastName_error = self.driver.find_element_by_xpath("//div[@id='last_name']/div[@class='error_msg']")
        self.email_error = self.driver.find_element_by_xpath("//div[@id='email']/div[@class='error_msg']")
        self.phoneNumber_error = self.driver.find_element_by_xpath("//div[@id='phone_number']/div[@class='error_msg']")
        self.address_error = self.driver.find_element_by_xpath("//div[@id='address']/div[@class='error_msg']")
        self.city_error = self.driver.find_element_by_xpath("//div[@id='city']/div[@class='error_msg']")
        self.zip_error = self.driver.find_element_by_xpath("//div[@id='zip']/div[@class='error_msg']")
        self.username_error = self.driver.find_element_by_xpath("//div[@id='username']/div[@class='error_msg']")
        self.password_error = self.driver.find_element_by_xpath("//div[@id='password']/div[@class='error_msg']")
        self.password_confirm_error = self.driver.find_element_by_xpath("//div[@id='password_retype']/div[@class='error_msg']")

    def test_invalid_data(self):
        self.firstNameField.send_keys(self.rand_val(self.population1,4))




        self.lastNameField.send_keys(self.random_invalid_name)
        self.emailField.send_keys(self.random_invalid_name)
        self.phoneNumberField.send_keys(self.random_invalid_name)
        self.addressField.send_keys(self.random_invalid_name)
        self.cityField.send_keys(self.random_invalid_name)
        self.zipField.send_keys(self.random_invalid_name)
        self.usernameField.send_keys(self.random_invalid_name)
        self.passwordField.send_keys(self.random_invalid_name)
        self.passwordConfirmField.send_keys(self.random_invalid_name)

        self.form.send_keys(Keys.ARROW_DOWN)

        assert self.error_msg_name_valid in self.firstName_error.text
        assert self.error_msg_name_valid in self.lastName_error.text
        assert self.error_msg_email_valid in self.email_error.text
        assert self.error_msg_phone_valid in self.phoneNumber_error.text
        assert self.error_msg_address_valid in self.address_error.text
        assert self.error_msg_city_valid in self.city_error.text
        assert self.error_msg_zip_valid in self.zip_error.text
        assert self.error_msg_username_valid in self.username_error.text
        assert self.error_msg_password_valid in self.password_error.text
        assert self.error_msg_password_confirm_valid in self.password_confirm_error.text

    def test_long_data(self):
        self.firstNameField.send_keys(self.random50)
        self.lastNameField.send_keys(self.random50)
        self.addressField.send_keys(self.random160)

    def test_mandatory_field(self):
        self.regButton.click()
        assert self.error_msg_mandatory in self.firstName_error.text
        assert self.error_msg_mandatory in self.lastName_error.text
        assert self.error_msg_mandatory in self.email_error.text
        assert self.error_msg_mandatory in self.phoneNumber_error.text
        assert self.error_msg_mandatory in self.address_error.text
        assert self.error_msg_mandatory in self.city_error.text
        assert self.error_msg_mandatory in self.zip_error.text
        assert self.error_msg_mandatory in self.username_error.text
        assert self.error_msg_mandatory in self.password_error.text

    def tearDown(self):
        time.sleep(5)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
'''