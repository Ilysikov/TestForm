from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromOptions


class Container:
    browser = {'firefox': FirefoxOptions(), "chrome": ChromOptions()}

    def __init__(self, capabilities, command_executor):
        self.capabilities = capabilities
        self.options = self.browser[self.capabilities["browserName"]]
        self.options.browser_version = self.capabilities["browserVersion"]
        self.options.enable_downloads = True
        self.options.add_argument('--profile-directory=Default')
        self.options.set_capability("selenoid:options", self.capabilities["selenoid:options"])
        self.command_executor = command_executor
