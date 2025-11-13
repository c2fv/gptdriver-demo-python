from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from gptdriver_client import GptDriver

if __name__ == "__main__":
    options = UiAutomator2Options()
    options.load_capabilities({
        "platformName": "Android",
        "platformVersion": "14.0",
        "deviceName": "emulator-5554",
        "automationName": "UiAutomator2",
        "gptdriver:apiKey": "<YOUR_API_KEY>",
    })

    gptd = GptDriver(command_executor="http://localhost:4723", options=options)

    # Example of using self-healing find_element
    gptd.find_element(by=AppiumBy.ID, value="com.example.app:id/login").click()

    # Self healing disabled for this element
    gptd.find_element(by=AppiumBy.ID, value="com.example.app:id/register", enable_self_healing=False).click()

    # ... other actions ...
    gptd.set_session_status("success")
