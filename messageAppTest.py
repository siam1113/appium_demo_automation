import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.google.android.apps.messaging',
    appActivity='ui.ConversationListActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def testNewConversation(self) -> None:
        # Click on New Conversation Button
        newConversationBtn = self.driver.find_element(
            by=AppiumBy.ID, value='com.google.android.apps.messaging:id/start_new_conversation_button')
        self.driver.implicitly_wait(15)
        newConversationBtn.click()
        self.driver.implicitly_wait(15)

        # Verify toggle button and back button
        backBtn = self.driver.find_element(
            by=AppiumBy.CLASS_NAME, value='android.widget.ImageButton')
        toggle = self.driver.find_element(
            by=AppiumBy.ID, value='com.google.android.apps.messaging:id/action_ime_dialpad_toggle')
        backBtn.is_displayed()
        toggle.is_displayed()
        self.driver.get_screenshot_as_file("messageNewConversationPage.png")

        # Click on back button and Verify New Conversation Button
        backBtn.click()
        backBtn.click()
        newConversationBtn.is_displayed()
        self.driver.get_screenshot_as_file("messageHomePage.png")


if __name__ == '__main__':
    unittest.main()
