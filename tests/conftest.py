import pytest
import selenium.webdriver.remote.webdriver
import os
import json

HUB_URL = os.environ["HUB_URL"]

@pytest.fixture
def config(scope='session'):
    with open('config.json') as config_file:
        config = json.load(config_file)

    assert config['browser'] in ('chrome', 'firefox', 'edge')
    assert isinstance(config['headless'], bool)
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    return config

@pytest.fixture(params=['chrome', 'firefox', 'edge'])
def driver(config, request):

    # configure options
    if request.param == 'chrome':
        opts = selenium.webdriver.ChromeOptions()
    elif request.param == 'firefox':
        opts = selenium.webdriver.FirefoxOptions()
    elif request.param == 'edge':
        opts = selenium.webdriver.EdgeOptions()

    if config['headless']:
        opts.add_argument("--headless")

    # initalize the webdriver intance
    b = selenium.webdriver.Remote(command_executor=HUB_URL, options=opts)

    # implicity wait for page to load
    b.implicitly_wait(config['implicit_wait'])

    # return webdriver
    yield b

    # quit the webdriver
    b.quit()
