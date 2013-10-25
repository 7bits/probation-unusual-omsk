# -*- coding: utf-8 -*-
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


def input_subscription (self, user_email):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys(user_email)
        self.selenium.find_element_by_id("subscription-button").click()
        alert = self.selenium.switch_to_alert()
        alert_text = alert.text
        alert.accept()
        return alert_text
    
class FestSubsription(LiveServerTestCase):
    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(FestSubsription, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(FestSubsription, cls).tearDownClass()

    def test_subscription_ok(self):
        user_email = "test2@mail.ru"
        alert_text = input_subscription(self, user_email)
        self.assertEqual(alert_text, u"Спасибо за подписку!")
        
    def test_subscription_failed(self):
        user_email = "test2mail.ru"
        alert_text = input_subscription(self, user_email)
        self.assertEqual(alert_text, u"Неправильный e-mail!")
