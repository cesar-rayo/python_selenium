import sys
sys.path.append('./pages')

import json
import pytest
import selenium.webdriver
from selenium.webdriver.chrome.options import Options

from constants import CHROME_PATH, FIREFOX_PATH
# scope=session runs once before the entire suite
@pytest.fixture
def config(scope="session"):
    with open('config.json') as config_file:
        config = json.load(config_file)

    assert config['browser'] in ['Chrome', 'Firefox', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0
    return config

@pytest.fixture
def web_browser(config):
    if config['browser'] == 'Chrome':
        driver = selenium.webdriver.Chrome(
            executable_path=CHROME_PATH)
    elif config['browser'] == 'Firefox':
        driver = selenium.webdriver.Firefox(
            executable_path=FIREFOX_PATH)
    elif config['browser'] == 'Headless Chrome':
        opts = Options()
        opts.add_argument("--headless")
        driver = selenium.webdriver.Chrome(
            executable_path=CHROME_PATH,
            options = opts)
    else:
        raise Exception("Browser {} is not supported".format(
            config['browser']))
    driver.implicitly_wait(config['implicit_wait'])
    yield driver
    driver.quit()