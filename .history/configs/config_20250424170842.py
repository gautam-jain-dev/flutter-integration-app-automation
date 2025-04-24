import os

# Retrieve credentials from environment variables
LT_USERNAME = os.getenv("LT_USERNAME")
LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY")

APPIUM_SERVER = f"https://{LT_USERNAME}:{LT_ACCESS_KEY}@stage-mobile-hub.lambdatestinternal.com/wd/hub"

CAPS_ANDROID = {
    "lt:options": {
		"w3c": True,
        "build": "Flutter Integration Android",
        "name": "Counter App Test",
        "platformName": "Android",
        "automationName": "FlutterIntegration",
        "platformVersion": "15",
        "deviceName": "Galaxy S25",
        "app": "lt://APP10104192521745492613950258",
    }
}

CAPS_IOS = {
    "lt:options": {
		"w3c": True,
        "build": "Flutter Integration iOS",
        "name": "Counter App Test",
        "platformName": "iOS",
        "automationName": "FlutterIntegration",
        "platformVersion": "18.1",
        "deviceName": "iPhone 16 Pro",
        "app": "lt://APP10104192521745492652411386",
    }
}
