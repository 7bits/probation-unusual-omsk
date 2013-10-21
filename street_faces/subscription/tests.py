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


def input_subscription (self, user_email):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys(user_email)
        self.selenium.find_element_by_id("subscription-button").click()
        alert = self.selenium.switch_to_alert()
        alert_text = alert.text
        alert.accept()
        return alert_text
    
class test_subsription(LiveServerTestCase):
    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(test_subsription, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(test_subsription, cls).tearDownClass()

    def test_subsription_ok(self):
        user_email = "test2@mail.ru"
        alert_text = input_subscription(self, user_email)
        self.assertEqual(alert_text, u"Спасибо за подписку!")
        
    def test_subsription_failed(self):
        user_email = "test2mail.ru"
        alert_text = input_subscription(self, user_email)
        self.assertEqual(alert_text, u"Неправильный e-mail!")
