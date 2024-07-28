from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_wikipedia_real_device():
    with step('Language'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/option_label')).should(
            have.text('Русский'))

    with step('Next welcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Should be text'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Новые способы исследований'))

    with step('Next welcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Should be text'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Списки для чтения с синхронизацией'))

    with step('Next welcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Should be text'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Данные и конфиденциальность'))

    with step('Stat button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).click()

