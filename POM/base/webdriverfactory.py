from selenium import webdriver
import os

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):

        baseURL = "http://apexdcsqa.azurewebsites.net/auth/login"
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome(executable_path="C:\\Users\\GSingh\\PycharmProjects\\POM\\drivers\\chromedriver.exe")
        else:
            driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseURL)
        return driver