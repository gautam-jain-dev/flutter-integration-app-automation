import time
from appium.webdriver import Remote
from appium.webdriver.extensions.flutter_integration.flutter_finder import FlutterFinder
from appium.options.common import AppiumOptions
from configs.config import APPIUM_SERVER, CAPS_ANDROID, CAPS_IOS
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--os", type=str, help="OS type (iOS or Android)")
args = parser.parse_args()

# Convert CAPS dictionary into AppiumOptions
options = AppiumOptions()
if args.os.lower() == "android":
options.load_capabilities(CAPS_ANDROID)

# Start Appium Driver with AppiumOptions
driver = Remote(command_executor=APPIUM_SERVER, options=options)

print("✅ Appium session started successfully!")

# ✅ Current Counter Value
time.sleep(1)
counter_text_finder = FlutterFinder.by_key('counter_value')
counter_text = driver.find_element(*counter_text_finder.as_args())
print("✅ Current Counter Value: ", counter_text.text)

# ✅ Click on "+" button 5 times
button_finder = FlutterFinder.by_key('increment')
counter_button = driver.find_element(*button_finder.as_args())

for i in range(5):
    time.sleep(1)
    counter_button.click()
    print(f"✅ Clicked on + {i+1} times")

# ✅ Current Counter Value after clicking 5 times
time.sleep(1)
counter_text_after = driver.find_element(*counter_text_finder.as_args())
print("✅ Current Counter Value after clicking 5 times: ", counter_text_after.text) 

driver.quit()
print("✅ Appium session closed.")
