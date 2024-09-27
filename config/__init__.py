from config.url import Url
from config.capabilities import Container

url = Url()
container = Container(capabilities={
    "browserName": "chrome",
    "browserVersion": "128.0",
    "selenoid:options": {
        "enableVideo": True,
        "downloadsEnabled": True
    }
},
    command_executor="http://localhost:4444/wd/hub",
)
