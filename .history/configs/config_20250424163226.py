import os

# Retrieve credentials from environment variables
# LT_USERNAME = os.getenv("LT_USERNAME")
# LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY")

LT_USERNAME = "gautamj"
LT_ACCESS_KEY = "LT_gMoYpF64OjFAc40cjhSyg2QAEK5EWj1Rqhv9iXrPpP1IDca"

APPIUM_SERVER = f"https://{LT_USERNAME}:{LT_ACCESS_KEY}@stage-mobile-hub.lambdatestinternal.com/wd/hub"

CAPS_ANDROID = {
    "build": "Flutter Integration Android",
    "test": "Counter App Test",
    "platformName": "Android",
    "automationName": "flutter",
    "platformVersion": "15",
    "deviceName": "Galaxy S25",
    "app": "lt://APP1016045521739462030652329",
}

CAPS_IOS = {
    "build": "Flutter Integration iOS",
    "test": "Counter App Test",
    "platformName": "iOS",
    "automationName": "flutter",
    "platformVersion": "18.1",
    "deviceName": "iPhone 16 Pro",
    "app": "lt://APP1016045521739462030652329",
}
