import os

# Retrieve credentials from environment variables
# LT_USERNAME = os.getenv("LT_USERNAME")
# LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY")

LT_USERNAME = "gautamj"
LT_ACCESS_KEY = "LT_gMoYpF64OjFAc40cjhSyg2QAEK5EWj1Rqhv9iXrPpP1IDca"

APPIUM_SERVER = f"https://{LT_USERNAME}:{LT_ACCESS_KEY}@mobile-hub.lambdatest.com/wd/hub"

CAPS_ANDROID = {
    "build": "Python Appium Calculator Test",
    "platformName": "Android",
    "automationName": "flutter",
    "platformVersion": "13",
    "deviceName": "Galaxy S23+",
    "app": "lt://APP1016045521739462030652329",
    "isRealMobile": True
}

CAPS_IOS = {
    "build": "Python Appium Calculator Test",
    "platformName": "iOS",
    "automationName": "flutter",
    "platformVersion": "13",
    "deviceName": "iPhone 15 Pro",
    "app": "lt://APP1016045521739462030652329",
    "isRealMobile": True
}
