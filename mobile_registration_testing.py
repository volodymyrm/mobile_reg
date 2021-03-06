__author__ = 'volodymyrm'
import random
import link
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class fName:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_first_name")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='first_name']/div[@class='error_msg']")
        self.error_invalid_characters = "Please only use letters (a-z) and characters (,-.)"
        self.error_invalid_length = "First name should have 1-50 characters"
        self.error_empty_data = "This field is mandatory"

class lName:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_last_name")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='last_name']/div[@class='error_msg']")
        self.error_invalid_characters = "Please only use letters (a-z) and characters (,-.)"
        self.error_invalid_length = "Last name should have 1-50 characters"
        self.error_empty_data = "This field is mandatory"


class eMail:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_email")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='email']/div[@class='error_msg']")
        self.error_invalid_characters = "Please enter a valid e-mail, using letters (a-z), numbers (0-9) and characters (._-@)"
        #self.error_invalid_length = THERE IS NO LENGTH LIMITATION
        self.error_empty_data = "This field is mandatory"

class pNumber:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_phone_number")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='phone_number']/div[@class='error_msg']")
        self.error_invalid_characters = "Please enter your mobile phone number (10-20 digits)"
        self.error_invalid_length = "Please enter your mobile phone number (10-20 digits)"
        self.error_empty_data = "This field is mandatory"

class aDdress:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_address")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='address']/div[@class='error_msg']")
        self.error_invalid_characters = "Please use only letters (a-z), numbers (0-9) and characters (,-'/#&)"
        self.error_invalid_length = "Address should have 2-160 characters"
        self.error_empty_data = "This field is mandatory"

class cIty:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_city")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='city']/div[@class='error_msg']")
        self.error_invalid_characters = "Please enter your city using letters (a-z), numbers (0-9) and characters (.-')"
        #self.error_invalid_length = THERE IS NO LENGTH LIMITATION
        self.error_empty_data = "This field is mandatory"

class zIp:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_zip")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='zip']/div[@class='error_msg']")
        self.error_invalid_characters = "Please enter your postal code using letters (a-z), numbers (0-9) and characters (_-/)"
        self.error_invalid_length = "Postal code should have 1-12 characters"
        self.error_empty_data = "This field is mandatory"

class userName:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_username")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='username']/div[@class='error_msg']")
        self.error_invalid_characters = "Please select a username using letters, numbers and characters (.-_@). 5-16 characters long"
        self.error_invalid_length = "Please select a username using letters, numbers and characters (.-_@). 5-16 characters long"
        self.error_empty_data = "This field is mandatory"

class passWord:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_password")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='password']/div[@class='error_msg']")
        self.error_invalid_characters = "Please choose a password 5-10 characters long, using letters (a-z) and numbers (0-9) only"
        self.error_invalid_length = "Please choose a password 5-10 characters long, using letters (a-z) and numbers (0-9) only"
        self.error_empty_data = "This field is mandatory"

class passwordConfirm:
    def __init__(self, driver):
        self.inputField = driver.find_element_by_class_name("hook_reg_password_confirm")
        self.errorMsg = driver.find_element_by_xpath("//div[@id='password_retype']/div[@class='error_msg']")
        self.error_invalid_characters = "Please choose a password 5-10 characters long, using letters (a-z) and numbers (0-9) only"
        self.error_invalid_length = "Please choose a password 5-10 characters long, using letters (a-z) and numbers (0-9) only"
        self.error_empty_data = "This field is mandatory"
        self.error_password_missmatch = "The passwords you typed do not match"

class regButton:
    def __init__(self, driver):
        self.Button = driver.find_element_by_xpath("//div[@class='reg_btn']")

    def click(self):
        self.Button.click()

class regForm:
    def __init__(self, driver):
        self.emptyField = driver.find_element_by_class_name("form_box_title")

    def click(self):
        self.emptyField.send_keys(Keys.ARROW_DOWN)

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
        self.password_confirm = passwordConfirm(self.driver)
        self.form = regForm(self.driver)
        self.button = regButton(self.driver)

#---------------------------------------- RUNNING TESTS----------------------------------------------

class EG_mobile(unittest.TestCase):

    pop1 = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMqwertyuiop"
    pop2 = "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890"
    pop3 = "!@$%^&*=+~!@$%^&*=+~!@$%^&*=+~!@$%^&*=+~!@$%^&*=+~!@$%^&*=+~!@$%^&*=+~!@$%^&*=+~!@$%^&*=+~"

    def rand_val_invalid(self,len):

        if len == 1:
            return str("".join(random.sample(self.pop3,len)))
        else:
            return str("".join(random.sample(self.pop1,int(len/2))) + "".join(random.sample(self.pop3,int(len/2))))

    def rand_val_valid(self,len):
        return str("".join(random.sample(self.pop1,len)))

    def rand_email(self):
        return str("".join(random.sample(self.pop1,5)) + "@" + "".join(random.sample(self.pop1,5))+ "." + "".join(random.sample(self.pop1,3)))

    def rand_val_digit(self, len):
        return str("".join(random.sample(self.pop2,len)))

    def setUp(self):
        self.eg = registration_page(link.lnk)

    def test_invalid_data(self):
        self.eg.first_name.inputField.send_keys(self.rand_val_invalid(8))
        self.eg.last_name.inputField.send_keys(self.rand_val_invalid(8))
        self.eg.email.inputField.send_keys(self.rand_val_invalid(8))
        self.eg.phone_number.inputField.send_keys(self.rand_val_invalid(8))
        self.eg.address.inputField.send_keys(self.rand_val_invalid(8))
        self.eg.city.inputField.send_keys(self.rand_val_invalid(8))
        self.eg.zip.inputField.send_keys(self.rand_val_invalid(8))
        self.eg.username.inputField.send_keys(self.rand_val_invalid(8))
        value = self.rand_val_invalid(8)
        self.eg.password.inputField.send_keys(value)
        self.eg.password_confirm.inputField.send_keys(value)
        self.eg.form.click()

        assert self.eg.first_name.errorMsg.text == self.eg.first_name.error_invalid_characters
        assert self.eg.last_name.errorMsg.text == self.eg.last_name.error_invalid_characters
        assert self.eg.email.errorMsg.text == self.eg.email.error_invalid_characters
        assert self.eg.phone_number.errorMsg.text == self.eg.phone_number.error_invalid_characters
        assert self.eg.address.errorMsg.text == self.eg.address.error_invalid_characters
        assert self.eg.city.errorMsg.text == self.eg.city.error_invalid_characters
        assert self.eg.zip.errorMsg.text == self.eg.zip.error_invalid_characters
        assert self.eg.username.errorMsg.text == self.eg.username.error_invalid_characters
        assert self.eg.password.errorMsg.text == self.eg.password.error_invalid_characters
        assert self.eg.password_confirm.errorMsg.text == self.eg.password_confirm.error_invalid_characters

    def test_empty_data(self):
        self.eg.button.click()
        assert self.eg.first_name.errorMsg.text == self.eg.first_name.error_empty_data
        assert self.eg.last_name.errorMsg.text == self.eg.last_name.error_empty_data
        assert self.eg.email.errorMsg.text == self.eg.email.error_empty_data
        assert self.eg.phone_number.errorMsg.text == self.eg.phone_number.error_empty_data
        assert self.eg.address.errorMsg.text == self.eg.address.error_empty_data
        assert self.eg.city.errorMsg.text == self.eg.city.error_empty_data
        assert self.eg.zip.errorMsg.text == self.eg.zip.error_empty_data
        assert self.eg.username.errorMsg.text == self.eg.username.error_empty_data
        assert self.eg.password.errorMsg.text == self.eg.password.error_empty_data
        assert self.eg.password_confirm.errorMsg.text == self.eg.password_confirm.error_empty_data

    def test_valid_data(self):
        self.eg.first_name.inputField.send_keys(self.rand_val_valid(8))
        self.eg.last_name.inputField.send_keys(self.rand_val_valid(8))
        self.eg.email.inputField.send_keys(self.rand_email())
        self.eg.phone_number.inputField.send_keys(self.rand_val_digit(10))
        self.eg.address.inputField.send_keys(self.rand_val_valid(8))
        self.eg.city.inputField.send_keys(self.rand_val_valid(8))
        self.eg.zip.inputField.send_keys(self.rand_val_valid(8))
        self.eg.username.inputField.send_keys(self.rand_val_valid(8))
        value = self.rand_val_valid(8)
        self.eg.password.inputField.send_keys(value)
        self.eg.password_confirm.inputField.send_keys(value)
        self.eg.button.click()

        time.sleep(30)
        assert self.eg.driver.find_element_by_class_name("submit_error_text_msg").text, "Registration Failed!"

    def test_short_data(self):
        self.eg.phone_number.inputField.send_keys(self.rand_val_digit(8))
        self.eg.address.inputField.send_keys(self.rand_val_valid(1))
        self.eg.username.inputField.send_keys(self.rand_val_valid(4))
        value = self.rand_val_valid(4)
        self.eg.password.inputField.send_keys(value)
        self.eg.password_confirm.inputField.send_keys(value)

        self.eg.button.click()

        assert self.eg.phone_number.errorMsg.text == self.eg.phone_number.error_invalid_length
        assert self.eg.address.errorMsg.text == self.eg.address.error_invalid_length
        assert self.eg.username.errorMsg.text == self.eg.username.error_invalid_length
        assert self.eg.password.errorMsg.text == self.eg.password.error_invalid_length
        assert self.eg.password_confirm.errorMsg.text == self.eg.password_confirm.error_invalid_length

    def test_long_data(self):
        self.eg.first_name.inputField.send_keys(self.rand_val_valid(51))
        self.eg.last_name.inputField.send_keys(self.rand_val_valid(51))
        self.eg.phone_number.inputField.send_keys(self.rand_val_digit(21))
        self.eg.address.inputField.send_keys(self.rand_val_valid(161))
        self.eg.zip.inputField.send_keys(self.rand_val_digit(21))
        self.eg.username.inputField.send_keys(self.rand_val_valid(17))
        value = self.rand_val_valid(11)
        self.eg.password.inputField.send_keys(value)
        self.eg.password_confirm.inputField.send_keys(value)


        self.eg.button.click()

        assert self.eg.first_name.errorMsg.text == self.eg.first_name.error_invalid_length
        assert self.eg.last_name.errorMsg.text == self.eg.last_name.error_invalid_length
        assert self.eg.phone_number.errorMsg.text == self.eg.phone_number.error_invalid_length
        assert self.eg.address.errorMsg.text == self.eg.address.error_invalid_length
        assert self.eg.zip.errorMsg.text == self.eg.zip.error_invalid_length
        assert self.eg.username.errorMsg.text == self.eg.username.error_invalid_length
        assert self.eg.password.errorMsg.text == self.eg.password.error_invalid_length
        assert self.eg.password_confirm.errorMsg.text == self.eg.password_confirm.error_invalid_length

    def test_password_missmatch(self):
        self.eg.password.inputField.send_keys(self.rand_val_valid(10))
        self.eg.password_confirm.inputField.send_keys(self.rand_val_valid(10))
        self.eg.button.click()
        assert self.eg.password_confirm.errorMsg.text == self.eg.password_confirm.error_password_missmatch

    def tearDown(self):
        #time.sleep(2)
        self.eg.driver.close()

if __name__ == "__main__":
    unittest.main()