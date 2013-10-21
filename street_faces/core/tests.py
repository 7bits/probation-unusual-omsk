# -*- coding: utf-8 -*-
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from django.contrib.auth.models import User


def input_login(self, user_name, user_pass):
    self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
    username_input = self.selenium.find_element_by_name("username")
    username_input.send_keys(user_name)
    password_input = self.selenium.find_element_by_name("password")
    password_input.send_keys(user_pass)
    self.selenium.find_element_by_name("login").click()


class login_test(LiveServerTestCase):
    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(login_test, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(login_test, cls).tearDownClass()

    def test_login_ok(self):
        user_name = "test2"
        user_pass = "test2"
        new_user = User.objects.create_user(user_name, None, user_pass)
        input_login(self, user_name, user_pass)
        WebDriverWait(self.selenium, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CLASS_NAME, "title-index")))

    def test_login_failed(self):
        user_name = ""
        user_pass = ""
        input_login(self, user_name, user_pass)
        WebDriverWait(self.selenium, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CLASS_NAME, "error-login")))
