import allure
import pytest
import os
from utils import attach
from appium.options.android import UiAutomator2Options
from appium import webdriver
from selene import browser
from dotenv import load_dotenv
import config

load_dotenv()
context = os.getenv('context')


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options()

    if context == 'emulator':
        load_dotenv(dotenv_path='.env.emulator')
    elif context == 'real_device':
        load_dotenv(dotenv_path='.env.real_device')
    elif context == 'bstack':
        load_dotenv(dotenv_path='.env.bstack')
        with allure.step('Configurate options'):
            user_name = os.getenv("USER_NAME")
            access_key = os.getenv("ACCESS_KEY")
            options.set_capability(
                # Set other BrowserStack capabilities
                'bstack:options', {
                    "projectName": "First Python project",
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",

                    "userName": user_name,
                    "accessKey": access_key,
                })

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)

    yield

    if context == 'bstack':
        attach.add_screenshot(browser)
        attach.add_xml(browser)
        session_id = browser.driver.session_id
        attach.add_video(session_id)

    with allure.step('tear down app session'):
        browser.quit()


