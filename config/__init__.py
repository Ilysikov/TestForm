from config.url import Url
from config.container import Container

url = Url()
container = Container(capabilities = {
    "browserName": "chrome",
    "browserVersion": "128.0",
    "selenoid:options": {
        "enableVideo": True,
        "screenResolution": "1280x1024x24",
        "downloadsEnabled":True
    }
},
    command_executor="http://localhost:4444/wd/hub",
)