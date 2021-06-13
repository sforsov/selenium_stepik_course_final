from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ar ca cs da de el en fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans")


@pytest.fixture(scope="function")
def browser(request):
    languages = "ar ca cs da de el en fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans"
    language = request.config.getoption("language")
    if (language + " ") in languages:
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        print("\nlanguage {} not supported :(\ntry: ar ca cs da de el fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en".format(language))
        pytest.fail("Wrong Language")
        # assert 0
    yield browser
    print("\nquit browser..")
    browser.quit()
    