# 🧪 Appium Flutter Integration Testing on LambdaTest


Test your **Flutter apps** on **LambdaTest Android Emulators** and **iOS Simulators** using the **Appium Flutter Integration Driver**.

---


## 🚀 Overview

LambdaTest supports testing Flutter apps using the [`appium-flutter-integration-driver`](https://github.com/AppiumTestDistribution/appium-flutter-integration-driver). This setup allows you to run tests in **Python**, **Java**, **JS**, and other languages supported by Appium, all while automatically managing Flutter’s rendering cycles and eliminating context switching.


## ℹ️ Compatibility & Requirements

The Appium Flutter Integration Driver tests on LambdaTest are supported with the following platform versions:

- Android: Version **12 and above** (Emulators)
- iOS: Version **14.2 and above** (Simulators)
- These tests are executed using **Appium 2.x versions**.  

📌 For a full list of supported capabilities, visit the [LambdaTest Capability Generator](https://www.lambdatest.com/capabilities-generator/)

---


## 📦 Prerequisites

- A [LambdaTest](https://www.lambdatest.com/) account
- A Flutter project


## 🔧 Prepare the app with Flutter Integration Server

1. In your Flutter app's `pubspec.yaml`, add the following dependencies:

   Get the latest version from `https://pub.dev/packages/appium_flutter_server/install`

   ```yaml
   dev_dependencies:
     appium_flutter_server: 0.0.27
   ```

2. Create a directory called `integration_test` in the root of your Flutter project.
3. Create a file called `appium_test.dart` in the `integration_test` directory.
4. Add the following code to the `appium_test.dart` file:

   ```dart
   import 'package:appium_flutter_server/appium_flutter_server.dart';
   import 'package:appium_testing_app/main.dart';

   void main() {
     initializeTest(app: const MyApp());
   }
   ```
   If you are in need to configure certain prerequisites before the testing app is loaded, you can try the following code:
   ```dart
   import 'package:appium_testing_app/main.dart'; as app;
   void main() {
     initializeTest(
       callback: (WidgetTester tester) async {
          // Perform any prerequisite steps or initialize any dependencies required by the app
          // and make sure to pump the app widget using below statement.
          await tester.pumpWidget(const app.MyApp());
       },
     );
   }
   ```

5. Build the Android app:

   ```bash
   ./gradlew app:assembleDebug -Ptarget=`pwd`/../integration_test/appium.dart
   ```

6. Build the iOS app:
    For Simulator - Debug mode
    ```bash
      flutter build ios integration_test/appium.dart --simulator
    ```



## 📤 Upload Your App to LambdaTest
Before running tests, you need to **upload your Flutter app (.apk or .zip) to LambdaTest** and get the **app ID**.

### **1️⃣ Sign in to LambdaTest**
- Go to [LambdaTest](https://www.lambdatest.com/)
- Log in to your account

### **2️⃣ Upload Your App**
- Navigate to **App Automation** → **Upload App**
- Upload your `.apk` (Android) or `.zip` (iOS) file
- Once uploaded, **copy the `app ID`** (e.g., `lt://APP123456789123456789`)

### **3️⃣ Update `config.py` with App ID and Credentials**
Open `configs/config.py` and update:
```python
APPIUM_SERVER = "https://<USERNAME>:<ACCESS_KEY>@mobile-hub.lambdatest.com/wd/hub"

CAPS_ANDROID = {
    "lt:options": {
		"w3c": True,
        "build": "Flutter Integration Android",
        "name": "Counter App Test",
        "platformName": "Android",
        "automationName": "FlutterIntegration",
        "platformVersion": "15",
        "deviceName": "Galaxy S25",
        "app": "lt://APP123456789123456789", # .apk 
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
        "app": "lt://APP123456789123456789", # .zip
    }
}
```
📌 **Replace `<USERNAME>` and `<ACCESS_KEY>`** with your LambdaTest credentials.  

---


## 🛠️ Running Instructions

### **1️⃣ Clone the Repository**
Open a terminal and run:
```bash
git clone https://github.com/gautam-jain-dev/flutter-integration-app-automation.git
cd flutter-integration-app-automation
```

### **2️⃣ Create a Virtual Environment**
To keep dependencies isolated, create a virtual environment:
```bash
python -m venv venv
```
Activate the environment:  
- **Windows**:  
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux**:  
  ```bash
  source venv/bin/activate
  ```

### **3️⃣ Install Dependencies**
Install all required Python packages:
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Flutter Test Script**
Execute the test script:
```bash
python -m tests.test_flutter_integration --os <ios/android>
```

---


## 📁 Project Structure
```bash
flutter-integration-app-automation/
│── configs/
│   ├── __init__.py
│   ├── config.py  # Stores Appium capabilities
│── tests/
│   ├── __init__.py
│   ├── test_flutter_integration.py  # Main test script
│── requirements.txt  # Python dependencies
│── SampleApp  # Sample Apps
│   ├── flutterIntegrationCounter.apk # android app
│   ├── flutterIntegrationCounter.zip # ios simulator zip
│── README.md  # Documentation
```

---