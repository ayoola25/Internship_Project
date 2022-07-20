import allure
from allure import attach
from allure_commons.types import AttachmentType
from app.application import Application

from reporting.browserstack_api import BSSession
from support.get_env import get_bs_key, get_bs_user

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.events import EventFiringWebDriver

from support.logger import logger, MyListener

# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
bs_user = 'ayoolaladapo_81yBFZ'
bs_key = 'L9EXxsyy9wxVm8yS6zMU'

# Allure command:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page.feature


def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    context.driver = webdriver.Chrome(executable_path="./chromedriver")
    # context.driver = webdriver.Firefox(executable_path='C:\\Users\\EZ-Trainer\\Desktop\\python-selenium-automation\\geckodriver.exe')
    # context.driver = webdriver.Safari()

    # HEADLESS MODE
    # options =webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')

    ### EventFiringWebDriver - log file ###
    ### for drivers ###
    context.driver = EventFiringWebDriver(webdriver.Chrome(executable_path="./chromedriver"), MyListener())
    # for headless mode ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options = options), MyListener())

    ### for browerstack ###
    # desired_cap = {
    #     'browser': 'Firefox',    #'Chrome',
    #     'os': 'Windows',
    #     'os_version': '10',
    #     'browser_version': 'latest',
    #     'browserstack.local': 'false',
    #     'name': test_name
    # }
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(3)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step.name}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step.name}')
        # Attach a screenshot to Allure report in case the step fails
        attach(
            context.driver.get_screenshot_as_png(),
            name=f'{step.name}.png',
            attachment_type=AttachmentType.PNG
        )
        # Mark test case as FAILED on BrowserStack:
        context.driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Step failed"}}')


def after_scenario(context, feature):
    # bs_session = BSSession(get_bs_user(), bs_key, context.driver.session_id)
    # bs_link = bs_session.get_browser_url()
    # #  If run via BS, attach link to a remote BS session to the report
    # attach(bs_link, name='BrowserStack Session', attachment_type=AttachmentType.URI_LIST)

    context.driver.delete_all_cookies()
    context.driver.quit()
    logger.info('Scenario finished.\n\n')
