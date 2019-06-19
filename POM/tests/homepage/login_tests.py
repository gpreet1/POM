from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from pages.homepage.login_page import LoginPage
from utilities.teststatus import statusCheck
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = statusCheck(self.driver)

    def test_validLogin(self):
        # login verification
        loginResult1 = self.lp.verifyLogin()
        self.ts.mark(loginResult1, "Login was successful")
        loginResult2 = self.lp.verifyTitle()
        self.ts.markFinal("test_validLogin", loginResult2, "Title")


