from appium.options.android import UiAutomator2Options
from gptdriver_client import GptDriver
from appium import webdriver

if __name__ == "__main__":
    options = UiAutomator2Options()
    options.load_capabilities({
        "platformName": "Android",
        "platformVersion": "14.0",
        "deviceName": "emulator-5554",
        "automationName": "UiAutomator2",
    })
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)

    gptd = GptDriver(api_key="<YOUR_API_KEY>", driver=driver)

    gptd.execute("Tap on the Gmail app")
    # ... other actions ...
    gptd.set_session_status("success")
